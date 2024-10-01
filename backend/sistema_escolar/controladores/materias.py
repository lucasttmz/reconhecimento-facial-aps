from datetime import datetime, timedelta
from random import randint

from sistema_escolar.modelos.materia import MateriaSchema, MateriaPublicSchema
from sistema_escolar.modelos.usuario import TipoUsuario, UsuarioSchema
from sistema_escolar.modelos.genericos import MensagemSchema
from sistema_escolar.dal.materias import MateriaDAO
from sistema_escolar.controladores.usuarios import UsuarioControle


class MateriaControle():
    def listar_todas_materias(self) -> list[MateriaSchema]:
        resultado: list[MateriaSchema] = []

        materiaDAO = MateriaDAO()
        materias = materiaDAO.listar_todas_materias()
        
        for materia in materias:

            professor = UsuarioControle().listar_info_professor(materia.id_professor)
            #alunos = BoletimControle().listar_alunos_por_materia(materia.id_materia)

            materiaSchema = {
                "nome": materia.nome,
                "professor": professor,
                "data_inicio": materia.data_inicio,
                "data_fim": materia.data_fim,
                "alunos": []
            }

            resultado.append(MateriaSchema(**materiaSchema))

        return resultado
    
    def listar_materia(self, id_materia: int) -> MateriaSchema:
        materiaDAO = MateriaDAO()
        materia = materiaDAO.buscar_materia_id(id_materia)
        professor = UsuarioControle().listar_info_professor(materia.id_professor)

        materiaSchema = {
            "nome": materia.nome,
            "professor": professor,
            "data_inicio": materia.data_inicio,
            "data_fim": materia.data_fim,
            "alunos": []
        }

        return MateriaSchema(**materiaSchema)
    
    # TODO
    # Materia
    # Pesquisar Materia por ID (id_materia) -> Materia
    # Criar Materia (MateriaSchema) -> id_materia
    # Atualizar Materia (MateriaSchema) -> id_materia
    # Apagar Materia (id_materia) -> None
    # lucas — Hoje às 18:34

    def criar_nova_materia(self, materia: MateriaSchema) -> int:
        materiaDAO = MateriaDAO()
        return materiaDAO.cadastrar_materia(materia)

    def buscar_materia_por_id(self, id: int) -> MateriaSchema:
        pass
    
    def atualizar_materia(self, id: int, materia_atualizada: MateriaSchema) -> MateriaSchema:
        # TODO: Lógica de atualizar matéria
        pass
    
    def deletar_materia(self, id: int) -> None:
        pass

    def atualizar_nota_e_faltas(self, id_materia: int, id_aluno: int, nota: float | None, faltas: float | None) -> MensagemSchema:
        # TODO: Lógica de atualizar a nota/faltas
        return MensagemSchema(mensagem="Nota e faltas atualizadas com sucesso!")