import { useState } from "react"
import { apiService } from "../../api/api"
import { CONST } from "../../const/Index"
import { Button } from "../ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/dialog"
import { Input } from "../ui/input"
import { Label } from "../ui/label"
import { toast } from "../../hooks/use-toast"
import { useNavigate } from "@tanstack/react-router"

interface Iparams {
  postId: number,
  alunoId: number
}
export function AlunoMateriaDialog({ postId, alunoId }: Iparams) {

  const navigate = useNavigate({ from: '/materia/$postId/aluno/$alunoId' })
  const [notasFaltas, setNotasFaltas] = useState({
    faltas: 0,
    nota: 0,
  })

  const postNotasFaltas = async () => {


    const data = await apiService().makeRequest({
      method: CONST.HTTP.PUT,
      path: `materias`,
      subpath: `${postId}/aluno/${alunoId}`,
      body: {
        faltas: notasFaltas.faltas,
        nota: notasFaltas.nota
      }
    })

    if (data.status == 200) {
      toast({
        title: 'Nota e Falta Lançadas',
        description: data.data.mensagem
      })
    }
    else {
      toast({
        title: 'Erro ao lançar nota e falta',
        description: data.response.data.detail[0].msg,
        variant: "destructive"
      })
    }
    
  }

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline"> Lançar Notas </Button>
      </DialogTrigger>

      <DialogContent className="sm:max-w-md max-w-[320px] rounded-xl">
        <DialogHeader>
          <DialogTitle>Lançar Notas</DialogTitle>
          <DialogDescription>
          </DialogDescription>
        </DialogHeader>

        <div className="flex items-center space-x-2">

          <div >
            <Label htmlFor="nome">
              Nota
            </Label>
            <Input onChange={(e) => setNotasFaltas({ ...notasFaltas, ['nota']: parseInt(e.target.value) })} type="number" />

          </div>
          <div >
            <Label htmlFor="nome">
              Faltas
            </Label>
            <Input onChange={(e) => setNotasFaltas({ ...notasFaltas, ['faltas']: parseInt(e.target.value) })} type="number" />

          </div>
        </div>


        <DialogFooter>
          <DialogClose asChild>
            <Button type="button" onClick={postNotasFaltas} variant="secondary"> Close </Button>
          </DialogClose>
        </DialogFooter>

      </DialogContent>
    </Dialog>
  )
}
