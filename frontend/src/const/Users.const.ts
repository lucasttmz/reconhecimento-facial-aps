
interface materias {

    id_materia: number,
    nome: string,
    professor: {
        id_usuario: number,
        codigo: string,
        nome: string,
        tipo: number
    }
    data_inicio: string
    data_fim: string
    alunos: aluno[]

}
interface aluno {
    id_usuario: number,
    codigo: string,
    nome: string,
    tipo: number
}
