from enum import IntEnum
from pathlib import Path
import re
from sqlite3 import connect, Cursor, Connection


CAMINHO_DB = Path("sistema_escolar/dal/db/aps.db")  # Caminho relativo


class TipoRetorno(IntEnum):
    """Tipos de retorno das querys do sqlite3"""

    FETCHONE = 1
    FETCHALL = 2


class Conexao:
    def __init__(self):
        self.conn: Connection | None = None

    def iniciar(self) -> Connection:
        """Inicia a conexão com o BD"""

        self.conn = connect(CAMINHO_DB)
        self.conn.row_factory = self.linha_para_dicionario
        return self.conn

    def fechar(self) -> None:
        """Fecha a conexão com o BD"""

        if self.conn is not None:
            self.conn.close()

    def limpar_query(self, query: str) -> str:
        """Remove espaços em branco com regex e adiciona ';' se estiver faltando"""

        query_limpa = re.sub(r"\n|\t|\r", "", str(query))
        if query_limpa[-1] == ";":
            return query_limpa
        else:
            return query_limpa + ";"

    def linha_para_dicionario(self, cursor: Cursor, row) -> dict | None:
        """Mapeia os dados retornados do BD para um dicionário chave:valor"""

        d_row: dict = {}
        for i, col in enumerate(cursor.description):
            d_row[col[0]] = row[i]
        return d_row

    def fetch_query(
        self,
        query: str,
        params: list,
        tipo_retorno: TipoRetorno = TipoRetorno.FETCHONE,
        mensagem_debug: str = "Erro",
    ) -> list[dict] | dict | None:
        """Executa query do tipo fetch (select) conforme o tipo especificado"""

        stmt = self.limpar_query(query)
        resultado = None
        cursor = None

        try:
            with self.iniciar() as conn:
                # Executa a query, utilizando os parametros se especificados
                cursor = conn.cursor()
                if params:
                    result = cursor.execute(stmt, params)
                else:
                    result = cursor.execute(stmt)

                # Chama o método fetch confome o tipo esperado
                if tipo_retorno == TipoRetorno.FETCHONE:
                    resultado = result.fetchone()  # 1 valor

                if tipo_retorno == TipoRetorno.FETCHALL:
                    resultado = [linha for linha in result.fetchall()]  # vários valores

        except Exception as erro:
            print(f"{mensagem_debug}: {erro}")

        finally:
            # Fecha o cursor
            if cursor is not None:
                cursor.close()

        return resultado

    def dml_query(self, query: str, params: list, mensagem_debug: str = "Erro") -> int:
        """Executa a query do tipo DML (insert/update/delete)"""

        stmt = self.limpar_query(query)
        linhas_afetadas: int = 0
        cursor = None

        try:
            with self.iniciar() as conn:
                cursor = conn.cursor()
                cursor.execute(stmt, params)
                # Checa se linhas forão afetadas (verificar se atualizou algo)
                linhas_afetadas = cursor.rowcount
                conn.commit()

        except Exception as erro:
            # Se der erro, informa que nada alterou
            print(f"{mensagem_debug}: {erro}")
            linhas_afetadas = -1

        finally:
            # Fecha o cursor
            if cursor is not None:
                cursor.close()

        return linhas_afetadas
