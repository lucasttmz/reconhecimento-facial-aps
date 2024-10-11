from datetime import datetime, timedelta
from http import HTTPStatus
from os import environ
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import encode, decode, DecodeError


from sistema_escolar.modelos.autenticacao import RegistroSchema
from sistema_escolar.modelos.genericos import MensagemSchema


CHAVE = environ.get("CHAVE_TOKEN", "seta la a chave")
EXPIRACAO_MINUTOS = int(environ.get("EXPIRACAO_TOKEN", 180))

Token = Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]

def usuario_autenticado(token: Token):
    return AutenticacaoControle.decodificar_token(token)
    

class AutenticacaoControle:
    def criar_token(self, dados: dict) -> str:
        copia_dados = dados.copy()
        expiracao = datetime.utcnow() + timedelta(
            minutes=EXPIRACAO_MINUTOS
        )
        copia_dados.update({"exp": expiracao})
        token_jwt = encode(copia_dados, CHAVE)
        return token_jwt
    
    @staticmethod
    def decodificar_token(token: Token) -> dict:
        exc_invalido = HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Token inválido ou expirado",
        )

        try:
            payload = decode(token.credentials, CHAVE, algorithms=["HS256"])
            nome = payload.get("sub")
            id_usuario = payload.get("user_id")
            permissoes = payload.get("permissions")
            if not nome or not permissoes or not id_usuario:
                raise exc_invalido
        
            return {"id": id_usuario, "nome": nome, "permissoes": permissoes}
        except DecodeError:
            raise exc_invalido

    def registrar_usuario(self, dados: RegistroSchema) -> MensagemSchema:
        return MensagemSchema(mensagem="Registrado com sucesso!")

    def realizar_login(self, fotos: list[str]): ...

    def realizar_biometria(self, fotos: list[str]): ...

