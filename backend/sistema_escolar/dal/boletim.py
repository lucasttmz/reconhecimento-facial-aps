from sistema_escolar.modelos.boletim import Boletim
from sistema_escolar.dal.conexao import Conexao, TipoRetorno


class BoletimDAO:
    def buscar_todos_boletins_aluno(self, id_aluno: int) -> list[Boletim] | None:
        con = Conexao()
        query = "SELECT * FROM boletim WHERE id_usuario = ?"
        res = con.fetch_query(query, [id_aluno], TipoRetorno.FETCHALL)

        if res is None:
            return None

        return [self._mapear_boletim(linha) for linha in res]

    def buscar_boletim_do_aluno(self, id_aluno: int, id_materia: int) -> Boletim | None:
        con = Conexao()
        query = "SELECT * FROM boletim WHERE id_usuario = ? AND id_materia = ?"
        res = con.fetch_query(query, [id_aluno, id_materia], TipoRetorno.FETCHONE)

        if res is None or isinstance(res, list):
            return None

        return self._mapear_boletim(res)

    def buscar_boletim_por_materia(self, id_materia: int) -> list[Boletim] | None:
        con = Conexao()
        query = "SELECT * FROM boletim WHERE id_materia = ?"
        res = con.fetch_query(query, [id_materia], TipoRetorno.FETCHALL)

        if res is None:
            return None

        return [self._mapear_boletim(linha) for linha in res]
    
    def _mapear_boletim(self, linha) -> Boletim:
        boletim = {
            "id_boletim": linha["id_boletim"],
            "id_usuario": linha["id_usuario"],
            "id_materia": linha["id_materia"],
            "nota": linha["nota"],
            "faltas": linha["faltas"],
        }

        return Boletim(**boletim)

    def criar_boletim_para_aluno(self, id_aluno: int,  id_materia: int):
        con = Conexao()
        query = f"INSERT INTO boletim VALUES (NULL, ?, ?, NULL, 0)"
        return con.dml_query(query, [id_aluno, id_materia])
    
    def remover_boletim_para_aluno(self, id_aluno: int,  id_materia: int):
        con = Conexao()
        query = f"DELETE FROM boletim WHERE id_usuario=? AND id_materia=?"
        return con.dml_query(query, [id_aluno, id_materia])
