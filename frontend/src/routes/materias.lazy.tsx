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
import { CONST } from '../const/Index';

export const Route = createLazyFileRoute('/materias')({
    component: Materias,
})

function Materias() {

    const [materias, setMaterias] = useState<materias[]>()
    const [carregando, setCarregando] = useState(true);
    const [response, setResponse] = useState<unknown>()

    const apiParams: makeRequestProps = {
        method: CONST.HTTP.GET,
        path: 'materias',
    }
    const getAllMaterias = async () => {

        try {
            const data = await apiService().makeRequest(apiParams)
            setMaterias(data)
            return data 
        }
        catch (err) {

            console.log(err)
        }
        finally {
            setCarregando(false);
        }
    }

    useEffect(() => {

        getAllMaterias()

    }, [])



    return (
        <div>
            <Table>
                <TableCaption>Lista de Materias</TableCaption>
                <TableHeader>
                    <TableRow>
                        <TableHead className="w-[100px] text-center">Nome Materia</TableHead>
                        <TableHead>Nome Professor</TableHead>
                        <TableHead>Data Inicio</TableHead>
                        <TableHead>Data Fim</TableHead>
                        <TableHead>Quantidade Alunos</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>

                    {
                        carregando ? (
                            <p>Carregado</p>
                        ) : (

                            materias?.length ? (
                                materias.map((materia) => (
                                    <TableRow key={materia.id_materia}>
                                        <TableCell>{materia.nome}</TableCell>
                                        <TableCell>{materia.professor.nome}</TableCell>
                                        <TableCell>{materia.data_inicio}</TableCell>
                                        <TableCell>{materia.data_fim}</TableCell>
                                        <TableCell>{materia.alunos.length}</TableCell>
                                    </TableRow>
                                ))
                            ) : (
                                <p></p>
                            )
                        )
                    }
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
interface aluno {
    id_usuario: number,
    codigo: string,
    nome: string,
    tipo: number
}
