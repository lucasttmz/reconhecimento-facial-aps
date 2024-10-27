from http import HTTPStatus

import pytest


def test_login_com_codigo_invalido(cliente):
    resposta = cliente.post("http://127.0.0.1:8000/login", json={"codigo": "123", "fotos": []})
    assert resposta.status_code == HTTPStatus.UNAUTHORIZED
    assert resposta.json().get("detail") == "Login falhou. Código inválido"

def test_login_sem_imagens_suficientes(cliente):
    resposta = cliente.post("http://127.0.0.1:8000/login", json={"codigo": "L478D1AE", "fotos": []})
    assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert resposta.json().get("detail") == "Nenhuma foto enviada para autenticação"


def test_login_imagens_formato_invalido(cliente):
    resposta = cliente.post("http://127.0.0.1:8000/login", json={"codigo": "L478D1AE", "fotos": ["a"] * 10})
    assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert resposta.json().get("detail") == "Foto de autenticação em formato inválido"


@pytest.mark.slow
def test_tentativa_de_login_invalida(cliente, imagem_base64):
    resposta = cliente.post(
        "http://127.0.0.1:8000/login", json={"codigo": "L478D1AE", "fotos": [imagem_base64]}
    )
    assert resposta.status_code == HTTPStatus.UNAUTHORIZED
    assert resposta.json().get("detail") == "Login falhou. Tente novamente"


@pytest.mark.slow
def test_registro_sem_rostos(cliente, imagem_base64):
    dados = {"nome": "Nome Sobrenome", "fotos": [imagem_base64]}
    resposta = cliente.post("http://127.0.0.1:8000/registrar", json=dados)
    assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert (
        resposta.json().get("detail") == "Centralizar o rosto antes de tirar as fotos"
    )
