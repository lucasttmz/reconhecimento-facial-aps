from sqlite3 import connect, Cursor
from pathlib import Path
from enum import IntEnum

import re


CAMINHO_DB = Path("sistema_escolar/dal/db/aps.db")


class TipoRetorno(IntEnum):
    FETCHONE = 1
    FETCHALL = 2


def limpar_query(texto: str) -> str:
    query_limpa = re.sub(r"\n|\t|\r", "", str(texto))

    if query_limpa[-1] == ";":
        return query_limpa
    else:
        return query_limpa + ";"


class Conexao:
    def iniciar(self) -> Cursor:
        self.conn = connect(CAMINHO_DB)
        return self.conn.cursor()

    def fechar(self) -> None:
        if self.conn is not None:
            self.conn.close()

    def fetch_query(
        self, query: str, tipo_retorno: TipoRetorno, mensagem_debug: str = "Erro"
    ) -> list[dict] | dict | None:
        stmt = limpar_query(query)
        resultado = None

        try:
            cursor = self.iniciar()
            res = cursor.execute(stmt)
            rows = res.fetchall()

            cols = []
            for tup in res.description:
                cols.append(tup[0])

            if tipo_retorno == TipoRetorno.FETCHALL:
                resultado = []
                for row in rows:
                    i = 0
                    dict_row = {}
                    for i in range(len(row)):
                        dict_row[cols[i]] = row[i]
                        i += 1
                    resultado.append(dict_row)
            elif tipo_retorno == TipoRetorno.FETCHONE:
                resultado = {}
                i = 0
                for item in rows[0]:
                    resultado[cols[i]] = item
                    i += 1

        except Exception as erro:
            print(f"{mensagem_debug}: {erro}")

        finally:
            self.fechar()

        return resultado

    def dml_query(self, query: str, mensagem_debug: str = "Erro") -> bool:
        stmt = limpar_query(query)
        resultado = True

        try:
            cursor = self.iniciar()
            cursor.executescript(stmt)

        except Exception as erro:
            print(f"{mensagem_debug}: {erro}")
            resultado = False
        finally:
            self.fechar()

        return resultado
