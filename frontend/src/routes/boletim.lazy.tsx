import { createLazyFileRoute,} from '@tanstack/react-router'
import { useState, useEffect } from 'react'
import { apiService } from '../api/api'
import { Table, TableCaption, TableHeader, TableRow, TableHead, TableBody, TableCell } from '../components/ui/table'
import { CONST } from '../const/Index'
import { ImateriaAluno } from '../const/Users.const'

export const Route = createLazyFileRoute('/boletim')({
  component: Boletim,
})

function Boletim() {
  const [boletim, setBoletim] = useState<ImateriaAluno[]>()
  
  const getAllAlunos = async () => {
    
    try {
      const data = await apiService().makeRequest({
        method: CONST.HTTP.GET,
        path: 'boletim',
      })
      console.log(data)
      setBoletim(data)
    } catch (err) {

      console.log(err)
    }
  }

  useEffect(() => {
    getAllAlunos()
  }, [])

  return (
    <div className="p-2 border-solid border-black">
      <Table>
        <TableCaption>Boletim</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead> Materia</TableHead>
            <TableHead> Nota </TableHead>
            <TableHead> Faltas </TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {
            boletim?.map((boletimNota)=>(
              <TableRow key={boletimNota.materia.id_materia}>
                <TableCell> {boletimNota.materia.nome}</TableCell>
                <TableCell> {boletimNota.nota}</TableCell>
                <TableCell> {boletimNota.faltas}</TableCell>

              </TableRow>
            ))
          }
        </TableBody>
      </Table>
    </div>
  )
}
