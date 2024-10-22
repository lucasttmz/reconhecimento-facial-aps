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

function Materias() {
  const [materias, setMaterias] = useState<Imateria[]>()
  const [carregando, setCarregando] = useState(true)
  const [response, setResponse] = useState<unknown>()
  const {
    states: { user },
  } = useUserStore()

  const apiParams: makeRequestProps = {
    method: CONST.HTTP.GET,
    path: 'materias',
  }
  const getAllMaterias = async () => {
    try {
      const data = await apiService().makeRequest(apiParams)
      setMaterias(data)
      return data
    } catch (err) {
      console.log(err)
    } finally {
      setCarregando(false)
    }
  }

  useEffect(() => {
    getAllMaterias()
  }, [])

  return (
    <div>
      <div className="p-3">
        {user?.permissions == 3 ? <CreateMateriaDialog /> : <span></span>}
        <Table>
          <TableCaption>Lista de Materias</TableCaption>
          <TableHeader>
            <TableRow className="bg-blue-700 pointer-events-none">
              <TableHead className="text-white">Nome Materia</TableHead>
              <TableHead className="text-white">Nome Professor</TableHead>
              <TableHead className="text-white">Data Inicio</TableHead>
              <TableHead className="text-white">Data Fim</TableHead>
              <TableHead className="text-white">Quantidade Alunos</TableHead>
              <TableHead className="text-white"> Ações</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {carregando ? (
              <p>Carregando ... </p>
            ) : materias?.length ? (
              materias.map((materia) => (
                <TableRow key={materia.id_materia}>
                  <TableCell>{materia.nome}</TableCell>
                  <TableCell>{materia.professor.nome}</TableCell>
                  <TableCell>
                    {materia.data_inicio.split('-').reverse().join('/')}
                  </TableCell>
                  <TableCell>
                    {materia.data_fim.split('-').reverse().join('/')}
                  </TableCell>
                  <TableCell>{materia.alunos.length}</TableCell>
                  <TableCell>
                    {' '}
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
