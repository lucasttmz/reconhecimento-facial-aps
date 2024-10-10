from pydantic import BaseModel, Field

from sistema_escolar.modelos.materia import UsuarioSchema, MateriaPublicSchema


class Boletim(BaseModel):
    id_boletim: int
    id_usuario: int
    id_materia: int
    nota: float | None
    faltas: int


class BoletimParaAlunoSchema(BaseModel):
    materia: MateriaPublicSchema
    nota: float | None
    faltas: int


class BoletimParaProfessorSchema(BaseModel):
    aluno: UsuarioSchema
    materia: MateriaPublicSchema
    nota: float | None
    faltas: int


class AtualizarBoletimSchema(BaseModel):
    faltas: int = Field(ge=0)
    nota: float = Field(ge=0, le=10)
