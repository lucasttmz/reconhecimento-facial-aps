from http import HTTPStatus


def test_aluno_pode_acessar_boletim(aluno, cliente):
    resposta = cliente.get("http://127.0.0.1:8000/boletim/", headers=aluno)
    assert resposta.status_code == HTTPStatus.OK

    resposta = cliente.get("http://127.0.0.1:8000/boletim/1", headers=aluno)
    assert resposta.status_code == HTTPStatus.OK


def test_aluno_nao_pode_acessar_rotas_de_materias(
    aluno, cliente, materia_valida, notas_e_faltas
):
    resposta = cliente.get("http://127.0.0.1:8000/materias/", headers=aluno)
    assert resposta.status_code == HTTPStatus.FORBIDDEN

    resposta = cliente.get("http://127.0.0.1:8000/materias/1", headers=aluno)
    assert resposta.status_code == HTTPStatus.FORBIDDEN

    resposta = cliente.get("http://127.0.0.1:8000/materias/1/aluno/1", headers=aluno)
    assert resposta.status_code == HTTPStatus.FORBIDDEN

    resposta = cliente.post(
        "http://127.0.0.1:8000/materias/", headers=aluno, json=materia_valida
    )
    assert resposta.status_code == HTTPStatus.FORBIDDEN

    resposta = cliente.put(
        "http://127.0.0.1:8000/materias/1", headers=aluno, json=materia_valida
    )
    assert resposta.status_code == HTTPStatus.FORBIDDEN

    resposta = cliente.put(
        "http://127.0.0.1:8000/materias/1/aluno/1", headers=aluno, json=notas_e_faltas
    )
    assert resposta.status_code == HTTPStatus.FORBIDDEN


def test_aluno_nao_pode_acessar_rotas_de_usuarios(aluno, cliente, alteracao_de_cargo):
    resposta = cliente.get("http://127.0.0.1:8000/alunos/", headers=aluno)
    assert resposta.status_code == HTTPStatus.FORBIDDEN

    resposta = cliente.get("http://127.0.0.1:8000/alunos/1", headers=aluno)
    assert resposta.status_code == HTTPStatus.FORBIDDEN

    resposta = cliente.get("http://127.0.0.1:8000/professores/", headers=aluno)
    assert resposta.status_code == HTTPStatus.FORBIDDEN

    resposta = cliente.get("http://127.0.0.1:8000/professores/1", headers=aluno)
    assert resposta.status_code == HTTPStatus.FORBIDDEN

    resposta = cliente.put(
        "http://127.0.0.1:8000/usuarios/1", headers=aluno, json=alteracao_de_cargo
    )
    assert resposta.status_code == HTTPStatus.FORBIDDEN


def test_professor_pode_acessar_suas_materias(professor, cliente):
    resposta = cliente.get("http://127.0.0.1:8000/materias/", headers=professor)
    assert resposta.status_code == HTTPStatus.OK

    resposta = cliente.get("http://127.0.0.1:8000/materias/1", headers=professor)
    assert resposta.status_code == HTTPStatus.OK


def test_professor_nao_pode_acessar_materias_outros_professores(professor, cliente):
    resposta = cliente.get("http://127.0.0.1:8000/materias/2", headers=professor)
    assert resposta.status_code == HTTPStatus.NOT_FOUND


def test_professor_pode_acessar_seus_alunos(professor, cliente):
    resposta = cliente.get("http://127.0.0.1:8000/alunos/", headers=professor)
    assert resposta.status_code == HTTPStatus.OK

    resposta = cliente.get("http://127.0.0.1:8000/alunos/16", headers=professor)
    assert resposta.status_code == HTTPStatus.OK

    resposta = cliente.get(
        "http://127.0.0.1:8000/materias/1/aluno/16", headers=professor
    )
    assert resposta.status_code == HTTPStatus.OK


def test_professor_nao_pode_acessar_alunos_que_ele_nao_da_aula(professor, cliente):
    resposta = cliente.get(
        "http://127.0.0.1:8000/materias/2/aluno/6", headers=professor
    )
    assert resposta.status_code == HTTPStatus.FORBIDDEN


def test_diretor_tem_permissoes_corretas(diretor, cliente):
    resposta = cliente.get("http://127.0.0.1:8000/materias/", headers=diretor)
    assert resposta.status_code == HTTPStatus.OK

    resposta = cliente.get("http://127.0.0.1:8000/materias/1", headers=diretor)
    assert resposta.status_code == HTTPStatus.OK

    resposta = cliente.get("http://127.0.0.1:8000/alunos/", headers=diretor)
    assert resposta.status_code == HTTPStatus.OK

    resposta = cliente.get("http://127.0.0.1:8000/alunos/1", headers=diretor)
    assert resposta.status_code == HTTPStatus.OK

    resposta = cliente.get("http://127.0.0.1:8000/professores/", headers=diretor)
    assert resposta.status_code == HTTPStatus.OK

    resposta = cliente.get("http://127.0.0.1:8000/professores/15", headers=diretor)
    assert resposta.status_code == HTTPStatus.OK
