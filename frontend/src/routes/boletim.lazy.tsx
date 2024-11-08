import { createLazyFileRoute, Link, } from '@tanstack/react-router'
import { useState, useEffect } from 'react'
import { apiService } from '../api/api'
import { Table, TableCaption, TableHeader, TableRow, TableHead, TableBody, TableCell } from '../components/ui/table'
import { CONST } from '../const/Index'
import { ImateriaAluno } from '../const/Users.const'
import { Eye } from 'lucide-react'

export const Route = createLazyFileRoute('/boletim')({
    component: Boletim,
})

function Boletim() {
    const [boletim, setBoletim] = useState<ImateriaAluno[]>()

    const getNotasFaltas = async () => {

        try {
            const data = await apiService().makeRequest({
                method: CONST.HTTP.GET,
                path: 'boletim/',
            })
 
            setBoletim(data)
        } catch (err) {

            console.log(err)
        }
    }

    useEffect(() => {
        getNotasFaltas()
    }, [])

    return (
        <div className="p-2 border-solid border-black">
            <Table>
                <TableCaption>Boletim</TableCaption>
                <TableHeader>
                    <TableRow className="bg-blue-700 pointer-events-none">
                        <TableHead className='w-[150px] text-white'> Materia</TableHead>
                        <TableHead className='text-white'> Nota </TableHead>
                        <TableHead className='text-white'> Faltas </TableHead>
                        <TableHead className=' w-[90px] text-white text-center'> Visualizar Matéria</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {
                        boletim?.map((boletimNota) => (
                            <TableRow key={boletimNota.materia.id_materia}>
                                <TableCell> {boletimNota.materia.nome}</TableCell>
                                <TableCell> {boletimNota.nota}</TableCell>
                                <TableCell> {boletimNota.faltas}</TableCell>
                                <TableCell className='flex justify-center'>
                                    <Link
                                        to='/boletim/$materiaId'
                                        params={{ materiaId: boletimNota.materia.id_materia.toString() }}
                                    >
                                        <Eye />
                                    </Link>
                                </TableCell>
                            </TableRow>
                        ))
                    }
                </TableBody>
            </Table>
        </div>
    )
}
