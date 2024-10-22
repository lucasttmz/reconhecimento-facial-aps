import { createLazyFileRoute} from '@tanstack/react-router'
import { useState, useEffect } from 'react'
import { apiService } from '../api/api'
import { makeRequestProps } from '../api/axios'
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
import {Iprofessor } from '../const/Users.const'

export const Route = createLazyFileRoute('/professores')({
  component: Professores,
})


function Professores() {
  const [carregando, setCarregando] = useState(true)
  const [professores, setProfessores] = useState<Iprofessor[]>()
  const apiParams: makeRequestProps = {
    method: CONST.HTTP.GET,
    path: 'professores',
  }
  const getAllAlunos = async () => {
    try {
      const data = await apiService().makeRequest(apiParams)

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
          <TableRow>
            <TableHead className="w-[100px] text-center">Cod. Aluno</TableHead>
            <TableHead>Nome</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {carregando ? (
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
          )}
        </TableBody>
      </Table>
    </div>
  )
}
