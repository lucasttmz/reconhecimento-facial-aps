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