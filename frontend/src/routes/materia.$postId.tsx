import { createFileRoute } from '@tanstack/react-router'
import { useState, useEffect } from 'react'
import { apiService } from '../api/api'
import { CONST } from '../const/Index'
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from '../components/ui/table'
import { Link } from '@tanstack/react-router'
import { Imateria } from '../const/Users.const'
import { NotebookPen } from 'lucide-react'

export const Route = createFileRoute('/materia/$postId')({
    component: Materia,
})

function Materia() {

    const { postId } = Route.useParams()
    const [materia, setMateria] = useState<Imateria>()
    const [carregando, setCarregando] = useState(true)

    const getAluno = async () => {
        try {
            const data = await apiService().makeRequest({
                method: CONST.HTTP.GET,
                path: `materias`,
                subpath: postId,
            })
            setMateria(data)
        } catch (err) {

        } finally {
            setCarregando(false)
        }
    }

    useEffect(() => {
        getAluno()
    }, [])

    return (
        <div>
            <div className='flex items-center flex-col'>
                <p className='font-bold text-xl'>{materia?.nome}</p>
                <p>Professor: {materia?.professor.nome}  {`[`}{materia?.professor.codigo}{`]`}</p>
                <p>Data de Inicio: {materia?.data_inicio.split('-').reverse().join('/')}</p>
                <p>Data de Encerramento: {materia?.data_fim.split('-').reverse().join('/')}</p>
            </div>


            <div className="p-2 lg:w-2/3 m-auto">
                <Table>
                    <TableCaption>Lista de Alunos</TableCaption>
                    <TableHeader>
                        <TableRow className="bg-blue-700 pointer-events-none">
                            <TableHead className="w-[100px] text-center text-white">
                                Cod. Aluno
                            </TableHead>
                            <TableHead className='text-white'> Nome </TableHead>
                            <TableHead className='text-center text-white'> Visualizar Notas </TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {
                            carregando ? (
                                <p>Carregando ...</p>
                            ) :
                                materia?.alunos.length ? (

                                    materia?.alunos.map((aluno) => (
                                        <TableRow key={aluno.id_usuario}>
                                            <TableCell>{aluno.codigo}</TableCell>
                                            <TableCell>{aluno.nome}</TableCell>
                                            <TableCell className='flex justify-center'>
                                                <Link
                                                    to="/materia/$postId/aluno/$alunoId"
                                                    params={{ postId: materia.id_materia.toString(), alunoId: aluno.id_usuario.toString() }}
                                                >
                                                    <NotebookPen />
                                                </Link>
                                            </TableCell>
                                        </TableRow>
                                    ))
                                ) : (
                                    <p> Nanhuma Aluno Vinculado </p>
                                )
                        }
                    </TableBody>
                </Table>
            </div>
        </div>
    )
}
