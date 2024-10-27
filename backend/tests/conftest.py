import base64
from random import randint

import cv2
from fastapi.testclient import TestClient
import numpy as np
import pytest

from sistema_escolar.main import app
from tests.util import criar_jwt


@pytest.fixture
def cliente():
    return TestClient(app)


@pytest.fixture(scope="session")
def aluno():
    token = criar_jwt(1).get("token")
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(scope="session")
def professor():
    token = criar_jwt(2).get("token")
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(scope="session")
def diretor():
    token = criar_jwt(3).get("token")
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def materia_valida():
    return {
        "nome": "string",
        "codigo_professor": 15,
        "data_inicio": "2024-10-18",
        "data_fim": "2024-10-18",
        "codigo_alunos": [],
    }


@pytest.fixture
def notas_e_faltas():
    return {"faltas": randint(0, 10), "nota": randint(0, 10)}


@pytest.fixture
def alteracao_de_cargo():
    return {"tipo": randint(1, 3)}


@pytest.fixture(scope="session")
def imagem_base64():
    # Imagem de um pixel só para ser válida
    imagem = np.array([[[0, 0, 255]]], dtype=np.uint8)
    _, buffer = cv2.imencode(".jpg", imagem)
    imagem_base64 = base64.b64encode(buffer).decode("utf-8")

    return f"data:image/jpeg;base64,{imagem_base64}"
