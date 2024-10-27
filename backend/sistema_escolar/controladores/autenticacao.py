from datetime import datetime, timedelta
from http import HTTPStatus
from os import environ
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import encode, decode, DecodeError

from sistema_escolar.controladores.biometria import (
    BiometriaControle,
    USUARIO_NAO_RECONHECIDO,
)
from sistema_escolar.controladores.usuarios import UsuarioControle
from sistema_escolar.modelos.autenticacao import (
    RegistroSchema,
    Token,
    UsuarioRegistradoSchema,
)
from sistema_escolar.modelos.usuario import TipoUsuario

# Constantes relacionadas ao JWT
CHAVE = environ.get("CHAVE_TOKEN", "seta la a chave")
EXPIRACAO_MINUTOS = int(environ.get("EXPIRACAO_TOKEN", 180))

# Injeção de dependência do JWT
T_Token = Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]


def usuario_autenticado(token: T_Token):
    """Retorna o usuário autenticado através do token"""

    return AutenticacaoControle.decodificar_token(token)


def possui_permissao(usuario: dict, permitidos: list[TipoUsuario]):
    """Checa se o usuário tem a permissão"""

    return usuario.get("permissoes") in permitidos


class AutenticacaoControle:
    def criar_token(self, dados: dict) -> str:
        """Cria o JWT baseados nos dados junto com a expiração"""

        copia_dados = dados.copy()
        expiracao = datetime.utcnow() + timedelta(minutes=EXPIRACAO_MINUTOS)
        copia_dados.update({"exp": expiracao})
        token_jwt = encode(copia_dados, CHAVE)
        return token_jwt

    @staticmethod
    def decodificar_token(token: T_Token) -> dict:
        """Decodifica o JWT e checa se ele ainda está válido"""

        exc_invalido = HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Token inválido ou expirado",
        )

        try:
            # Decodificada os dados do token
            payload = decode(token.credentials, CHAVE, algorithms=["HS256"])
            nome = payload.get("sub")
            id_usuario = payload.get("user_id")
            permissoes = payload.get("permissions")

            # Se não encontrar nenhum deles quer dizer que o token está em formato inválido
            if not nome or not permissoes or not id_usuario:
                raise exc_invalido

        except DecodeError:
            raise exc_invalido

        return {"id": id_usuario, "nome": nome, "permissoes": permissoes}

    def registrar_usuario(
        self, dados: RegistroSchema, biometria_controle: BiometriaControle
    ) -> UsuarioRegistradoSchema:
        """Registra um novo usuário no BD e no modelo de reconhecimento facial"""

        usuario_controle = UsuarioControle()
        proximo_id = usuario_controle.sequencia_usuario() + 1
        biometria_controle.registrar_rosto(dados.fotos, proximo_id)

        return usuario_controle.criar_usuario(proximo_id, dados.nome.title())

    def realizar_login(
        self, codigo_esperado: str, fotos: list[str], biometria: BiometriaControle
    ) -> Token:
        """Realiza o login do usuário usando reconhecimento facial"""

        # Lê o ID do usuário referente ao código fornecido no form. de login
        id_esperado = UsuarioControle().listar_id_usuario_por_codigo(
            codigo_esperado.upper()
        )
        # Se o ID não for encontrado, já falha antes de realizar a biometria
        if id_esperado == USUARIO_NAO_RECONHECIDO:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Login falhou. Código inválido",
            )
        # Realiza a biometria comparando as fotos com o modelo treinado
        id_usuario = biometria.realizar_biometria(id_esperado, fotos)
        if id_usuario == USUARIO_NAO_RECONHECIDO:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Login falhou. Tente novamente",
            )
        # Cria o token com os dados do usuário reconhecido
        usuario = UsuarioControle().listar_info_usuario(id_usuario)
        dados = {
            "sub": usuario.nome,
            "user_id": id_usuario,
            "permissions": usuario.tipo,
        }

        return Token(token=self.criar_token(dados), tipo="Bearer")
