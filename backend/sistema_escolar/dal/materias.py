from sistema_escolar.modelos.materia import Materia
from sistema_escolar.modelos.materia import MateriaSchema
from sistema_escolar.dal.conexao import Conexao

class MateriaDAO():
    def cadastrar_materia(self, materia: MateriaSchema) -> int:
        stmt: str = f"""
            INSERT INTO materia (nome, id_professor, data_inicio, data_fim) 
            VALUES (
                '{materia.nome}', 
                {materia.professor.codigo}, 
                '{materia.data_inicio}', 
                '{materia.data_fim}');
        """
        con = Conexao()

        try:
            con.iniciar()
            cursor = con.conn.cursor()
            res = cursor.execute(stmt)
            resultado = res.lastrowid
        except Exception as erro:
            print("Erro ao cadastrar materia: " + erro)
            resultado = -1
        finally:
            con.fechar()

        return resultado

    def buscar_materia_por_id(self, id: int) -> Materia:
        stmt = f"SELECT * FROM materia WHERE id_materia = {id}"
        con = Conexao()

        try:
            con.iniciar()
            cursor = con.conn.cursor()
            res = cursor.execute(stmt)

            id_materia, nome, id_professor, data_inicio, data_fim = res.fetchone()
            resultado = Materia(id_materia, id_professor, nome, data_inicio, data_fim)
        except Exception as erro:
            print("Erro ao buscar materia por ID" + erro)
        finally:
            con.fechar()

        return resultado
    
    def alterar_materia(self, id: int, alteracao: Materia) -> None:
        stmt = f"""
            UPDATE materia 
            SET 
                nome = {alteracao.nome}, 
                id_professor = {alteracao.id_professor}, 
                data_inicio = {alteracao.data_inicio}, 
                data_fim = {alteracao.data_fim}
            WHERE id_materia = {id}
        """
        con = Conexao()
        
        try:
            con.iniciar()
            cursor = con.conn.cursor()
            cursor.execute(stmt)
        except Exception as erro:
            print("Erro ao alterar matéria: " + erro)
        finally:
            con.fechar()

    def deletar_materia(self, id: int) -> None:
        stmt = f"DELETE FROM materia WHERE id_materia = {id}"
        con = Conexao()

        try:
            con.iniciar()
            cursor = con.conn.cursor()
            cursor.execute(stmt)
        except Exception as erro:
            print("Erro ao excluir matéria: " + erro)
        finally:
            con.fechar()
