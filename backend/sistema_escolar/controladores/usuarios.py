import uuid

from fastapi import HTTPException

from sistema_escolar.modelos.usuario import UsuarioSchema, AtualizarUsuarioSchema
from sistema_escolar.modelos.genericos import MensagemSchema
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
                "id_usuario": aluno.id_usuario,
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

        usuarioSchema = {
            "id_usuario": aluno.id_usuario,
            "codigo": aluno.codigo, 
            "nome": aluno.nome, 
            "tipo": aluno.tipo
        }

        return UsuarioSchema(**usuarioSchema)

    def listar_todos_professores(self) -> list[UsuarioSchema]:
        usuarioDAO = UsuarioDAO()
        professores = usuarioDAO.todos_os_professores()

        if professores is None:
            raise HTTPException(404)

        resultado: list[UsuarioSchema] = []
        for professor in professores:
            usuarioSchema = {
                "id_usuario": professor.id_usuario,
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
            "id_usuario": professor.id_usuario,
            "codigo": professor.codigo,
            "nome": professor.nome,
            "tipo": professor.tipo,
        }

        return UsuarioSchema(**usuarioSchema)
    
    def listar_info_usuario(self, id_usuario: int) -> UsuarioSchema:
        usuarioDAO = UsuarioDAO()
        usuario = usuarioDAO.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            raise HTTPException(404)

        usuarioSchema = {
            "id_usuario": usuario.id_usuario,
            "codigo": usuario.codigo,
            "nome": usuario.nome,
            "tipo": usuario.tipo,
        }

        return UsuarioSchema(**usuarioSchema)

    def sequencia_usuario(self) -> int:
        usuarioDAO = UsuarioDAO()
        return usuarioDAO.sequencia_usuario()
    
    def gerar_codigo_usuario(self) -> str:
        return str(uuid.uuid4()).upper()[:8]

    def criar_usuario(self, id_usuario: int, nome_usuario: str) -> MensagemSchema:
        dados = {
            "id_usuario": id_usuario,
            "nome": nome_usuario,
            "codigo": self.gerar_codigo_usuario(),
            "tipo": 1
        }
        print(dados)
        usuarioDAO = UsuarioDAO()
        sucesso = usuarioDAO.criar_usuario(UsuarioSchema(**dados))

        if not sucesso:
            raise HTTPException(404)

        return MensagemSchema(mensagem=f"{nome_usuario} registrado com sucesso!")

    def atualizar_usuario(self, id_usuario: int, usuario_atualizado: AtualizarUsuarioSchema) -> MensagemSchema:
        usuarioDAO = UsuarioDAO()
        sucesso = usuarioDAO.atualizar_tipo_usuario(id_usuario, usuario_atualizado.tipo)

        if not sucesso:
            raise HTTPException(404)

        return MensagemSchema(mensagem=f"Cargo atualizado com sucesso!")
