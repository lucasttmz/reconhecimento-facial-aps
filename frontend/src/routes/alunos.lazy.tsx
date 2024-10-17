import { createLazyFileRoute, Link} from '@tanstack/react-router'
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

export const Route = createLazyFileRoute('/alunos')({
  component: Alunos,
})

interface aluno {
    id_usuario: number,
    codigo: string,
    nome: string,
    tipo: number
}

function Alunos(){
    
    const [carregando, setCarregando] = useState(true);
    const [alunos, setAlunos] = useState<aluno[]>();
    const apiParams: makeRequestProps = {
        method: CONST.HTTP.GET,
        path: 'alunos',
    }
    const getAllAlunos = async () => {

        try {
            const data = await apiService().makeRequest(apiParams)

            setAlunos(data)
        }
        catch (err) {

            console.log(err)
        }
        finally {
            setCarregando(false);
        }
    }

    useEffect(() => {

        getAllAlunos()

    }, [])

    return (
        <div>
            <Table>
                <TableCaption>Lista de Alunos</TableCaption>
                <TableHeader>
                    <TableRow>
                        <TableHead className="w-[100px] text-center">Cod. Aluno</TableHead>
                        <TableHead>Nome</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>

                    {
                        carregando ? (
                            <p>Carregado</p>
                        ) : (

                            alunos?.length ? (
                                alunos.map((aluno) => (
                                    <Link to='/aluno/$postId' params={{postId: aluno.id_usuario.toString()}} key={aluno.id_usuario}>
                                        <TableRow >
                                        <TableCell>{aluno.codigo}</TableCell>
                                        <TableCell>{aluno.nome}</TableCell>                           
                                        </TableRow>
                                    </Link>
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

