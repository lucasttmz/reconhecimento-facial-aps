from sistema_escolar.modelos.usuario import Usuario, UsuarioSchema
from sistema_escolar.dal.conexao import Conexao
from sistema_escolar.dal.conexao import TipoRetorno


class UsuarioDAO:
    def buscar_usuario_por_id(self, id: int) -> Usuario | None:
        con = Conexao()
        res = con.fetch_query(
            f"SELECT * FROM usuario WHERE id_usuario = {id}", TipoRetorno.FETCHONE
        )

        if res is None or isinstance(res, list):
            return None

        usuario = {
            "id_usuario": res["id_usuario"],
            "codigo": res["codigo"],
            "nome": res["nome"],
            "tipo": res["tipo"],
        }

        return Usuario(**usuario)

    def buscar_professor_por_id(self, id: int) -> Usuario | None:
        con = Conexao()
        res = con.fetch_query(
            f"SELECT * FROM usuario WHERE id_usuario = {id} AND tipo = 2",
            TipoRetorno.FETCHONE,
        )

        if not res or isinstance(res, list):
            return None

        usuario = {
            "id_usuario": res["id_usuario"],
            "codigo": res["codigo"],
            "nome": res["nome"],
            "tipo": res["tipo"],
        }

        return Usuario(**usuario)

    def buscar_aluno_por_id(self, id: int) -> Usuario | None:
        con = Conexao()
        res = con.fetch_query(
            f"SELECT * FROM usuario WHERE id_usuario = {id} AND tipo = 1",
            TipoRetorno.FETCHONE,
        )

        if not res or isinstance(res, list):
            return None

        usuario = {
            "id_usuario": res["id_usuario"],
            "codigo": res["codigo"],
            "nome": res["nome"],
            "tipo": res["tipo"],
        }

        return Usuario(**usuario)

    def todos_os_professores(self) -> list[Usuario] | None:
        con = Conexao()
        res = con.fetch_query(
            "SELECT * FROM usuario WHERE tipo = 2", TipoRetorno.FETCHALL
        )

        if res is None:
            return None

        resultado: list[Usuario] = []
        for row in res:
            professor = {
                "id_usuario": row["id_usuario"],
                "codigo": row["codigo"],
                "nome": row["nome"],
                "tipo": row["tipo"],
            }
            resultado.append(Usuario(**professor))

        return resultado

    def todos_os_alunos(self) -> list[Usuario] | None:
        con = Conexao()
        res = con.fetch_query(
            "SELECT * FROM usuario WHERE tipo = 1", TipoRetorno.FETCHALL
        )

        if res is None:
            return None

        resultado: list[Usuario] = []
        for row in res:
            aluno = {
                "id_usuario": row["id_usuario"],
                "codigo": row["codigo"],
                "nome": row["nome"],
                "tipo": row["tipo"],
            }
            resultado.append(Usuario(**aluno))

        return resultado

    def sequencia_usuario(self) -> int:
        con = Conexao()
        res = con.fetch_query(
            "SELECT MAX(id_usuario) AS novo_id FROM usuario", TipoRetorno.FETCHONE
        )

        return int(res.get("novo_id", 0))  # type: ignore

    def criar_usuario(self, usuario: UsuarioSchema) -> int:
        con = Conexao()
        query: str = f"""
                        INSERT INTO usuario
                        VALUES (
                            {usuario.id_usuario}, 
                            '{usuario.codigo}',
                            '{usuario.nome}',
                            {usuario.tipo}
                        )
                    """
        con.dml_query(query)

        return usuario.id_usuario
    
    def atualizar_tipo_usuario(self, id_usuario: int, tipo: int) -> int:
        con = Conexao()
        query = f"""
            UPDATE usuario
            SET 
                tipo = {tipo}
            WHERE id_usuario = {id_usuario}
        """

        if not con.dml_query(query):
            return 0

        return id_usuario
