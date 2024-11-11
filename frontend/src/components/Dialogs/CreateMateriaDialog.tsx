import { Button } from "../ui/button"
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "../ui/dialog"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "../ui/select"
import { Input } from "../ui/input"
import { Label } from "../ui/label"
import { apiService } from "../../api/api"
import { CONST } from "../../const/Index"
import {useState } from "react"
import { AlunosDialog } from "./AlunosDialog"
import { Iprofessor } from "../../const/Users.const"
import { DialogClose } from "@radix-ui/react-dialog"
import { toast } from "../../hooks/use-toast"

interface paramsPost {
    nome: string,
    codigo_professor: number,
    data_inicio: string,
    data_fim: string,
    codigo_alunos: number[]
}
interface listAlunos {
    alunos: string[]
}
interface ICreateMateriaDialog{
    AtualizarMaterias: (atualizar: boolean)=> void
}
export const CreateMateriaDialog = ({AtualizarMaterias}:ICreateMateriaDialog) => {

    const [prefessores, setProfessores] = useState<Iprofessor[]>([])
    const [params, setParams] = useState<paramsPost>({
        nome: "",
        codigo_professor: 0,
        data_inicio: "",
        data_fim: "",
        codigo_alunos: []

    })

    const atualizarEstadoPai = (novoValor: listAlunos) => {
        setParams((prevParams) => ({
            ...prevParams,
            codigo_alunos: novoValor.alunos.map(Number)
        }));
    };

    const getAllPreofessores = async () => {

        const data = await apiService().makeRequest({
            method: CONST.HTTP.GET,
            path: 'professores'
        })

        setProfessores(data)
    }
    const setInputValue = (e: any, inputName: string) => {

        if (inputName == "codigo_professor") {
            setParams({
                ...params,
                [inputName]: parseInt(e),
            })
        }
        else {
            setParams({
                ...params,
                [inputName]: e.target.value,
            })
        }

    }
    const postNewMateria = async () => {

        try {
            
            const data = await apiService().makeRequest({
                method: CONST.HTTP.POST,
                path: 'materias',
                body: params
            })
            
            if (data.status == 200) {
                toast({
                  title: data.data.mensagem,
                })
            }

            AtualizarMaterias(true)

        } catch (error:any) {

            toast({
                title: "Opss...",
                description: error?.response.data.detail[0].msg,
                variant: "destructive"
              })
        }
        
        
    }

    return (
        <Dialog>
            <DialogTrigger asChild>
                <Button variant="outline" onClick={getAllPreofessores}>Adicionar Materia</Button>
            </DialogTrigger>
            <DialogContent className="px-10 max-w-[320px] pl-3 pr-3 rounded">
                <DialogHeader>
                    <DialogTitle>Criar Materia</DialogTitle>
                    <DialogDescription></DialogDescription>
                </DialogHeader>
                <div className="grid gap-1 py-4">
                    <div className="">
                        <Label htmlFor="name" className="text-right">
                            Nome Matéria
                        </Label>
                        <Input onChange={(e) => setInputValue(e, "nome")} className="col-span-3" />
                    </div>
                    <div className="">
                        <Label htmlFor="cod-professor" className="text-right">
                            Nome Professor
                        </Label>
                        <Select onValueChange={(e) => setInputValue(e, "codigo_professor")}>
                            <SelectTrigger className="w-full" >
                                <SelectValue placeholder="Professores" />
                            </SelectTrigger>
                            <SelectContent >
                                {
                                    prefessores.map((professor) => (
                                        <SelectItem key={professor.id_usuario} value={professor.id_usuario.toString()}>{professor.nome}</SelectItem>
                                    ))
                                }
                            </SelectContent>
                        </Select>
                    </div>
                    <div className="">
                        <Label htmlFor="date-start" className="text-right">
                            Data Inicio
                        </Label>
                        <Input type="date" onChange={(e) => setInputValue(e, "data_inicio")} className="col-span-3" />
                    </div>
                    <div className="">
                        <Label htmlFor="date-end" className="text-right">
                            Data Fim
                        </Label>
                        <Input type="date" onChange={(e) => setInputValue(e, "data_fim")} className="col-span-3" />
                    </div>
                    <div>
                        <Label htmlFor="alunos" className="text-right">
                            Alunos
                        </Label>
                        <AlunosDialog atualizarEstado={atualizarEstadoPai} />
                    </div>
                </div>
                <DialogFooter>
                    <DialogClose>
                        <Button type="submit" onClick={postNewMateria}> Adicionar Materia</Button>
                    </DialogClose>
                </DialogFooter>
            </DialogContent>
        </Dialog>

    )
}