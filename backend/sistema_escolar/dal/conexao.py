from sqlite3 import connect, Cursor, Connection
from pathlib import Path
from enum import IntEnum

import os
import re

# CAMINHO_DB = Path("backend\\sistema_escolar\\dal\\db\\aps.db") # Caminho relativo
CAMINHO_DB = os.path.join(os.getcwd(), "dal\\db\\aps.db") # Caminho completo desde o C:\

class TipoRetorno(IntEnum):
    FETCHONE = 1
    FETCHALL = 2


def limpar_query(texto: str) -> str:
    query_limpa = re.sub(r"\n|\t|\r", "", str(texto))

    if query_limpa[-1] == ";":
        return query_limpa
    else:
        return query_limpa + ";"

def linha_para_dicionario(cursor: Cursor, row) -> dict | None:
    d_row: dict = {}
    for i, col in enumerate(cursor.description):
        d_row[col[0]] = row[i]
    return d_row


class Conexao:
    def __init__(self):
        self.conn: Connection = None

    def iniciar(self) -> Cursor:
        self.conn = connect(CAMINHO_DB)
        self.conn.row_factory = linha_para_dicionario
        return self.conn.cursor()

    def fechar(self) -> None:
        if self.conn is not None:
            self.conn.close()

    def fetch_query(self, query: str, tipo_retorno: TipoRetorno = TipoRetorno.FETCHONE, mensagem_debug: str = "Erro") -> list[dict] | dict | None:
        stmt = limpar_query(query)
        resultado = None

        try:
            cursor = self.iniciar()
            result = cursor.execute(stmt)

            if tipo_retorno == TipoRetorno.FETCHONE:
                resultado = result.fetchone()
                
            if tipo_retorno == TipoRetorno.FETCHALL:
                resultado = []
                for linha in result.fetchall():
                    resultado.append(linha)


        except Exception as erro:
            print(f"{mensagem_debug}: {erro}")

        finally:
            self.fechar()

        print(resultado)

        return resultado

    def dml_query(self, query: str, mensagem_debug: str = "Erro", checar_alteracao: bool = False) -> bool:
        stmt = limpar_query(query)
        resultado = True

        try:
            cursor = self.iniciar()
            cursor.execute(stmt)

            if checar_alteracao and cursor.rowcount <= 0:
                resultado = False

        except Exception as erro:
            print(f"{mensagem_debug}: {erro}")
            resultado = False
        finally:
            self.fechar()

        return resultado
