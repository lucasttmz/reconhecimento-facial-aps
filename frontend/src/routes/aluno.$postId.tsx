import { createFileRoute } from '@tanstack/react-router'
import { apiService } from '../api/api'
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
import { Ialuno } from '../const/Users.const'
import { useUserStore } from '../store/user'


export const Route = createFileRoute('/aluno/$postId')({
    component: Aluno,
})


function Aluno() {
    const { postId } = Route.useParams()
    const [aluno, setAluno] = useState<Ialuno>()
    const [tipo, setTipo] = useState('')
    const { states: { user } } = useUserStore()


    const setAlunoTipo = async () => {

        try {
            const data = await apiService().makeRequest({
                method: CONST.HTTP.PUT,
                path: 'usuarios',
                subpath: `${aluno?.id_usuario}`,
                body: {
                    tipo: parseInt(tipo)
                }
            })
            toast({
                title: 'Usuario Atualizado',
                description: data.data.mensagem
            })
        } catch (error: any) {
            toast({
                title: 'Erro ao Atualizar tipo',
                description: error?.response.data.detail[0].msg,
                variant: "destructive"
            })
        }



    }
    const getAluno = async () => {
        try {
            const data = await apiService().makeRequest({
                method: CONST.HTTP.GET,
                path: `alunos/${postId}`,
            }
            )
            console.log(data)
            setAluno(data)

        } catch (err) {

        }
    }

    useEffect(() => {
        getAluno()
    }, [])

    return (
        <div className='flex items-center flex-col'>

            <div
                className=" w-1/2 p-4 rounded-2xl text-white text-center shadow-lg border-2"
            >{/*bg-gradient-to-r from-cyan-200 to-blue-300  bg-opacity-15 */}
                <div
                    className='shadow-lg border-2 rounded-sm m-auto min-h-[140px] w-1/2 p-6 flex items-center justify-center lg:max-w-32'
                >{/*bg-gradient-to-r from-cyan-100 to-blue-200 */}
                    <User color='black' />
                </div>

                <p className='mt-2 font-bold text-2xl text-black'>{aluno?.nome}</p>
                <small className='text-black'>{aluno?.codigo}</small>

                {
                    user?.permissions == 3 && (
                        <div className='flex items-center flex-col gap-2 text-black'>
                            <h1>Atualizar tipo do aluno</h1>
                            <Select onValueChange={(e) => setTipo(e)}>
                                <SelectTrigger className="max-w-[180px]">
                                    <SelectValue placeholder="Tipo Alunos" />
                                </SelectTrigger>
                                <SelectContent>
                                    <SelectItem value="1">Aluno</SelectItem>
                                    <SelectItem value="2">Professor</SelectItem>
                                    <SelectItem value="3">Diretor</SelectItem>
                                </SelectContent>
                            </Select>
                            <Button onClick={setAlunoTipo}> Atualizar tipo </Button>
                        </div>
                    )
                }
            </div>
        </div>
    )
}
