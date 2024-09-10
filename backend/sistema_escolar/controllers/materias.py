from datetime import datetime, timedelta
from random import randint

from fastapi import APIRouter

from sistema_escolar.modelos import MateriaSchema

router = APIRouter(prefix="/materias", tags=["materias"])

@router.get("/")
def listar_materias():
    """Visualizar todas as materias"""
    return [
       {
           "nome": "portugues",
           "professor": "reverdan",
           "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
           "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
       },
       {
           "nome": "matematica",
           "professor": "samuel",
           "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
           "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
       }
    ]

@router.get("/{id_materia}")
def pesquisar_materias(id_materia: int):
    """Visualizar informações da materia"""
    return {
       "nome": f"nome da materia {id_materia}",
       "professor": f"professor da materia {id_materia}",
       "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
       "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
    }

@router.get("/{id_materia}/aluno/{id_aluno}")
def materias_do_aluno(id_materia: int, id_aluno: int):
    """Boletim do aluno na matéria"""
    return {
        "nota": 10,
        "faltas": 2
    }

@router.post("/{id_materia}/aluno/{id_aluno}/nota")
def lancar_nota(id_materia: int, id_aluno: int):
    """Lançar nota para o aluno"""

@router.post("/{id_materia}/aluno/{id_aluno}/falta")
def lancar_falta(id_materia: int, id_aluno: int):
    """Lançar falta para o aluno"""

@router.put("/{id_materia}/aluno/{id_aluno}/nota")
def atualizar_nota(id_materia: int, id_aluno: int):
    """Atualizar nota para o aluno"""

@router.put("/{id_materia}/aluno/{id_aluno}/falta")
def atualizar_falta(id_materia: int, id_aluno: int):
    """Atualizar falta para o aluno"""
