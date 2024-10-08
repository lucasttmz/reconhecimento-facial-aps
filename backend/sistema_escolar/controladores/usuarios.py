from fastapi import HTTPException

from sistema_escolar.modelos.usuario import UsuarioSchema
from sistema_escolar.dal.usuarios import UsuarioDAO


class UsuarioControle:
    def listar_todos_alunos(self) -> list[UsuarioSchema]:
        usuarioDAO = UsuarioDAO()
        alunos = usuarioDAO.todos_os_alunos()

        if alunos is None:
            raise HTTPException(404)

        resultado = []
        for aluno in alunos:
            usuarioSchema = {
                "codigo": aluno.codigo,
                "nome": aluno.nome,
                "tipo": aluno.tipo,
            }
            resultado.append(UsuarioSchema(**usuarioSchema))

        return resultado

    def listar_info_aluno(self, id_aluno: int) -> UsuarioSchema:
        usuarioDAO = UsuarioDAO()
        aluno = usuarioDAO.buscar_aluno_por_id(id_aluno)

        if aluno is None:
            raise HTTPException(404)

        usuarioSchema = {"codigo": aluno.codigo, "nome": aluno.nome, "tipo": aluno.tipo}

        return UsuarioSchema(**usuarioSchema)

    def listar_todos_professores(self) -> list[UsuarioSchema]:
        usuarioDAO = UsuarioDAO()
        professores = usuarioDAO.todos_os_professores()

        if professores is None:
            raise HTTPException(404)

        resultado: list[UsuarioSchema] = []
        for professor in professores:
            usuarioSchema = {
                "codigo": professor.codigo,
                "nome": professor.nome,
                "tipo": professor.tipo,
            }
            resultado.append(UsuarioSchema(**usuarioSchema))

        return resultado

    def listar_info_professor(self, id_professor: int) -> UsuarioSchema:
        usuarioDAO = UsuarioDAO()
        professor = usuarioDAO.buscar_professor_por_id(id_professor)

        if professor is None:
            raise HTTPException(404)

        usuarioSchema = {
            "codigo": professor.codigo,
            "nome": professor.nome,
            "tipo": professor.tipo,
        }

        return UsuarioSchema(**usuarioSchema)

    def criar_usuario(self, nome_usuario: UsuarioSchema): ...

    def atualizar_usuario(self, id: int, usuario_atualizado: UsuarioSchema): ...
