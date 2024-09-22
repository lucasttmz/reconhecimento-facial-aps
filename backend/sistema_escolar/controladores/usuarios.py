from sistema_escolar.modelos.usuario import TipoUsuario, UsuarioSchema


class UsuarioControle():
    def listar_todos_alunos(self) -> list[UsuarioSchema]:
        alunos = [
            {"codigo": "AL_LUC4S", "nome": "Lucas", "tipo": TipoUsuario.ALUNO},
            {"codigo": "AL_F3L1P3", "nome": "Felipe", "tipo": TipoUsuario.ALUNO},
            {"codigo": "AL_S4MU3L", "nome": "Samuel", "tipo": TipoUsuario.ALUNO},
        ]
        return [UsuarioSchema(**aluno) for aluno in alunos]

    def listar_info_aluno(self, id_aluno: int) -> UsuarioSchema:
        return self.listar_todos_alunos()[id_aluno % 3]
    
    def listar_todos_professores(self) -> list[UsuarioSchema]:
        professores = [
            {"codigo": "PF_M4R14", "nome": "Maria", "tipo": TipoUsuario.PROFESSOR},
            {"codigo": "PF_J040", "nome": "João", "tipo": TipoUsuario.PROFESSOR},
            {"codigo": "PF_M4RC0S", "nome": "Marcos", "tipo": TipoUsuario.PROFESSOR},
        ]
        return [UsuarioSchema(**professor) for professor in professores]

    def listar_info_professor(self, id_professor: int) -> UsuarioSchema:
        return self.listar_todos_professores()[id_professor % 3]
    
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
