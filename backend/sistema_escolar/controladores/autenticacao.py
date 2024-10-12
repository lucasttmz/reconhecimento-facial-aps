from datetime import datetime, timedelta
from http import HTTPStatus
from os import environ
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import encode, decode, DecodeError

from sistema_escolar.controladores.biometria import BiometriaControle, USUARIO_NAO_RECONHECIDO
from sistema_escolar.controladores.usuarios import UsuarioControle
from sistema_escolar.modelos.autenticacao import RegistroSchema, Token
from sistema_escolar.modelos.genericos import MensagemSchema


CHAVE = environ.get("CHAVE_TOKEN", "seta la a chave")
EXPIRACAO_MINUTOS = int(environ.get("EXPIRACAO_TOKEN", 180))

T_Token = Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]

def usuario_autenticado(token: T_Token):
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
    def decodificar_token(token: T_Token) -> dict:
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

    def registrar_usuario(self, dados: RegistroSchema, biometria: BiometriaControle) -> MensagemSchema:
        return MensagemSchema(mensagem="Registrado com sucesso!")

    def realizar_login(self, fotos: list[str], biometria: BiometriaControle) -> Token: 
        id_usuario = biometria.realizar_biometria(fotos)
        if id_usuario == USUARIO_NAO_RECONHECIDO:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, 
                detail="Login falhou. Tente novamente"
            )
        
        # Cria o token com os dados do usuário reconhecido
        usuario = UsuarioControle().listar_info_usuario(id_usuario)
        dados = {"sub":usuario.nome, "user_id": id_usuario, "permissions": usuario.tipo}

        return Token(token=self.criar_token(dados), tipo="Bearer")
        

