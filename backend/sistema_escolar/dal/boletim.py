from sistema_escolar.modelos.boletim import Boletim
from sistema_escolar.modelos.usuario import Usuario
from sistema_escolar.dal.conexao import Conexao, TipoRetorno


class BoletimDAO:
    def buscar_todos_boletins_aluno(self, id_aluno: int) -> list[Boletim] | None:
        con = Conexao()
        res = con.fetch_query(
            f"SELECT * FROM boletim WHERE id_usuario = {id_aluno}", TipoRetorno.FETCHALL
        )

        if res is None:
            return None

        resultado = []
        for row in res:
            boletim = {
                "id_boletim": row.get("id_boletim", 0),
                "id_usuario": row.get("id_usuario", 0),
                "id_materia": row.get("id_materia", 0),
                "nota": row.get("nota", None),
                "faltas": row.get("faltas", 0),
            }

            resultado.append(Boletim(**boletim))

        return resultado

    def buscar_boletim_do_aluno(self, id_aluno: int, id_materia: int) -> Boletim | None:
        con = Conexao()
        row = con.fetch_query(
            f"SELECT * FROM boletim WHERE id_usuario = {id_aluno} AND id_materia = {id_materia}",
            TipoRetorno.FETCHONE,
        )

        if row is None or isinstance(row, list):
            return None

        boletim = {
            "id_boletim": row.get("id_boletim", 0),
            "id_usuario": row.get("id_usuario", 0),
            "id_materia": row.get("id_materia", 0),
            "nota": row.get("nota", None),
            "faltas": row.get("faltas", 0),
        }
        return Boletim(**boletim)

    def buscar_boletim_por_materia(self, id_materia: int) -> list[Boletim] | None:
        con = Conexao()
        res = con.fetch_query(
            f"SELECT * FROM boletim WHERE id_materia = {id_materia}",
            TipoRetorno.FETCHALL,
        )

        if res is None:
            return None

        resultado = []
        for row in res:
            boletim = {
                "id_boletim": row["id_boletim"],
                "id_usuario": row["id_usuario"],
                "id_materia": row["id_materia"],
                "nota": row["nota"],
                "faltas": row["faltas"],
            }

            resultado.append(Boletim(**boletim))

        return resultado
