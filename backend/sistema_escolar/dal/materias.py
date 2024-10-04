from sistema_escolar.modelos.materia import Materia, CriarAtualizarMateriaSchema
from sistema_escolar.dal.conexao import Conexao, TipoRetorno
from datetime import datetime

class MateriaDAO():
    def sequencia_materia(self) -> int:
        con = Conexao()
        res = con.fetch_query("SELECT MAX(id_materia) AS novo_id FROM materia", TipoRetorno.FETCHONE)

        return int(res["novo_id"])

    def listar_todas_materias(self) -> list[Materia]:
        con = Conexao()
        res = con.fetch_query("SELECT * FROM materia", TipoRetorno.FETCHALL)
        resultado: list[Materia] = []

        for row in res:
            materia = {
                "id_materia" : row.get("id_materia", 0),
                "id_professor" : row.get("id_professor", 0),
                "nome" : row.get("nome", None),
                "data_inicio" : datetime.fromisoformat(row.get("data_inicio", "0000-00-00 00:00:00")).date(),
                "data_fim" : datetime.fromisoformat(row.get("data_fim", "0000-00-00 00:00:00")).date()
            }

            resultado.append(Materia(**materia))
            
        return resultado
    
    def buscar_materia_id(self, id_materia) -> Materia:
        con = Conexao()
        row = con.fetch_query(f"SELECT * FROM materia WHERE id_materia = {id_materia}", TipoRetorno.FETCHONE)

        materia = {
            "id_materia" : row.get("id_materia", 0),
            "id_professor" : row.get("id_professor", 0),
            "nome" : row.get("nome", ""),
            "data_inicio" : datetime.fromisoformat(row.get("data_inicio", "1970-01-01 00:00:00")).date(),
            "data_fim" : datetime.fromisoformat(row.get("data_fim", "1970-01-01 00:00:00")).date()
        }

        return Materia(**materia)

    def criar_materia(self, nova_materia: CriarAtualizarMateriaSchema) -> int:
        seq: int = self.sequencia_materia() + 1
        con = Conexao()
        query: str = f"""
                        INSERT INTO materia 
                        VALUES (
                            {seq}, 
                            '{nova_materia.nome}',
                            {int(nova_materia.codigo_professor)},
                            '{nova_materia.data_inicio}',
                            '{nova_materia.data_fim}'
                        )
                    """
        con.dml_query(query)

        return seq
    
    def atualizar_materia(self, id_materia: int, materia: CriarAtualizarMateriaSchema) -> int:
        con = Conexao()

        query = f"""
            UPDATE materia 
            SET 
                id_professor = {int(materia.codigo_professor)},
                nome = '{materia.nome}',
                data_inicio = '{materia.data_inicio}',
                data_fim = '{materia.data_fim}'
            WHERE id_materia = {id_materia}
        """

        if not con.dml_query(query):
            return 0
        
        return id_materia

    def atualizar_notas_faltas(self, id_materia: int, id_aluno: int, nota: float | None, faltas: float | None) -> int:
        con = Conexao()

        cursando_materia = con.fetch_query(f"SELECT 1 FROM boletim WHERE id_usuario = {id_aluno} AND id_materia = {id_materia}", TipoRetorno.FETCHONE)
        if not cursando_materia:
            return 0

        query = f"""
            UPDATE boletim
            SET 
                nota = {nota},
                faltas = {faltas}
            WHERE
                id_materia = {id_materia}
            AND id_usuario = {id_aluno}
        """
        
        if not con.dml_query(query):
            return 0

        return id_aluno