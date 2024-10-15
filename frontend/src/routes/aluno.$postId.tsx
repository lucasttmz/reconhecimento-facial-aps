import { createFileRoute } from '@tanstack/react-router'
import { apiService } from '../api/api'
import { makeRequestProps } from '../api/axios'
import { CONST } from '../const/Index'
import { useEffect, useState } from 'react'
import { LoaderCircle } from 'lucide-react'

export const Route = createFileRoute('/aluno/$postId')({
    component: Aluno,
})

interface Ialuno {
    id_usuario: number,
    codigo: string,
    nome: string,
    tipo: number
}

function Aluno() {

    const { postId } = Route.useParams()

    const apiParams: makeRequestProps = {
        method: CONST.HTTP.GET,
        path: `alunos/${postId}`
    }

    const [aluno, setAluno] = useState<Ialuno>()
    const [carregando, setCarregando] = useState(true)
    
    const getAluno = async () => {
        try {
            const data = await apiService().makeRequest(apiParams)
            console.log(data)
            setAluno(data)
        }
        catch (err) {
        }
        finally {
            setCarregando(false)
        }
    }
    
    useEffect(()=>{
        getAluno()
    },[])

    return (
        <div>
            {
                carregando ? 
                
                    <LoaderCircle
                        size={24}
                        className='text-white ml-2 animate-spin'
                    /> 
                :

                <div className='flex justify-center aling-center'> 
                    {aluno?.nome}
                </div>
        
            }     
        </div>
    )
}