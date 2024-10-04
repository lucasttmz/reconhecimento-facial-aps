from datetime import datetime, timedelta
from random import randint

from sistema_escolar.modelos.materia import MateriaSchema, CriarAtualizarMateriaSchema, MateriaPublicSchema
from sistema_escolar.modelos.usuario import TipoUsuario, UsuarioSchema
from sistema_escolar.modelos.genericos import MensagemSchema
from sistema_escolar.dal.materias import MateriaDAO
from sistema_escolar.controladores.usuarios import UsuarioControle
from fastapi import HTTPException


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

        if materia.id_materia == 0:
            raise HTTPException(404)

        professor = UsuarioControle().listar_info_professor(materia.id_professor)

        materiaSchema = {
            "nome": materia.nome,
            "professor": professor,
            "data_inicio": materia.data_inicio,
            "data_fim": materia.data_fim,
            "alunos": []
        }

        return MateriaSchema(**materiaSchema)
    
    def listar_public_materia(self, id_materia) -> MateriaPublicSchema:
        materiaDAO = MateriaDAO()
        materia = materiaDAO.buscar_materia_id(id_materia)

        if materia.id_materia == 0:
            raise HTTPException(404)

        professor = UsuarioControle().listar_info_professor(materia.id_professor)

        materia_public = {
            "nome": materia.nome,
            "professor": professor.nome,
            "data_inicio": materia.data_inicio,
            "data_fim": materia.data_fim
        }

        return MateriaPublicSchema(**materia_public)
    
    # TODO
    # Materia
    # Pesquisar Materia por ID (id_materia) -> Materia
    # Criar Materia (MateriaSchema) -> id_materia
    # Atualizar Materia (MateriaSchema) -> id_materia
    # Apagar Materia (id_materia) -> None
    # lucas — Hoje às 18:34

    def criar_nova_materia(self, materia: CriarAtualizarMateriaSchema) -> MensagemSchema:
        materiaDAO = MateriaDAO()
        if (novo_id := materiaDAO.criar_materia(materia)) == 0:
            raise HTTPException(404)
        
        return MensagemSchema(mensagem=f"Deu certo! {novo_id}")
    
    def atualizar_materia(self, id_materia: int, materia_atualizada: CriarAtualizarMateriaSchema) -> MensagemSchema:
        materiaDAO = MateriaDAO()
        if materiaDAO.atualizar_materia(id_materia, materia_atualizada) == 0:
            raise HTTPException(404)
        
        return MensagemSchema(mensagem="Deu certo! :D")
    
    def atualizar_nota_e_faltas(self, id_materia: int, id_aluno: int, nota: float | None, faltas: float | None) -> MensagemSchema:
        materiaDAO = MateriaDAO()
        if materiaDAO.atualizar_notas_faltas(id_materia, id_aluno, nota, faltas) == 0:
            raise HTTPException(404)

        return MensagemSchema(mensagem="Nota e faltas atualizadas com sucesso!")