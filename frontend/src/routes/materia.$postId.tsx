import { createFileRoute } from '@tanstack/react-router'
import { makeRequestProps } from '../api/axios'
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
} from "../components/ui/table"
import { Link } from '@tanstack/react-router'
export const Route = createFileRoute('/materia/$postId')({
  component: Materia,
})

function Materia() {
  const { postId } = Route.useParams()
  const apiParams: makeRequestProps = {
    method: CONST.HTTP.GET,
    path: `materias`,
    subpath: postId
  }

  const [materia, setMateria] = useState()
  const [carregando, setCarregando] = useState(true)

  const getAluno = async () => {
    try {
      const data = await apiService().makeRequest(apiParams)
      console.log(data)
      setMateria(data)
    }
    catch (err) {
    }
    finally {
      setCarregando(false)
    }
  }

  useEffect(() => {
    getAluno()
  }, [])

  return(
    <div>
       <p>{materia?.nome}</p>
       <p>{materia?.professor.nome} : {materia?.professor.codigo}</p>
       <p>{materia?.data_inicio.split('-').reverse().join('/')}</p>
       <p>{materia?.data_fim.split('-').reverse().join('/')}</p>

       <div className='p-2 border-solid border-black'>
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

                            materia?.alunos.length ? (
                              materia?.alunos.map((aluno) => (

                                    <TableRow key={aluno.id_usuario}>
                                        <TableCell>{aluno.codigo}</TableCell>
                                        <TableCell>{aluno.nome}</TableCell>
                                        <TableCell> <Link to='/aluno/$postId' params={{ postId: aluno.id_usuario.toString() }}>aaa</Link> </TableCell>
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
