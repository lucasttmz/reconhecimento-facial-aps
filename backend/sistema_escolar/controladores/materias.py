from sistema_escolar.modelos.materia import (
    MateriaSchema,
    CriarAtualizarMateriaSchema,
    MateriaPublicSchema,
)
from sistema_escolar.modelos.genericos import MensagemSchema
from sistema_escolar.dal.materias import MateriaDAO
from sistema_escolar.controladores.usuarios import UsuarioControle
from fastapi import HTTPException


class MateriaControle:
    def listar_todas_materias(self) -> list[MateriaSchema]:
        resultado = []
        materiaDAO = MateriaDAO()
        materias = materiaDAO.listar_todas_materias()

        if materias is None:
            raise HTTPException(404)

        for materia in materias:
            professor = UsuarioControle().listar_info_professor(materia.id_professor)

            materia_schema = {
                "nome": materia.nome,
                "professor": professor,
                "data_inicio": materia.data_inicio,
                "data_fim": materia.data_fim,
                "alunos": [],
            }

            resultado.append(MateriaSchema(**materia_schema))

        return resultado

    def listar_materia(self, id_materia: int) -> MateriaSchema:
        materiaDAO = MateriaDAO()
        materia = materiaDAO.buscar_materia_id(id_materia)

        if materia is None or materia.id_materia == 0:
            raise HTTPException(404)

        professor = UsuarioControle().listar_info_professor(materia.id_professor)

        materia_schema = {
            "nome": materia.nome,
            "professor": professor,
            "data_inicio": materia.data_inicio,
            "data_fim": materia.data_fim,
            "alunos": [],
        }

        return MateriaSchema(**materia_schema)

    def listar_public_materia(self, id_materia) -> MateriaPublicSchema:
        materiaDAO = MateriaDAO()
        materia = materiaDAO.buscar_materia_id(id_materia)

        if materia is None or materia.id_materia == 0:
            raise HTTPException(404)

        professor = UsuarioControle().listar_info_professor(materia.id_professor)

        materia_public = {
            "nome": materia.nome,
            "professor": professor.nome,
            "data_inicio": materia.data_inicio,
            "data_fim": materia.data_fim,
        }

        return MateriaPublicSchema(**materia_public)

    def criar_nova_materia(
        self, materia: CriarAtualizarMateriaSchema
    ) -> MensagemSchema:
        materiaDAO = MateriaDAO()

        # TODO: Pegar id professor pelo codigo
        id_professor = 2
        sucesso = materiaDAO.criar_materia(id_professor, materia)

        if not sucesso:
            raise HTTPException(404)

        return MensagemSchema(mensagem=f"Matéria {materia.nome} criada com sucesso!")

    def atualizar_materia(
        self, id_materia: int, materia: CriarAtualizarMateriaSchema
    ) -> MensagemSchema:
        materiaDAO = MateriaDAO()

        # TODO: Pegar id professor pelo codigo
        id_professor = 2

        sucesso = materiaDAO.atualizar_materia(id_materia, id_professor, materia)

        if not sucesso:
            raise HTTPException(404)

        return MensagemSchema(
            mensagem=f"Matéria {materia.nome} atualizada com sucesso!"
        )

    def atualizar_nota_e_faltas(
        self, id_materia: int, id_aluno: int, nota: float | None, faltas: float | None
    ) -> MensagemSchema:
        materiaDAO = MateriaDAO()
        if materiaDAO.atualizar_notas_faltas(id_materia, id_aluno, nota, faltas) == 0:
            raise HTTPException(404)

        return MensagemSchema(mensagem="Nota e faltas atualizadas com sucesso!")
