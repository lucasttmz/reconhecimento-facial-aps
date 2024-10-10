from sqlite3 import connect, Cursor, Connection
from pathlib import Path
from enum import IntEnum

import os
import re

CAMINHO_DB = Path("sistema_escolar/dal/db/aps.db") # Caminho relativo
# CAMINHO_DB = Path(os.path.join(os.getcwd(), "dal\\db\\aps.db")) # Caminho completo desde o C:\..\sistema_escolar\

class TipoRetorno(IntEnum):
    FETCHONE = 1
    FETCHALL = 2

class Conexao:
    def __init__(self):
        self.conn: Connection | None = None

    def iniciar(self) -> Connection:
        self.conn = connect(CAMINHO_DB)
        self.conn.row_factory = self.linha_para_dicionario
        return self.conn

    def fechar(self) -> None:
        if self.conn is not None:
            self.conn.close()

    def limpar_query(self, query: str) -> str:
        query_limpa = re.sub(r"\n|\t|\r", "", str(query))
        if query_limpa[-1] == ";":
            return query_limpa
        else:
            return query_limpa + ";"
        
    def linha_para_dicionario(self, cursor: Cursor, row) -> dict | None:
        d_row: dict = {}
        for i, col in enumerate(cursor.description):
            d_row[col[0]] = row[i]
        return d_row

    def fetch_query(self, query: str, tipo_retorno: TipoRetorno = TipoRetorno.FETCHONE, mensagem_debug: str = "Erro") -> list[dict] | dict | None:
        stmt = self.limpar_query(query)
        resultado = None
        cursor = None

        try:
            with self.iniciar() as conn:
                cursor = conn.cursor()
                result = cursor.execute(stmt)

                if tipo_retorno == TipoRetorno.FETCHONE:
                    resultado = result.fetchone()
                    
                if tipo_retorno == TipoRetorno.FETCHALL:
                    resultado = [linha for linha in result.fetchall()]

        except Exception as erro:
            print(f"{mensagem_debug}: {erro}")

        finally:
            if cursor is not None:
                cursor.close()

        return resultado

    def dml_query(self, query: str, mensagem_debug: str = "Erro") -> int:
        stmt = self.limpar_query(query)
        linhas_afetadas: int = 0
        cursor = None

        try:
            with self.iniciar() as conn:
                cursor = conn.cursor()
                cursor.execute(stmt)
                linhas_afetadas = cursor.rowcount
                conn.commit() 

        except Exception as erro:
            print(f"{mensagem_debug}: {erro}")
            linhas_afetadas = -1

        finally:
            if cursor is not None:
                cursor.close()

        return linhas_afetadas
