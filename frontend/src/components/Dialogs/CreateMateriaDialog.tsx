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
import { useNavigate } from "@tanstack/react-router"
import { api, makeRequestProps } from "../../api/axios"
import { apiService } from "../../api/api"
import { CONST } from "../../const/Index"
import { useEffect, useState } from "react"
import { AlunosDialog } from "./AlunosDialog"

interface paramsPost {
    nome: string,
    codigo_professor: number,
    data_inicio: string,
    data_fim: string,
}
interface Professor {
    id_usuario: number,
    codigo: string,
    nome: string,
    tipo: number
}
export const CreateMateriaDialog = () => {

    const navigate = useNavigate({ from: '/materias' })
    const [params, setParams] = useState<paramsPost>({
        nome: "",
        codigo_professor: 0,
        data_inicio: "",
        data_fim: "",

    })
    const [prefessores, setProfessores] = useState<Professor[]>([])

    const getAllPreofessores = async () => {

        const data = await apiService().makeRequest({
            method: CONST.HTTP.GET,
            path: 'professores'
        })

        setProfessores(data)
    }

    const apiParams: makeRequestProps = {

        method: CONST.HTTP.POST,
        path: 'materias',
        body: params
    }
    const setInputValue = (e: any, inputName: string) => {
        setParams({
            ...params,
            [inputName]: e.target.value,
        })
    }
    const apicall = async () => {

        const data = await apiService().makeRequest(apiParams)

        console.log(data)
        navigate({ to: '/materias' })
    }

    const getDateFomat = (): string => {

        const TodayDate = new Date()

        return `${TodayDate.getFullYear()}-${TodayDate.getMonth()}-${TodayDate.getDate()}}`

    }

    return (
        <Dialog>
            <DialogTrigger asChild>
                <Button variant="outline" onClick={async () => await getAllPreofessores()}>Adicionar Materia</Button>
            </DialogTrigger>
            <DialogContent className="px-10 max-w-[320px] pl-3 pr-3 rounded">
                <DialogHeader>
                    <DialogTitle>Criar Materia</DialogTitle>
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
                        <Select>
                            <SelectTrigger className="w-full">
                                <SelectValue placeholder="Professores" />
                            </SelectTrigger>
                            <SelectContent>

                                {
                                    prefessores.map((professor) => (
                                        <SelectItem value={professor.id_usuario.toString()}>{professor.nome}</SelectItem>
                                    ))
                                }
                            </SelectContent>
                        </Select>

                        {/* <Input onChange={(e) => setInputValue(e, "codigo_professor")} className="col-span-3" /> */}
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
                        <AlunosDialog />
                    </div>
                </div>
                <DialogFooter>
                    <Button type="submit" onClick={() => apicall()}> Adicionar Materia</Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>

    )
}