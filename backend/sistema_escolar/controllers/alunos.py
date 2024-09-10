from fastapi import APIRouter

from sistema_escolar.modelos import UsuarioSchema

router = APIRouter(prefix="/alunos", tags=["alunos"])

@router.get("/", response_model=list[UsuarioSchema])
def todos_alunos():
    return [
        {
            "matricula": "123",
            "nome": "lucas",
            "tipo": 1,
        }, 
        {
            "matricula": "321",
            "nome": "felipe",
            "tipo": 2,
        },
    ]


@router.get("/{id_aluno}", response_model=UsuarioSchema)
def pesquisar_aluno(id_aluno: int):
    """Visualizar informações do aluno"""
    return {
        "matricula": f"matricula do {id_aluno}",
        "nome": f"nome do {id_aluno}",
        "tipo": (id_aluno % 3) or 3
    }


@router.get("/{id_aluno}/boletim")
def pesquisar_boletim_aluno(id_aluno: int):
    """Visualizar boletim do aluno"""
    return [
        {
            "materia": 1,
            "nota": 10,
            "faltas": 2
        },
        {
            "materia": 2,
            "nota": 9,
            "faltas": 0
        }
    ]
