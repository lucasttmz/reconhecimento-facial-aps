import { useEffect, useState } from "react"
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

interface IparamsAlunoMateriaD {
  postId: number,
  alunoId: number
  ataulizarNotas: (atualizar:boolean)=> void
  notaFaltaAtual: {
    nota: number | undefined
    falta: number | undefined
  }
}
export function AlunoMateriaDialog({ postId, alunoId, ataulizarNotas, notaFaltaAtual }: IparamsAlunoMateriaD) {

  const [notasFaltas, setNotasFaltas] = useState({
    faltas: notaFaltaAtual.falta,
    nota: notaFaltaAtual.nota,
  })

  const postNotasFaltas = async () => {

    try {

      const data = await apiService().makeRequest({
        method: CONST.HTTP.PUT,
        path: `materias`,
        subpath: `${postId}/aluno/${alunoId}`,
        body: {
          faltas: notasFaltas.faltas,
          nota: notasFaltas.nota
        }
      })

      toast({
        title: 'Nota e Falta Lançadas',
        description: data.data.mensagem
      })
      ataulizarNotas(true)

    } catch (error:any) {

      toast({
        title: 'Erro ao lançar nota e falta',
        description: error?.response.data.detail[0].msg,
        variant: "destructive",
        duration: 10000
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
            <Label htmlFor="Nota">
              Nota
            </Label>
            <Input onChange={(e) => setNotasFaltas({ ...notasFaltas, ['nota']: parseInt(e.target.value) })} type="number" />

          </div>
          <div >
            <Label htmlFor="Faltas">
              Faltas
            </Label>
            <Input onChange={(e) => setNotasFaltas({ ...notasFaltas, ['faltas']: parseInt(e.target.value) })} type="number" />

          </div>
        </div>


        <DialogFooter>
          <DialogClose asChild>
            <Button type="button" onClick={postNotasFaltas} variant="secondary"> Lançar </Button>
          </DialogClose>
        </DialogFooter>

      </DialogContent>
    </Dialog>
  )
}
