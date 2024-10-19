export interface Permissions {
    permissionId: number,
    permissionRoutes: string[]
}

export const PERMISSIONS_ACTIONS_CONST: Permissions[] = [
    {
        permissionId: 1,
        permissionRoutes: ['boletim', 'home']
    },
    {
        permissionId: 2,
        permissionRoutes: ['home', 'alunos', 'materias', 'aluno', 'materia']
    },
    {
        permissionId: 3,
        permissionRoutes: ['home', 'alunos', 'materias', 'aluno', 'materia', 'professores']
    },
]

