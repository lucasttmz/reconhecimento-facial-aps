import { createLazyFileRoute } from '@tanstack/react-router'
import { useState, useEffect } from 'react'
import { apiService } from '../api/api'
import {
    Table,
    TableCaption,
    TableHeader,
    TableRow,
    TableHead,
    TableBody,
    TableCell
} from '../components/ui/table'
import { CONST } from '../const/Index'
import { Iprofessor } from '../const/Users.const'

export const Route = createLazyFileRoute('/professores')({
    component: Professores,
})


function Professores() {
    const [carregando, setCarregando] = useState(true)
    const [professores, setProfessores] = useState<Iprofessor[]>()

    const getAllAlunos = async () => {
        try {
            const data = await apiService().makeRequest({
                method: CONST.HTTP.GET,
                path: 'professores',
            })
            setProfessores(data)
        } catch (err) {
            console.log(err)
        } finally {
            setCarregando(false)
        }
    }

    useEffect(() => {
        getAllAlunos()
    }, [])

    return (
        <div className="p-2 border-solid border-black">
            <Table>
                <TableCaption>Lista de Professores</TableCaption>
                <TableHeader>
                    <TableRow className="bg-blue-700 pointer-events-none">
                        <TableHead className="w-[140px]  text-white">Cod. Professor</TableHead>
                        <TableHead className='text-white'>Nome</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {
                        carregando ? (
                            <p>Carregado</p>
                        ) : professores?.length ? (
                            professores.map((professor) => (
                                <TableRow key={professor.id_usuario}>
                                    <TableCell>{professor.codigo}</TableCell>
                                    <TableCell>{professor.nome}</TableCell>
                                </TableRow>
                            ))
                        ) : (
                            <p></p>
                        )
                    }
                </TableBody>
            </Table>
        </div>
    )
}
