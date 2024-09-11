from fastapi import APIRouter

from sistema_escolar.modelos.usuario import TipoUsuario, UsuarioSchema

router = APIRouter(tags=["usuarios"])


@router.get("/alunos", response_model=list[UsuarioSchema])
def listar_todos_alunos():
    """Lista todos os alunos"""
    return [
        {
            "codigo": "AL_LUC4S",
            "nome": "lucas",
            "tipo": TipoUsuario.ALUNO,
        },
        {
            "codigo": "AL_F3L1P3",
            "nome": "felipe",
            "tipo": TipoUsuario.ALUNO,
        },
    ]


@router.get("/alunos/{id_aluno", response_model=UsuarioSchema)
def pesquisar_aluno(id_aluno: int):
    """Exibe as informações de um aluno em específico"""
    return {
        "codigo": f"codigo do {id_aluno}",
        "nome": f"nome do {id_aluno}",
        "tipo": TipoUsuario.ALUNO,
    }


@router.get("/professores", response_model=list[UsuarioSchema])
def listar_todos_professores():
    """Lista todos os professores"""
    return [
        {
            "codigo": "PF_M4R14",
            "nome": "Maria",
            "tipo": TipoUsuario.PROFESSOR,
        },
        {
            "codigo": "PF_J040",
            "nome": "João",
            "tipo": TipoUsuario.PROFESSOR,
        },
    ]


@router.get("/professores/{id_professor}", response_model=UsuarioSchema)
def pesquisar_professor(id_professor: int):
    """Exibe as informações de um professor em específico"""
    return {
        "codigo": f"codigo do {id_professor}",
        "nome": f"nome do {id_professor}",
        "tipo": TipoUsuario.PROFESSOR,
    }
