import { createFileRoute } from '@tanstack/react-router'
import { apiService } from '../api/api'
import { makeRequestProps } from '../api/axios'
import { CONST } from '../const/Index'
import { useEffect, useState } from 'react'
import { User } from 'lucide-react'
import { Button } from '../components/ui/button'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../components/ui/select"
import { toast } from '../hooks/use-toast'


export const Route = createFileRoute('/aluno/$postId')({
  component: Aluno,
})

interface Ialuno {
  id_usuario: number
  codigo: string
  nome: string
  tipo: number
}

function Aluno() {
  const { postId } = Route.useParams()

  const apiParams: makeRequestProps = {
    method: CONST.HTTP.GET,
    path: `alunos/${postId}`,
  }

  const [aluno, setAluno] = useState<Ialuno>()
  const [tipo, setTipo] = useState('')


  const setNewTipo = async ()=> {
    const data = await apiService().makeRequest({
      method: CONST.HTTP.PUT,
      path: 'usuarios',
      subpath: `${aluno?.id_usuario}`,
      body:{
        tipo: parseInt(tipo)
      }
    })

    console.log(data)
    if (data.status == 200) {
      toast({
        title: 'Usuario Atualizado',
        description: data.data.mensagem
      })
    }
    else {
      toast({
        title: 'Erro ao Atualizar tipo',
        description: data.response.data.detail[0].msg,
        variant: "destructive"
      })
    }
  }
  const getAluno = async () => {
    try {
      const data = await apiService().makeRequest(apiParams)
      console.log(data)
      setAluno(data)

    } catch (err) {

    }
  }

  useEffect(() => {
    getAluno()
  }, [])

  return (
    <div className='m-auto'>

      <div className="flex items-center flex-col gap-2">
        <div className=' bg-blue-200 min-h-[140px] w-1/3 p-6'>
          <User />
        </div>
        <p className='font-bold text-2xl'>{aluno?.nome}</p>
        <small>{aluno?.codigo}</small>

        <div className='flex flex-col gap-2'>
          <h1>Atualizar tipo do aluno</h1>
          <Select onValueChange={(e)=> setTipo(e)}>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Tipo Alunos" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="1">Aluno</SelectItem>
              <SelectItem value="2">Professor</SelectItem>
              <SelectItem value="3">Diretor</SelectItem>
            </SelectContent>
          </Select>
          <Button onClick={setNewTipo}> Atualizar tipo </Button>
        </div>
      </div>
    </div>
  )
}
