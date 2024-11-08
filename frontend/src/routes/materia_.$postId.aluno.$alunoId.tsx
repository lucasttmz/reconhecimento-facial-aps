import { User } from 'lucide-react'
import { apiService } from '../api/api'
import { useEffect, useState } from 'react'
import { useUserStore } from '../store/user'
import { Input } from '../components/ui/input'
import { Label } from '../components/ui/label'
import { ImateriaAluno } from '../const/Users.const'
import { createFileRoute } from '@tanstack/react-router'
import { AlunoMateriaDialog } from '../components/Dialogs/AlunoMateriaDialog'


export const Route = createFileRoute('/materia/$postId/aluno/$alunoId')({
    component: MateriaAluno,
})

function MateriaAluno() {

    const { postId, alunoId } = Route.useParams()
    const [alunoNotas, setAlunoNotas] = useState<ImateriaAluno>()
    const { states: { user } } = useUserStore()


    const getAlunoNotas = async () => {   // Chamada da API

        const data = await apiService().makeRequest({
            method: 'GET',
            path: `materias`,
            subpath: `${postId}/aluno/${alunoId}`
        })
        setAlunoNotas(data)
    }

    const atualizarNotas = (atualizar: boolean) => { // Função passada para o componente Filho para chamar novamente a API 
        if (atualizar) { getAlunoNotas() }
    }

    useEffect(() => {
        getAlunoNotas()
    }, [])


    return (

        <div>
            <div
                className='flex items-center min-h-[420px] flex-col p-2 gap-3 border border-solid rounded-xl m-10 shadow-lg'
            >
                <div className='flex justify-center h-full flex-col items-center gap-2'>

                    <div className=' min-h-[150px] w-full flex justify-around gap-1 p-4'> {/* Dados Aluno */}

                        <div className='flex p-2 justify-center flex-col items-center'> {/* Informações aluno */}
                            <User />
                            <div className='text-center'>
                                <p className='font-bold m-0'>{alunoNotas?.aluno.nome.toUpperCase()}</p>
                                <small className='m-0'>{alunoNotas?.aluno.codigo}</small>
                            </div>
                        </div>

                        <div className='p-2 flex flex-col gap-3 justify-center'>
                            <div className='flex justify-center items-center gap-2'>
                                <div className=' w-16 h-16 flex flex-col items-center rounded-md'>
                                    <p className='font-bold'>Notas</p>
                                    {
                                        alunoNotas?.nota == undefined ?
                                            <p className='font-bold'> N/L </p> :
                                            <p className={alunoNotas.nota >= 7 ? 'font-bold text-green-500 text-3xl' : 'font-bold text-red-500 text-3xl'}>
                                                {alunoNotas?.nota}
                                            </p>
                                    }
                                </div>
                                <div className='w-16 h-16 flex flex-col items-center rounded-md ' >
                                    <p className='font-bold'> Faltas </p>
                                    {
                                        alunoNotas?.faltas == undefined ?
                                            <p className='font-bold'> N/L </p> :
                                            <p className={alunoNotas?.faltas <= 3 ? 'font-bold text-green-500 text-3xl' : 'font-bold text-red-500 text-3xl'}>
                                                {alunoNotas?.faltas}
                                            </p>
                                    }
                                </div>
                            </div>
                            {
                                user?.permissions == 2 && ( // Verifica O acesso de professor para lançar Notas
                                    <AlunoMateriaDialog 
                                        notaFaltaAtual={{falta: alunoNotas?.faltas,nota: alunoNotas?.nota}} 
                                        ataulizarNotas={atualizarNotas} 
                                        postId={parseInt(postId)} 
                                        alunoId={parseInt(alunoId)} 
                                    />
                                )
                            }
                        </div>
                    </div>
                    <div className='w-full '> {/*Dados Materia*/}
                        <div className='p-3'>
                            <div>
                                <Label>Matéria</Label>
                                <Input className='bg-white' value={alunoNotas?.materia.nome} />
                            </div>

                            <div className='flex gap-2'>
                                <div>
                                    <Label>Professor</Label>
                                    <Input className='bg-white' value={alunoNotas?.materia.professor} />
                                </div>
                                <div>
                                    <Label>Data Final</Label>
                                    <Input className='bg-white' value={alunoNotas?.materia.data_fim.split('-').reverse().join('/')} />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    )
}