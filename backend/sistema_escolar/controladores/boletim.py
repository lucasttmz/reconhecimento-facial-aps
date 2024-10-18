from fastapi import HTTPException

from sistema_escolar.controladores.materias import MateriaControle
from sistema_escolar.controladores.usuarios import UsuarioControle
from sistema_escolar.dal.boletim import BoletimDAO
from sistema_escolar.modelos.boletim import (
    BoletimParaAlunoSchema,
    BoletimParaProfessorSchema,
)


class BoletimControle:
    def listar_boletim_aluno(self, id_aluno: int) -> list[BoletimParaAlunoSchema]:
        boletimDAO = BoletimDAO()
        boletins = boletimDAO.buscar_todos_boletins_aluno(id_aluno)

        if boletins is None:
            raise HTTPException(404)

        resultado = []
        for boletim in boletins:
            materia = MateriaControle().listar_public_materia(boletim.id_materia)

            boletim_schema = {
                "materia": materia,
                "nota": boletim.nota,
                "faltas": boletim.faltas,
            }
            resultado.append(BoletimParaAlunoSchema(**boletim_schema))

        return resultado

    def listar_boletim_aluno_em_materia(
        self, id_aluno: int, id_materia
    ) -> BoletimParaAlunoSchema:
        boletimDAO = BoletimDAO()
        boletim = boletimDAO.buscar_boletim_do_aluno(id_aluno, id_materia)

        if boletim is None:
            raise HTTPException(404)

        materia = MateriaControle().listar_public_materia(boletim.id_materia)
        boletim_schema = {
            "materia": materia,
            "nota": boletim.nota,
            "faltas": boletim.faltas,
        }

        return BoletimParaAlunoSchema(**boletim_schema)

    def listar_boletim_para_professores(
        self, id_aluno: int, id_materia: int
    ) -> BoletimParaProfessorSchema:
        aluno = UsuarioControle().listar_info_aluno(id_aluno)
        boletim = self.listar_boletim_aluno_em_materia(id_aluno, id_materia)

        return BoletimParaProfessorSchema(
            aluno=aluno,
            faltas=boletim.faltas,
            nota=boletim.nota,
            materia=boletim.materia,
        )

    def listar_boletim_por_materia(
        self, id_materia: int
    ) -> list[BoletimParaProfessorSchema] | None:
        boletimDAO = BoletimDAO()
        boletins = boletimDAO.buscar_boletim_por_materia(id_materia)

        if boletins is None:
            return None

        resultado = []
        for boletim in boletins:
            aluno = UsuarioControle().listar_info_aluno(boletim.id_usuario)
            materia = MateriaControle().listar_materia(boletim.id_materia)

            boletimSchema = {
                "aluno": aluno,
                "materia": materia,
                "nota": boletim.nota,
                "faltas": boletim.faltas,
            }

            resultado.append(BoletimParaProfessorSchema(**boletimSchema))

        return resultado
