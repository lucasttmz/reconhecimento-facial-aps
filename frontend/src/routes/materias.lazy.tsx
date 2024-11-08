import { createLazyFileRoute, Link } from '@tanstack/react-router'
import { makeRequestProps } from '../api/axios'
import { apiService } from '../api/api'
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from '../components/ui/table'
import { useEffect, useState } from 'react'
import { CONST } from '../const/Index'
import { CreateMateriaDialog } from '../components/Dialogs/CreateMateriaDialog'
import { useUserStore } from '../store/user'
import { Eye } from 'lucide-react'
import { Imateria } from '../const/Users.const'

export const Route = createLazyFileRoute('/materias')({
    component: Materias,
})

function Materias() { //Lista de Todas as Materias 
    const [materias, setMaterias] = useState<Imateria[]>()
    const [carregando, setCarregando] = useState(true)
    const { states: { user }, } = useUserStore()

    const getAllMaterias = async () => {
        try {
            const data = await apiService().makeRequest({
                method: CONST.HTTP.GET,
                path: 'materias',
            })
            setMaterias(data)
            return data
        } catch (err) {
            console.log(err)
        } finally {
            setCarregando(false)
        }
    }
    const AtualizarMaterias = (atualizar: boolean) => { // Atualiza as Materias quando uma é adicionada
        if (atualizar) { getAllMaterias() }
    }

    useEffect(() => {
        getAllMaterias()
    }, [])

    return (
        <div>
            <div className="p-3">
                {
                    user?.permissions == 3 &&
                    (

                        <div className='flex justify-end mr-3 mb-2 w-full'>
                            <CreateMateriaDialog AtualizarMaterias={AtualizarMaterias} />
                        </div>
                    )
                }
                <Table>
                    <TableCaption>Lista de Materias</TableCaption>
                    <TableHeader>
                        <TableRow className=" bg-blue-700 pointer-events-none">
                            <TableHead className=" w-[150px] text-white"> Nome Materia </TableHead>
                            <TableHead className="text-white"> Nome Professor </TableHead>
                            <TableHead className="text-white"> Data Inicio </TableHead>
                            <TableHead className="text-white"> Data Fim </TableHead>
                            <TableHead className="text-white"> Quantidade Alunos </TableHead>
                            <TableHead className="text-white"> Ações </TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {carregando ? (
                            <p>Carregando ... </p>
                        ) : materias?.length ? (
                            materias.map((materia) => (
                                <TableRow key={materia.id_materia}>
                                    <TableCell> {materia.nome} </TableCell>
                                    <TableCell> {materia.professor.nome} </TableCell>
                                    <TableCell> {materia.data_inicio.split('-').reverse().join('/')} </TableCell>
                                    <TableCell> {materia.data_fim.split('-').reverse().join('/')} </TableCell>
                                    <TableCell> {materia.alunos.length} </TableCell>
                                    <TableCell>
                                        <Link
                                            to="/materia/$postId"
                                            params={{ postId: materia.id_materia.toString() }}
                                        >
                                            <Eye />
                                        </Link>
                                    </TableCell>
                                </TableRow>
                            ))
                        ) : (
                            <p></p>
                        )}
                    </TableBody>
                </Table>
            </div>
        </div>
    )
}
