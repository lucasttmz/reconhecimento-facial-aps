from http import HTTPStatus

from fastapi import HTTPException

from sistema_escolar.modelos.materia import (
    MateriaSchema,
    CriarAtualizarMateriaSchema,
    MateriaPublicSchema,
)
from sistema_escolar.modelos.genericos import MensagemSchema
from sistema_escolar.dal.materias import MateriaDAO
from sistema_escolar.controladores.usuarios import UsuarioControle
from sistema_escolar.modelos.usuario import UsuarioSchema


class MateriaControle:
    def listar_todas_materias(self) -> list[MateriaSchema]:
        materiaDAO = MateriaDAO()
        materias = materiaDAO.listar_todas_materias()

        return self._mapear_materia_schema(materias)
    
    def listar_todas_materias_do_professor(self, id_prof: int) -> list[MateriaSchema]:
        materiaDAO = MateriaDAO()
        materias = materiaDAO.listar_todas_materias_do_professor(id_prof)

        return self._mapear_materia_schema(materias)
    
    def listar_materia(self, id_materia: int) -> MateriaSchema:
        materiaDAO = MateriaDAO()
        materia = materiaDAO.buscar_materia_id(id_materia)

        return self._mapear_materia_schema([materia])[0]
    
    def listar_materia_do_professor(self, id_materia: int, id_prof) -> MateriaSchema:
        materiaDAO = MateriaDAO()
        materia = materiaDAO.buscar_materia_professor(id_materia, id_prof)

        return self._mapear_materia_schema([materia])[0]

    def listar_public_materia(self, id_materia) -> MateriaPublicSchema:
        materiaDAO = MateriaDAO()
        materia = materiaDAO.buscar_materia_id(id_materia)

        return self._mapear_public_materia_schema(materia)
    
    def _mapear_materia_schema(self, materias: list | None) -> list:
        if materias is None:
            raise HTTPException(HTTPStatus.NOT_FOUND, "Matérias não encontradas")
        
        resultado = []
        for materia in materias:
            if materia is None or materia.id_materia == 0:
                raise HTTPException(HTTPStatus.NOT_FOUND, "Matéria não encontrada")
            
            professor = UsuarioControle().listar_info_professor(materia.id_professor)
            alunos = self.listar_alunos_em_materia(materia.id_materia)
            materia_schema = {
                "id_materia": materia.id_materia,
                "nome": materia.nome,
                "professor": professor,
                "data_inicio": materia.data_inicio,
                "data_fim": materia.data_fim,
                "alunos": alunos,
            }

            resultado.append(MateriaSchema(**materia_schema))
    
        return resultado
    
    def _mapear_public_materia_schema(self, materia) -> MateriaPublicSchema:
        if materia is None or materia.id_materia == 0:
            raise HTTPException(HTTPStatus.NOT_FOUND, "Matéria não encontrada")

        professor = UsuarioControle().listar_info_professor(materia.id_professor)
        materia_public = {
            "id_materia": materia.id_materia,
            "nome": materia.nome,
            "professor": professor.nome,
            "data_inicio": materia.data_inicio,
            "data_fim": materia.data_fim,
        }

        return MateriaPublicSchema(**materia_public)
    
    def listar_alunos_em_materia(self, id_materia: int) -> list[UsuarioSchema] | None:
        controle = UsuarioControle()
        materiaDAO = MateriaDAO()
        alunos = materiaDAO.buscar_alunos_em_materia(id_materia)

        if alunos is None:
            return []

        return [controle._mapear_usuario_schema(aluno) for aluno in alunos]

    def criar_materia(
            self, materia: CriarAtualizarMateriaSchema, boletim_controle
    ) -> MensagemSchema:
        materiaDAO = MateriaDAO()
        id_materia = materiaDAO.criar_materia(materia.codigo_professor, materia)
        if not id_materia:
            raise HTTPException(
                HTTPStatus.NOT_FOUND, detail="Não foi possível criar a matéria"
            )
        
        sucesso = boletim_controle.adicionar_boletins(materia.codigo_alunos, id_materia)
        if not sucesso:
            raise HTTPException(
                HTTPStatus.NOT_FOUND, "Não foi possível adicionar os alunos a matéria"
            )

        return MensagemSchema(mensagem=f"Matéria {materia.nome} criada com sucesso!")

    def atualizar_materia(
        self, id_materia: int, materia: CriarAtualizarMateriaSchema, boletim_controle
    ) -> MensagemSchema:
        materiaDAO = MateriaDAO()
        sucesso = materiaDAO.atualizar_materia(
            id_materia, materia.codigo_professor, materia
        )
        if not sucesso:
            raise HTTPException(
                HTTPStatus.NOT_FOUND, "Não foi possível atualizar a matéria"
            )
        
        sucesso = boletim_controle.adicionar_e_remover_boletins(
            materia.codigo_alunos, id_materia
        )
        if not sucesso:
            raise HTTPException(
                HTTPStatus.NOT_FOUND, "Não foi possível adicionar os alunos a matéria"
            )

        return MensagemSchema(
            mensagem=f"Matéria {materia.nome} atualizada com sucesso!"
        )

    def atualizar_nota_e_faltas(
        self, 
        id_materia: int, 
        id_aluno: int,
        nota: float | None, 
        faltas: float | None
    ) -> MensagemSchema:
        materiaDAO = MateriaDAO()
        if materiaDAO.atualizar_notas_faltas(id_materia, id_aluno, nota, faltas) == 0:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        return MensagemSchema(mensagem="Nota e faltas atualizadas com sucesso!")

    def professor_ensina_materia(self, id_prof: int, id_materia: int) -> bool:
       materiaDAO = MateriaDAO()
       materia = materiaDAO.buscar_materia_id(id_materia)
       if materia is None:
           return False
       
       return materia.id_professor == id_prof
