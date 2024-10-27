from sistema_escolar.dal.conexao import Conexao, TipoRetorno
from sistema_escolar.modelos.usuario import Usuario, UsuarioSchema, TipoUsuario


class UsuarioDAO:
    def buscar_usuario_por_id(self, id: int) -> Usuario | None:
        """Busca um usuário utilizando seu id"""

        con = Conexao()
        query = "SELECT * FROM usuario WHERE id_usuario = ?"
        res = con.fetch_query(query, [id], TipoRetorno.FETCHONE)
        if res is None or isinstance(res, list):
            return None

        return self._mapear_usuario(res)

    def buscar_diretor_por_id(self, id: int) -> Usuario | None:
        """Busca um diretor utilizando seu id"""

        return self.buscar_usuario_por_id_e_tipo(id, TipoUsuario.DIRETOR)

    def buscar_professor_por_id(self, id: int) -> Usuario | None:
        """Busca um professor utilizando seu id"""

        return self.buscar_usuario_por_id_e_tipo(id, TipoUsuario.PROFESSOR)

    def buscar_aluno_por_id(self, id: int) -> Usuario | None:
        """Busca um aluno utilizando seu id"""

        return self.buscar_usuario_por_id_e_tipo(id, TipoUsuario.ALUNO)

    def buscar_usuario_por_id_e_tipo(self, id: int, tipo: int) -> Usuario | None:
        """Busca um usuário pelo seu id e tipo (chamado por outros métodos)"""

        con = Conexao()
        query = "SELECT * FROM usuario WHERE id_usuario = ? AND tipo = ?"
        res = con.fetch_query(query, [id, tipo], TipoRetorno.FETCHONE)
        if not res or isinstance(res, list):
            return None

        return self._mapear_usuario(res)

    def buscar_usuario_por_codigo(self, codigo: str) -> Usuario | None:
        """Busca um usuário utilizando seu código"""

        con = Conexao()
        query = "SELECT * FROM usuario WHERE codigo = ?"
        res = con.fetch_query(query, [codigo], TipoRetorno.FETCHONE)
        if res is None or isinstance(res, list):
            return None

        return self._mapear_usuario(res)

    def todos_os_professores(self) -> list[Usuario] | None:
        """Busca todos os professores"""

        con = Conexao()
        res = con.fetch_query(
            "SELECT * FROM usuario WHERE tipo = 2", [], TipoRetorno.FETCHALL
        )
        if res is None:
            return None

        return [self._mapear_usuario(linha) for linha in res]

    def todos_os_alunos(self) -> list[Usuario] | None:
        """Busca todos os alunos"""

        con = Conexao()
        res = con.fetch_query(
            "SELECT * FROM usuario WHERE tipo = 1", [], TipoRetorno.FETCHALL
        )
        if res is None:
            return None

        return [self._mapear_usuario(linha) for linha in res]

    def _mapear_usuario(self, linha) -> Usuario:
        """Mapeia dados do banco de dados para Usuario"""

        usuario = {
            "id_usuario": linha["id_usuario"],
            "codigo": linha["codigo"],
            "nome": linha["nome"],
            "tipo": linha["tipo"],
        }

        return Usuario(**usuario)

    def sequencia_usuario(self) -> int:
        """Retorna o id máximo dos usuários (para registrar novo usuário no modelo LBPH)"""
        con = Conexao()
        res = con.fetch_query(
            "SELECT MAX(id_usuario) AS novo_id FROM usuario", [], TipoRetorno.FETCHONE
        )

        return int(res.get("novo_id", 0) or 0)  # type: ignore

    def criar_usuario(self, usuario: UsuarioSchema) -> int:
        """Cria um novo usuário no BD"""

        con = Conexao()
        query: str = "INSERT INTO usuario VALUES (?, ?, ?, ?)"
        params = [usuario.id_usuario, usuario.codigo, usuario.nome, usuario.tipo]
        con.dml_query(query, params)

        return usuario.id_usuario

    def atualizar_tipo_usuario(self, id_usuario: int, tipo: int) -> int:
        """Atualiza o tipo de um usuário"""

        con = Conexao()
        query = "UPDATE usuario SET tipo = ? WHERE id_usuario = ?"
        params = [tipo, id_usuario]
        if not con.dml_query(query, params):
            return 0

        return id_usuario
