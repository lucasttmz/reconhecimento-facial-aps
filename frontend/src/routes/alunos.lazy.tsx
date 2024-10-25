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
import { SquarePen } from 'lucide-react'
import { Ialuno } from '../const/Users.const'
import { useUserStore } from '../store/user'


export const Route = createLazyFileRoute('/alunos')({
  component: Alunos,
})

function Alunos() {
  const [carregando, setCarregando] = useState(true)
  const [alunos, setAlunos] = useState<Ialuno[]>()
  const { states: { user } } = useUserStore()
  const apiParams: makeRequestProps = {
    method: CONST.HTTP.GET,
    path: 'alunos',
  }
  const getAllAlunos = async () => {
    try {
      const data = await apiService().makeRequest(apiParams)

      setAlunos(data)
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
        <TableCaption>Lista de Alunos</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead className="w-[100px] text-center">Cod. Aluno</TableHead>
            <TableHead>Nome</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {carregando ? (
            <p>Carregado</p>
          ) : alunos?.length ? (
            alunos.map((aluno) => (
              <TableRow key={aluno.id_usuario}>
                <TableCell>{aluno.codigo}</TableCell>
                <TableCell>{aluno.nome}</TableCell>

                {user?.permissions == 3 && (
                  <TableCell>
                    <Link
                      to="/aluno/$postId"
                      params={{ postId: aluno.id_usuario.toString()}}
                    >
                      <SquarePen color="green" />
                    </Link>
                  </TableCell>
                )}

              </TableRow>
            ))
          ) : (
            <p></p>
          )}
        </TableBody>
      </Table>
    </div>
  )
}
