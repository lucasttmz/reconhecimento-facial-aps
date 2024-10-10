export interface PermissionActions {
    VER_BOLETIM: boolean;
    VER_MATERIAS: boolean;
    VER_ALUNOS: boolean;
    VERIFICAR_ALUNOS: boolean;
    VER_PROFESSORES: boolean;
    ALTERAR_CRIAR_MATERIAS: boolean;
}

export interface Permissions {
    Aluno: PermissionActions;
    Professor: PermissionActions;
    Diretor: PermissionActions;
}

export const PERMISSIONS_ACTIONS_CONST: Permissions  = {
    'Aluno': {
        VER_BOLETIM: true,
        VER_MATERIAS: false,
        VER_ALUNOS: false,
        VERIFICAR_ALUNOS: false,
        VER_PROFESSORES: false,
        ALTERAR_CRIAR_MATERIAS: false,
    },
    'Professor': {
        VER_BOLETIM: false,
        VER_MATERIAS: true,
        VER_ALUNOS: true,
        VERIFICAR_ALUNOS: false,
        VER_PROFESSORES: false,
        ALTERAR_CRIAR_MATERIAS: false,
    },
    'Diretor': {
        VER_BOLETIM: false,
        VER_MATERIAS: true,
        VER_ALUNOS: true,
        VERIFICAR_ALUNOS: true,
        VER_PROFESSORES: true,
        ALTERAR_CRIAR_MATERIAS: true,
    },
}