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
import { CreateMateriaDialog } from '../components/Dialogs/CreateMateriaDialog';
import { useUserStore } from '../store/user';


export const Route = createLazyFileRoute('/materias')({
    component: Materias,
})

function Materias() {

    const [materias, setMaterias] = useState<materias[]>()
    const [carregando, setCarregando] = useState(true);
    const [response, setResponse] = useState<unknown>()
    const { states: { user }} = useUserStore();

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
            
            <div className='p-3'>
            {user?.permissions == 3 ? <CreateMateriaDialog/> : <span></span>}
                <Table>
                    <TableCaption>Lista de Materias</TableCaption>
                    <TableHeader>
                        <TableRow className='bg-blue-700'>
                            <TableHead className='text-white'>Nome Materia</TableHead>
                            <TableHead className='text-white'>Nome Professor</TableHead>
                            <TableHead className='text-white'>Data Inicio</TableHead>
                            <TableHead className='text-white'>Data Fim</TableHead>
                            <TableHead className='text-white'>Quantidade Alunos</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>

                        {
                            carregando ? (
                                <p>Carregando ... </p>
                            ) : (

                                materias?.length ? (
                                    materias.map((materia) => (
                                        <TableRow key={materia.id_materia}>
                                            <TableCell>{materia.nome}</TableCell>
                                            <TableCell>{materia.professor.nome}</TableCell>
                                            <TableCell>{materia.data_inicio.split('-').reverse().join('/')}</TableCell>
                                            <TableCell>{materia.data_fim.split('-').reverse().join('/')}</TableCell>
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
