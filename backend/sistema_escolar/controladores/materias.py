from datetime import datetime, timedelta
from random import randint

from sistema_escolar.modelos.materia import MateriaSchema
from sistema_escolar.modelos.usuario import TipoUsuario
from sistema_escolar.modelos.genericos import MensagemSchema


class MateriaControle():
    def listar_todas_materias(self, id_usuario: int) -> list[MateriaSchema]:
        # TODO: Verificar se usuário é diretor ou professor
        permissao_professor = id_usuario % 2 == 0 # Simula permissão
        
        qtd_materias = 3
        if permissao_professor:
            qtd_materias -= 1
        
        return [self.listar_materia(i) for i in range(qtd_materias)]
    
    def listar_materia(self, id_materia: int) -> MateriaSchema:
        alunos = []
        if id_materia % 2:
            alunos = [
                {"codigo": "AL_LUC4S", "nome": "lucas", "tipo": TipoUsuario.ALUNO},
                {"codigo": "AL_F3L1P3", "nome": "felipe", "tipo": TipoUsuario.ALUNO},
            ]

        nomes_materias = ("Matemática", "Inglês", "Física")
        professores = ("João", "Mária", "Felipe")
        materia = {
            "nome": nomes_materias[id_materia % 3],
            "professor": {
                "codigo": f"Cod. do {professores[id_materia % 3]}",
                "nome": professores[id_materia % 3],
                "tipo": TipoUsuario.PROFESSOR,
            },
            "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
            "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
            "alunos": alunos,
        }   
        return MateriaSchema(**materia)
    
    def atualizar_nota(self, id_materia: int, id_aluno: int, nota: float) -> MensagemSchema:
        # TODO: Lógica de atualizar a nota
        return MensagemSchema(mensagem=f"Nota atualizada com sucesso: {nota}")
    
    def atualizar_qtd_faltas(self, id_materia: int, id_aluno: int, faltas: int) -> MensagemSchema:
        # TODO: Lógica de atualizar a qtd. faltas
        return MensagemSchema(mensagem=f"Falta atualizada com sucesso: {faltas}")
