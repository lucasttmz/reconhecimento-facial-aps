from datetime import datetime, timedelta
from random import randint

from sistema_escolar.modelos.boletim import BoletimParaAlunoSchema, BoletimParaProfessorSchema, Boletim
from sistema_escolar.modelos.usuario import TipoUsuario, UsuarioSchema
from sistema_escolar.dal.boletim import BoletimDAO
from fastapi import HTTPException
# from sistema_escolar.controladores.usuarios import UsuarioControle
from sistema_escolar.controladores.materias import MateriaControle


class BoletimControle():
    def listar_boletim_aluno(self, id_aluno: int) -> list[BoletimParaAlunoSchema]:
        boletimDAO = BoletimDAO()
        boletins = boletimDAO.buscar_todos_boletins_aluno(id_aluno)

        resultado: list[BoletimParaAlunoSchema] = []
        for boletim in boletins:
            materia = MateriaControle().listar_public_materia(boletim.id_materia)

            boletim_schema = {
                "materia": materia,
                "nota": boletim.nota,
                "faltas": boletim.faltas
            }
            resultado.append(BoletimParaAlunoSchema(**boletim_schema))

        return resultado
    
    def listar_boletim_aluno_em_materia(self, id_aluno: int, id_materia) -> BoletimParaAlunoSchema:
        boletimDAO = BoletimDAO()
        if (boletim := boletimDAO.buscar_boletim_do_aluno(id_aluno, id_materia)) is None:
            raise HTTPException(404)

        materia = MateriaControle().listar_public_materia(boletim.id_materia)

        boletim_schema = {
            "materia": materia,
            "nota": boletim.nota,
            "faltas": boletim.faltas
        }

        return BoletimParaAlunoSchema(**boletim_schema)
    
    def listar_boletim_para_professores(self, id_aluno: int, id_materia: int) -> BoletimParaProfessorSchema:
        aluno = UsuarioSchema(codigo=f"AL_{id_aluno}", nome=f"Nome Aluno{id_aluno}", tipo=TipoUsuario.ALUNO)
        boletim = self.listar_boletim_aluno_em_materia(id_aluno, id_materia)

        return BoletimParaProfessorSchema(aluno=aluno, faltas=boletim.faltas, nota=boletim.faltas, materia=boletim.materia)
        

    # DPS EU VEJO ISSO
    # def listar_boletim_por_materia(self, id_materia: int) -> None:
    #     boletimDAO = BoletimDAO()
    #     boletins: list[Boletim] = boletimDAO.buscar_boletim_por_materia(id_materia)

    #     resultado: list[BoletimParaProfessorSchema] = []
    #     for boletim in boletins:
    #         aluno = UsuarioControle().listar_info_aluno(boletim.id_usuario)
    #         materia = MateriaControle().buscar_materia_por_id(boletim.id_materia)

    #         boletimSchema = {
    #             "aluno" : aluno,
    #             "materia": materia,
    #             "nota": boletim.nota,
    #             "faltas": boletim.faltas
    #         }

    #         resultado.append(BoletimParaProfessorSchema(**boletimSchema))

    #     return resultado

    # Boletim
    # Pesquisar Materias por Aluno (id_aluno) -> list[Materia]
    # Pesquisar TODOS Alunos por materia (id_materia) -> list[Usuário]
    # Pesquisar Boletim por materia (id_aluno, id_materia) -> Boletim
    # Pesquisar TODOS Boletins por aluno (id_aluno) -> list[Boletim]
    # Atualizar Boletim (id_boletim, AtualizarBoletimSchema) -> None