from sqlite3 import connect
from sqlite3 import Connection
from pydantic import BaseModel

class Conexao(BaseModel):
    conn_str: str = "db/aps.db"
    conn: Connection

    def iniciar(self) -> None:
        self.conn = connect(self.conn_str)

    def fechar(self) -> None:
        if self.conn != None:
            self.conn.close()