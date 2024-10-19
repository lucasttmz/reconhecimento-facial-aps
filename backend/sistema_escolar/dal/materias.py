from sistema_escolar.modelos.materia import (
    Materia,
    CriarAtualizarMateriaSchema,
)
from sistema_escolar.modelos.usuario import Usuario
from sistema_escolar.dal.conexao import Conexao, TipoRetorno
from datetime import datetime


class MateriaDAO:
    def sequencia_materia(self) -> int:
        con = Conexao()
        res = con.fetch_query(
            "SELECT MAX(id_materia) AS novo_id FROM materia", [], TipoRetorno.FETCHONE
        )

        return int(res.get("novo_id", 0))  # type: ignore

    def listar_todas_materias(self) -> list[Materia] | None:
        con = Conexao()
        res = con.fetch_query("SELECT * FROM materia", [], TipoRetorno.FETCHALL)

        if res is None:
            return None

        return [self._mapear_materia(linha) for linha in res]
    
    def listar_todas_materias_do_professor(self, id_prof: int) -> list[Materia] | None:
        con = Conexao()
        query = "SELECT * FROM materia WHERE id_professor=?"
        res = con.fetch_query(query, [id_prof], TipoRetorno.FETCHALL)

        if res is None:
            return None

        return [self._mapear_materia(linha) for linha in res]

    def buscar_materia_id(self, id_materia: int) -> Materia | None:
        con = Conexao()
        query = "SELECT * FROM materia WHERE id_materia = ?"
        res = con.fetch_query(query, [id_materia], TipoRetorno.FETCHONE)

        if res is None or isinstance(res, list):
            return None

        return self._mapear_materia(res)
    
    def buscar_materia_professor(self, id_materia: int, id_prof: int) -> Materia | None:
        con = Conexao()
        query = "SELECT * FROM materia WHERE id_materia = ? and id_professor = ?"
        res = con.fetch_query(query, [id_materia, id_prof], TipoRetorno.FETCHONE)

        if res is None or isinstance(res, list):
            return None

        return self._mapear_materia(res)
    
    def _mapear_materia(self, linha) -> Materia:
        materia = {
            "id_materia": linha.get("id_materia", 0),
            "id_professor": linha.get("id_professor", 0),
            "nome": linha.get("nome", ""),
            "data_inicio": datetime.fromisoformat(
                linha.get("data_inicio", "1970-01-01 00:00:00")
            ).date(),
            "data_fim": datetime.fromisoformat(
                linha.get("data_fim", "1970-01-01 00:00:00")
            ).date(),
        }

        return Materia(**materia)

    
    def buscar_alunos_em_materia(self, id_materia: int) -> list[Usuario] | None:
        con = Conexao()
        query = """
            SELECT u.*
            FROM usuario u
            JOIN boletim b ON u.id_usuario = b.id_usuario
            WHERE b.id_materia = ?
        """
        res = con.fetch_query(query, [id_materia], TipoRetorno.FETCHALL)

        if res is None:
            return None
        
        resultado = []
        for row in res:
            professor = {
                "id_usuario": row["id_usuario"],
                "codigo": row["codigo"],
                "nome": row["nome"],
                "tipo": row["tipo"],
            }
            resultado.append(Usuario(**professor))

        return resultado

    def criar_materia(
        self, id_professor: int, nova_materia: CriarAtualizarMateriaSchema
    ) -> int:
        seq: int = self.sequencia_materia() + 1
        con = Conexao()
        query = "INSERT INTO materia VALUES (?, ?, ?, ?, ?)"
        params = [seq, nova_materia.nome, id_professor, nova_materia.data_inicio, nova_materia.data_fim]
        con.dml_query(query, params)

        return seq

    def atualizar_materia(
        self, id_materia: int, id_professor: int, materia: CriarAtualizarMateriaSchema
    ) -> int:
        con = Conexao()

        query = """
            UPDATE materia 
            SET 
                id_professor = ?,
                nome = ?,
                data_inicio = ?,
                data_fim = ?
            WHERE id_materia = ?
        """
        params = [id_professor, materia.nome, materia.data_inicio, materia.data_fim, id_materia]

        if not con.dml_query(query, params):
            return 0

        return id_materia

    def atualizar_notas_faltas(
        self, id_materia: int, id_aluno: int, nota: float | None, faltas: float | None
    ) -> int:
        con = Conexao()
        query = "SELECT 1 FROM boletim WHERE id_usuario = ? AND id_materia = ?"
        params = [id_aluno, id_materia]
        cursando_materia = con.fetch_query(query, params, TipoRetorno.FETCHONE)
        if not cursando_materia:
            return 0

        query = """
            UPDATE boletim
            SET 
                nota = ?,
                faltas = ?
            WHERE
                id_materia = ?
            AND id_usuario = ?
        """
        params = [nota, faltas, id_materia, id_aluno]

        if not con.dml_query(query, params):
            return 0

        return id_aluno
