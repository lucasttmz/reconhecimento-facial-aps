from sqlite3 import connect, Connection, Cursor
import re

def limpar_query(texto: str) -> str:
    query_limpa = re.sub(r"\n|\t|\r", "", str(texto))

    if query_limpa[-1] == ";":
        return query_limpa;
    else:
        return query_limpa + ";"

class Conexao():
    conn_str: str = "teste.db"
    conn: Connection

    def iniciar(self) -> Cursor:
        self.conn = connect(self.conn_str)
        return self.conn.cursor()
    
    def fechar(self) -> None:
        if self.conn != None:
            self.conn.close()

    def fetch_query(self, query: str, mensagem_debug: str = "Erro") -> list[dict] | dict | None:
        stmt = limpar_query(query)
        resultado = None

        try:
            cursor = self.iniciar()
            res = cursor.execute(stmt)
            rows = res.fetchall()

            cols = []
            for tup in res.description:
                cols.append(tup[0])
            
            if len(rows) > 1:
                resultado = []
                for row in rows:
                    i = 0
                    dict_row = {}
                    for i in range(len(row)):
                        dict_row[cols[i]] = row[i]
                        i+=1
                    resultado.append(dict_row)
            elif len(rows) == 1:
                resultado = {}
                i = 0
                for item in rows[0]:
                    resultado[cols[i]] = item
                    i+=1

        except Exception as erro:
            print(mensagem_debug + ": " + str(erro))

        finally:
            self.fechar()
        
        return resultado

    def dml_query(self, query: str, mensagem_debug: str = "Erro") -> None:
        stmt = limpar_query(query)

        try:
            cursor = self.iniciar()
            cursor.executescript(stmt)
            return 1
        
        except Exception as erro:
            print(mensagem_debug + ": " + str(erro))
            return -1
        finally:
            self.fechar()