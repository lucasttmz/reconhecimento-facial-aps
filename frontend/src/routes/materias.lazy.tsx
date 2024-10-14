import { createLazyFileRoute } from '@tanstack/react-router'
import { makeRequestProps } from '../api/axios';
import { apiService } from "../api/api";
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "../components/ui/table"
import { useEffect, useState } from 'react';

export const Route = createLazyFileRoute('/materias')({
    component: Materias,
})

function Materias() {

    const [materias, setMaterias] = useState<materiasList>()
    const [carregando, setCarregando] = useState(true);

    const apiParams: makeRequestProps = {
        method: 'GET',
        path: 'materias',
    }




    useEffect(() => {

        const call = async () => {

            try {

                const data = await apiService().makeRequest(apiParams)
                console.log(data)
                setMaterias(data)
            }
            catch (err) {
                console.log(err)
            }
            finally {
                setCarregando(false);
            }
        }

        call()
    }, [])


    return (
        <div>
            <Table>
                <TableCaption>Lista de Materias</TableCaption>
                <TableHeader>
                    <TableRow>
                        <TableHead className="w-[100px]">Nome Materia</TableHead>
                        <TableHead>Nome Professor</TableHead>
                        <TableHead>Data Inicio</TableHead>
                        <TableHead>Data Fim</TableHead>
                        <TableHead>Quantidade Alunos</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>

                    {carregando ? (
                        <p>Carregando...</p>
                    ) : (
                        // Verifica se materias e materias.materias estão definidos
                        materias && materias.materias ? (
                            materias.materias.map((materia) => (
                                <TableRow key={materia.id_materia}>
                                    <TableCell>{materia.nome}</TableCell>
                                    <TableCell>{materia.professor.nome}</TableCell>
                                    <TableCell>{materia.data_inicio}</TableCell>
                                    <TableCell>{materia.data_fim}</TableCell>
                                    <TableCell>{materia.alunos.length}</TableCell>
                                </TableRow>
                            ))
                        ) : (
                            <p>Nenhuma matéria encontrada.</p>
                        )
                    )}
                </TableBody>
            </Table>
        </div>
    )
}

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
interface materiasList {
    materias: materias[]
}
interface aluno {
    id_usuario: number,
    codigo: string,
    nome: string,
    tipo: number
}
