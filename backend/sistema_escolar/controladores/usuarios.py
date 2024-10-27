from http import HTTPStatus
import uuid

from fastapi import HTTPException

from sistema_escolar.modelos.autenticacao import UsuarioRegistradoSchema
from sistema_escolar.modelos.usuario import UsuarioSchema, AtualizarUsuarioSchema
from sistema_escolar.modelos.genericos import MensagemSchema
from sistema_escolar.dal.usuarios import UsuarioDAO


class UsuarioControle:
    def listar_todos_alunos(self) -> list[UsuarioSchema]:
        """Lista todos os alunos"""

        usuarioDAO = UsuarioDAO()
        alunos = usuarioDAO.todos_os_alunos()
        # Para o caso de não ter nenhum aluno cadastrado
        if alunos is None:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        return [self._mapear_usuario_schema(aluno) for aluno in alunos]

    def listar_info_aluno(self, id_aluno: int) -> UsuarioSchema:
        """Lista as informações de um aluno"""

        usuarioDAO = UsuarioDAO()
        aluno = usuarioDAO.buscar_aluno_por_id(id_aluno)

        return self._mapear_usuario_schema(aluno)

    def listar_todos_professores(self) -> list[UsuarioSchema]:
        """Lista todos os professores"""

        usuarioDAO = UsuarioDAO()
        professores = usuarioDAO.todos_os_professores()
        # Para o caso de não ter nenhum professor cadastrado
        if professores is None:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        return [self._mapear_usuario_schema(prof) for prof in professores]

    def listar_info_professor(self, id_professor: int) -> UsuarioSchema:
        """Lista as informações de um professor"""

        usuarioDAO = UsuarioDAO()
        professor = usuarioDAO.buscar_professor_por_id(id_professor)

        return self._mapear_usuario_schema(professor)

    def listar_info_usuario(self, id_usuario: int) -> UsuarioSchema:
        """Lista as informações de um usuário, independente de cargo"""

        usuarioDAO = UsuarioDAO()
        usuario = usuarioDAO.buscar_usuario_por_id(id_usuario)

        return self._mapear_usuario_schema(usuario)

    def _mapear_usuario_schema(self, usuario) -> UsuarioSchema:
        """Mapeia Usuario -> UsuarioSchema p/ retornar na API"""

        if usuario is None:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        usuarioSchema = {
            "id_usuario": usuario.id_usuario,
            "codigo": usuario.codigo,
            "nome": usuario.nome,
            "tipo": usuario.tipo,
        }

        return UsuarioSchema(**usuarioSchema)

    def listar_id_usuario_por_codigo(self, codigo: str) -> int:
        """Retorna o ID do usuário usando seu código"""

        usuarioDAO = UsuarioDAO()
        usuario = usuarioDAO.buscar_usuario_por_codigo(codigo)
        # Se o código não corresponder a nenhum usuário, retorna 0
        if usuario is None:
            return 0

        return usuario.id_usuario

    def sequencia_usuario(self) -> int:
        """Retorna o próximo ID de usuário para treinar o modelo"""

        usuarioDAO = UsuarioDAO()
        return usuarioDAO.sequencia_usuario()

    def gerar_codigo_usuario(self) -> str:
        """Gera o código de usuário"""

        return str(uuid.uuid4()).upper()[:8]

    def criar_usuario(
        self, id_usuario: int, nome_usuario: str
    ) -> UsuarioRegistradoSchema:
        """Cria um novo usuário"""

        # Primeiro usuário cadastrado é diretor, os demais são alunos
        cargo = 1 if id_usuario > 1 else 3
        codigo = self.gerar_codigo_usuario()
        dados = {
            "id_usuario": id_usuario,
            "nome": nome_usuario,
            "codigo": codigo,
            "tipo": cargo,
        }
        usuarioDAO = UsuarioDAO()
        sucesso = usuarioDAO.criar_usuario(UsuarioSchema(**dados))
        if not sucesso:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        return UsuarioRegistradoSchema(codigo=codigo, nome=nome_usuario)

    def atualizar_usuario(
        self, id_usuario: int, usuario_atualizado: AtualizarUsuarioSchema
    ) -> MensagemSchema:
        """Atualiza o cargo do usuário"""

        usuarioDAO = UsuarioDAO()
        sucesso = usuarioDAO.atualizar_tipo_usuario(id_usuario, usuario_atualizado.tipo)
        # Para o caso de tentar atualizar um usuário que não existe
        if not sucesso:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        return MensagemSchema(mensagem="Cargo atualizado com sucesso!")
