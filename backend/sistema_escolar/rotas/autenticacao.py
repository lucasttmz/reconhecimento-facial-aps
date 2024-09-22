from datetime import datetime, timedelta
from http import HTTPStatus
from os import environ
from random import randint
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import encode, decode, DecodeError

from sistema_escolar.modelos.autenticacao import LoginSchema, RegistroSchema, Token
from sistema_escolar.modelos.genericos import MensagemSchema


SECRET_KEY = environ.get("SECRET_KEY", "123")
EXPIRACAO_TOKEN_MIN = 60

jwt_token = HTTPBearer()
router = APIRouter(tags=["autenticacao"])


def usuario_logado(token: HTTPAuthorizationCredentials = Depends(jwt_token)):
    exc_invalido = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail="Token inválido ou expirado",
    )

    try:
        payload = decode(token.credentials, SECRET_KEY, algorithms=["HS256"])
        nome = payload.get("sub")
        id_usuario = payload.get("user_id")
        permissoes = payload.get("permissions")
        if not nome or not permissoes or not id_usuario:
            raise exc_invalido
    
        return {"id": id_usuario, "nome": nome, "permissoes": permissoes}
    except DecodeError:
        raise exc_invalido


def criar_token(dados: dict):
    copia_dados = dados.copy()
    expiracao = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
        minutes=EXPIRACAO_TOKEN_MIN
    )
    copia_dados.update({"exp": expiracao})
    token_jwt = encode(copia_dados, SECRET_KEY)
    return token_jwt


@router.post("/login", response_model=Token)
def login(fotos: LoginSchema):
    permissao = randint(1, 3)
    usuarios = ["Lucas", "Raul", "Samuel"]
    token = criar_token(dados={"sub": usuarios[permissao-1], "user_id":permissao+10, "permissions": permissao})
    return {"token": token, "tipo": "Bearer"}


@router.post("/registrar")
def registrar(dados: RegistroSchema):
    return MensagemSchema(mensagem="Registrado com sucesso!")


@router.get("/protegida")
def rota_protegida_testes(usuario: dict = Depends(usuario_logado)):
    return {"message": "Acesso permitido", "usuario": usuario}
