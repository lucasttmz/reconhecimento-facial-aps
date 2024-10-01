from sistema_escolar.modelos.usuario import TipoUsuario, UsuarioSchema, Usuario
from sistema_escolar.dal.usuarios import UsuarioDAO

class UsuarioControle():
    def listar_todos_alunos(self) -> list[UsuarioSchema]:
        usuarioDAO = UsuarioDAO()
        alunos = usuarioDAO.todos_os_alunos()

        resultado: list[UsuarioSchema] = []
        for aluno in alunos:
            usuarioSchema = {
                "codigo" : aluno.codigo,
                "nome": aluno.nome,
                "tipo": aluno.tipo
            }
            resultado.append(UsuarioSchema(**usuarioSchema))

        return resultado

    def listar_info_aluno(self, id_aluno: int) -> UsuarioSchema:
        usuarioDAO = UsuarioDAO()
        aluno = usuarioDAO.buscar_aluno_por_id(id_aluno)
    
        usuarioSchema = {
            "codigo": aluno.codigo,
            "nome": aluno.nome,
            "tipo": aluno.tipo
        }

        return UsuarioSchema(**usuarioSchema)

    
    def listar_todos_professores(self) -> list[UsuarioSchema]:
        usuarioDAO = UsuarioDAO()
        professores = usuarioDAO.todos_os_professores()

        resultado: list[UsuarioSchema] = []
        for professor in professores:
            usuarioSchema = {
                "codigo" : professor.codigo,
                "nome": professor.nome,
                "tipo": professor.tipo
            }
            resultado.append(UsuarioSchema(**usuarioSchema))

        return resultado

    def listar_info_professor(self, id_professor: int) -> UsuarioSchema:
        usuarioDAO = UsuarioDAO()
        professor = usuarioDAO.buscar_usuario_por_id(id_professor)

        usuarioSchema = {
            "codigo": professor.codigo,
            "nome": professor.nome,
            "tipo": professor.tipo
        }

        return UsuarioSchema(**usuarioSchema)
    
    # TODO
    # Usuário
    # Pesquisar Usuário por ID (id_aluno) -> Usuário
    # Criar Usuário ( UsuárioSchema) -> id_usuario
    # Atualizar Usuário (id_usuario,  UsuárioSchema) -> None

    def criar_usuario(self, nome_usuario: UsuarioSchema) -> int:
        pass

    def buscar_usuario_por_id(self, id: int) -> UsuarioSchema:
        pass

    def atualizar_usuario(self, id: int, usuario_atualizado: UsuarioSchema) -> int:
        pass
