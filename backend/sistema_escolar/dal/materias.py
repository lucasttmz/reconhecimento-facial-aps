from sistema_escolar.modelos.materia import Materia, CriarAtualizarMateriaSchema
from sistema_escolar.dal.conexao import Conexao, TipoRetorno
from datetime import datetime

class MateriaDAO():
    def sequencia_materia() -> int:
        con = Conexao()
        res = con.fetch_query("SELECT MAX(id_materia) AS novo_id FROM materia")

        return int(res["novo_id"])

    def listar_todas_materias(self) -> list[Materia]:
        con = Conexao()
        res = con.fetch_query("SELECT * FROM materia", TipoRetorno.FETCHALL)
        resultado: list[Materia] = []

        for row in res:

            materia = {
                "id_materia" : row["id_materia"],
                "id_professor" : row["id_professor"],
                "nome" : row["nome"],
                "data_inicio" : datetime.fromisoformat(row["data_inicio"]).date(),
                "data_fim" : datetime.fromisoformat(row["data_fim"]).date()
            }

            resultado.append(Materia(**materia))
            
        return resultado
    
    def buscar_materia_id(self, id_materia) -> Materia:
        con = Conexao()
        row = con.fetch_query(f"SELECT * FROM materia WHERE id_materia = {id_materia}", TipoRetorno.FETCHONE)

        materia = {
            "id_materia" : int(row["id_materia"]),
            "id_professor" : int(row["id_professor"]),
            "nome" : row["nome"],
            "data_inicio" : datetime.fromisoformat(row["data_inicio"]).date(),
            "data_fim" : datetime.fromisoformat(row["data_fim"]).date()
        }

        return Materia(**materia)

    def criar_materia(self, NovaMateria: CriarAtualizarMateriaSchema) -> int:
        seq: int = self.sequencia_materia()
        con = Conexao()
        query: str = f"""
                        INSERT INTO materia 
                        VALUES (
                            {seq}, 
                            {NovaMateria.codigo_professor},
                            '{NovaMateria.nome}',
                            '{NovaMateria.data_inicio}',
                            '{NovaMateria.data_fim}'
                        )
                    """
        sucesso = con.dml_query(query)
        
        if not sucesso:
            seq = 0

        return seq

