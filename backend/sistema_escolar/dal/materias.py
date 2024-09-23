from sistema_escolar.modelos.materia import Materia
from sistema_escolar.dal.conexao import Conexao
from sistema_escolar.dal.conexao import TipoRetorno
from datetime import datetime

class MateriaDAO():
    def listar_todas_materias(self) -> list[Materia]:
        con = Conexao()
        res = con.fetch_query("SELECT * FROM materia", TipoRetorno.FETCHALL)
        resultado: list[Materia] = []

        for row in res:

            print(datetime.now().date())
            print(str(row["data_inicio"]))
            # print(datetime.strptime(str(row["data_inicio"]), "%y-%m-%d %H:%M:%S").date())

            materia = {
                "id_materia" : row["id_materia"],
                "id_professor" : row["id_professor"],
                "nome" : row["nome"],
                "data_inicio" : datetime.now().date(),
                "data_fim" : datetime.now().date()
            }

            resultado.append(Materia(**materia))
            
        return resultado
