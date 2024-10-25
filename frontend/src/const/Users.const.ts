export interface Imateria {
    id_materia: number,
    nome: string,
    professor: Iprofessor
    data_inicio: string
    data_fim: string
    alunos: Ialuno[]
}
export interface Ialuno {
    id_usuario: number,
    codigo: string,
    nome: string,
    tipo: number
}
export interface Iprofessor {
    id_usuario: number,
    codigo: string,
    nome: string,
    tipo: number
}
export interface ImateriaAluno {
    aluno: {
        id_usuario: number,
        codigo: string,
        nome: string,
        tipo: number
    },
    materia: {
        id_materia: number,
        nome: string,
        professor: string,
        data_inicio: string,
        data_fim: string
    },
    nota: number,
    faltas: number
}

interface ImateriaNota {
    materia: {
        id_materia: number,
        nome: string,
        professor: string,
        data_inicio: string,
        data_fim: string
    },
    nota: number,
    faltas: number
}