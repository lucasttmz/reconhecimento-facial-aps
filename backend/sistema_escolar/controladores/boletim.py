from datetime import datetime, timedelta
from random import randint

from sistema_escolar.modelos.boletim import BoletimParaAlunoSchema, BoletimParaProfessorSchema
from sistema_escolar.modelos.usuario import TipoUsuario, UsuarioSchema


class BoletimControle():
    def listar_boletim_aluno(self, id_aluno: int) -> list[BoletimParaAlunoSchema]:
        id_materias_aluno = (1, 2, 3)

        return [self.listar_boletim_aluno_em_materia(id_aluno, materia) for materia in id_materias_aluno]
    
    def listar_boletim_aluno_em_materia(self, id_aluno: int, id_materia) -> BoletimParaAlunoSchema:
        materia = {
            "materia": {
                "nome": f"Nome Matéria {id_materia}",
                "professor": f"Prof. Matéria {id_materia}",
                "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
                "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
            },
            "nota": randint(0, 10),
            "faltas": randint(0, 5),
        }

        return BoletimParaAlunoSchema(**materia)
    
    def listar_boletim_para_professores(self, id_aluno: int, id_materia: int) -> BoletimParaProfessorSchema:
        aluno = UsuarioSchema(codigo=f"AL_{id_aluno}", nome=f"Nome Aluno{id_aluno}", tipo=TipoUsuario.ALUNO)
        boletim = self.listar_boletim_aluno_em_materia(id_aluno, id_materia)

        return BoletimParaProfessorSchema(aluno=aluno, faltas=boletim.faltas, nota=boletim.faltas, materia=boletim.materia)

    # TODO
    # Boletim
    # Pesquisar Materias por Aluno (id_aluno) -> list[Materia]
    # Pesquisar TODOS Alunos por materia (id_materia) -> list[Usuário]
    # Pesquisar Boletim por materia (id_aluno, id_materia) -> Boletim
    # Pesquisar TODOS Boletins por aluno (id_aluno) -> list[Boletim]
    # Atualizar Boletim (id_boletim, AtualizarBoletimSchema) -> None