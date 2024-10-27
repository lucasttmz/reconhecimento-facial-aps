from pydantic import BaseModel, Field

from sistema_escolar.modelos.materia import UsuarioSchema, MateriaPublicSchema


class Boletim(BaseModel):
    """Modelo do Boletim no BD"""

    id_boletim: int
    id_usuario: int
    id_materia: int
    nota: float | None
    faltas: int


class BoletimParaAlunoSchema(BaseModel):
    """Dados retornados no boletim para os alunos (sem os seus dados)"""

    materia: MateriaPublicSchema
    nota: float | None
    faltas: int


class BoletimParaProfessorSchema(BaseModel):
    """Dados retornados no boletim para os professor (com dados do aluno)"""

    aluno: UsuarioSchema
    materia: MateriaPublicSchema
    nota: float | None
    faltas: int


class AtualizarBoletimSchema(BaseModel):
    """Dados necessários para atualizar notas e faltas"""

    faltas: int = Field(ge=0)
    nota: float = Field(ge=0, le=10)
