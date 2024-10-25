import { createFileRoute } from '@tanstack/react-router'
import { makeRequestProps } from '../api/axios'
import { useState, useEffect } from 'react'
import { useNavigate } from '@tanstack/react-router'
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
  const navigate = useNavigate()
  const apiParams: makeRequestProps = {
    method: CONST.HTTP.GET,
    path: `materias`,
    subpath: postId,
  }

  const [materia, setMateria] = useState<Imateria>()
  const [carregando, setCarregando] = useState(true)

  const getAluno = async () => {
    try {
      const data = await apiService().makeRequest(apiParams)
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


      <div className="p-2 border-solid border-black">
        <Table>
          <TableCaption>Lista de Alunos</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[100px] text-center">
                Cod. Aluno
              </TableHead>
              <TableHead> Nome </TableHead>
              <TableHead className='text-center'> Vizualiazar Notas </TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {carregando ? (
              <p>Carregado</p>
            ) : materia?.alunos.length ? (
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
              <p></p>
            )}
          </TableBody>
        </Table>
      </div>
    </div>
  )
}
