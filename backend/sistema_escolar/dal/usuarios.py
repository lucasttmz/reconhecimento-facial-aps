from sistema_escolar.modelos.usuario import Usuario
from sistema_escolar.dal.conexao import Conexao
from sistema_escolar.dal.conexao import TipoRetorno

class UsuarioDAO():
    def buscar_usuario_por_id(self, id: int) -> Usuario:
        con = Conexao()
        res = con.fetch_query(f"SELECT * FROM usuario WHERE id_usuario = {id}", TipoRetorno.FETCHONE)
        
        usuario = {
            "id_usuario": res["id_usuario"],
            "codigo": res["codigo"],
            "nome": res["nome"],
            "tipo": res["tipo"]
        }

        return Usuario(**usuario)
    
    def buscar_professor_por_id(self, id: int) -> Usuario:
        con = Conexao()
        row = con.fetch_query(f"SELECT * FROM usuario WHERE id_usuario = {id} AND tipo = 2", TipoRetorno.FETCHONE)
        
        usuario = {
            "id_usuario": row.get("id_usuario", 0),
            "codigo": row["codigo"],
            "nome": row["nome"],
            "tipo": row["tipo"]
        }

        return Usuario(**usuario)
    
    def buscar_aluno_por_id(self, id: int) -> Usuario:
        con = Conexao()
        res = con.fetch_query(f"SELECT * FROM usuario WHERE id_usuario = {id} AND tipo = 1", TipoRetorno.FETCHONE)
        
        usuario = {
            "id_usuario": res["id_usuario"],
            "codigo": res["codigo"],
            "nome": res["nome"],
            "tipo": res["tipo"]
        }

        return Usuario(**usuario)
    
    def todos_os_professores(self) -> list[Usuario]:
        con = Conexao()
        res = con.fetch_query(f"SELECT * FROM usuario WHERE tipo = 2", TipoRetorno.FETCHALL)

        resultado: list[Usuario] = []
        for row in res:
            professor = {
                "id_usuario": row["id_usuario"],
                "codigo": row["codigo"],
                "nome": row["nome"],
                "tipo": row["tipo"]
            }
            resultado.append(Usuario(**professor))

        return resultado

    def todos_os_alunos(self) -> list[Usuario]:
        con = Conexao()
        res = con.fetch_query(f"SELECT * FROM usuario WHERE tipo = 1", TipoRetorno.FETCHALL)

        resultado: list[Usuario] = []
        for row in res:
            aluno = {
                "id_usuario": row["id_usuario"],
                "codigo": row["codigo"],
                "nome": row["nome"],
                "tipo": row["tipo"]
            }
            resultado.append(Usuario(**aluno))

        return resultado