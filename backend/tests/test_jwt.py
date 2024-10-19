from fastapi import HTTPException
from fastapi.security import  HTTPAuthorizationCredentials
import pytest

from http import HTTPStatus

from sistema_escolar.controladores.autenticacao import AutenticacaoControle


def test_criacao_do_jwt():
    controle = AutenticacaoControle()

    token = controle.criar_token({"sub": "Sebastião", "user_id": 10, "permissions": 1})
    jwt = HTTPAuthorizationCredentials(credentials=token, scheme="Bearer")
    decodificado = controle.decodificar_token(jwt)

    assert decodificado.get("id") == 10
    assert decodificado.get("nome") == "Sebastião"
    assert decodificado.get("permissoes") == 1

    token = controle.criar_token({"sub": "Zé", "user_id": 7, "permissions": 2})
    jwt = HTTPAuthorizationCredentials(credentials=token, scheme="Bearer")
    decodificado = controle.decodificar_token(jwt)

    assert decodificado.get("permissoes") == 2

    token = controle.criar_token({"sub": "João", "user_id": 2, "permissions": 3})
    jwt = HTTPAuthorizationCredentials(credentials=token, scheme="Bearer")
    decodificado = controle.decodificar_token(jwt)

    assert decodificado.get("permissoes") == 3


def test_jwt_invalido():
    controle = AutenticacaoControle()

    with pytest.raises(HTTPException) as exc:
        controle.decodificar_token(HTTPAuthorizationCredentials(
            credentials="token invalido", scheme="Bearer"
        ))
        
        assert exc.value.args[0] == HTTPStatus.UNAUTHORIZED
        assert exc.value.args[1] == "Token inválido ou expirado"

    