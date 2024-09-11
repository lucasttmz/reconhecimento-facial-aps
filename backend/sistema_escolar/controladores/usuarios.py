from fastapi import APIRouter

from sistema_escolar.modelos import TipoUsuario

router = APIRouter(tags=["usuarios"])


@router.get("/alunos")
def listar_todos_alunos():
    """Lista todos os alunos"""
    return [
        {
            "matricula": "123",
            "nome": "lucas",
            "tipo": TipoUsuario.ALUNO,
        },
        {
            "matricula": "321",
            "nome": "felipe",
            "tipo": TipoUsuario.ALUNO,
        },
    ]


@router.get("/alunos/{id_aluno")
def pesquisar_aluno(id_aluno: int):
    """Exibe as informações de um aluno em específico"""
    return {
        "matricula": f"matricula do {id_aluno}",
        "nome": f"nome do {id_aluno}",
        "tipo": (id_aluno % 3) or 3,
    }


@router.get("/professores")
def listar_todos_professores():
    """Lista todos os alunos"""
    return [
        {
            "matricula": "123",
            "nome": "joao",
            "tipo": TipoUsuario.PROFESSOR,
        },
        {
            "matricula": "321",
            "nome": "maria",
            "tipo": TipoUsuario.PROFESSOR,
        },
    ]


@router.get("/professores/{id_professor}")
def pesquisar_professor(id_professor: int):
    """Exibe as informações de um professor em específico"""
    return {
        "matricula": f"matricula do {id_professor}",
        "nome": f"nome do {id_professor}",
        "tipo": TipoUsuario.PROFESSOR,
    }
