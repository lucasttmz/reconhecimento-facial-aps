import { createFileRoute } from '@tanstack/react-router'
import { apiService } from '../api/api'
import { CONST } from '../const/Index'
import { useEffect, useState } from 'react'
import { ImateriaNota } from '../const/Users.const'

export const Route = createFileRoute('/boletim/$materiaId')({
    component: BoletimMateria
})

function BoletimMateria() {

    const params = Route.useParams()
    const [MateriaInfo, setMateriaInfo] = useState<ImateriaNota>()

    const getNotaFaltaMateria = async () => {
        try {

            const response = await apiService().makeRequest({
                method: CONST.HTTP.GET,
                path: `/boletim/${params.materiaId}`
            })
            setMateriaInfo(response)
        } catch (error) {

        }
    }
    useEffect(() => {
        getNotaFaltaMateria()
    }, [])

    

    return (
        <div className='flex flex-col gap-3 m-4 p-2 shadow-lg shadow-slate-800 rounded-lg'>
            
            <div className='flex flex-col lg:text-2xl lg:m-10'>
                <p className='font-bold'>
                    Matéria: {MateriaInfo?.materia.nome}
                </p>
                <p>Professor: {MateriaInfo?.materia.professor}</p>
                <p>Data de Inicio: {MateriaInfo?.materia.data_inicio.split('-').reverse().join("/")}</p>
                <p>Data de Encerramento: {MateriaInfo?.materia.data_fim.split('-').reverse().join("/")}</p>
            </div>

            <div className='flex justify-center lg:text-2xl'>
                <div className='m-auto'> 
                    <p className='font-bold'>Notas</p>
                    <p className='text-center'>{MateriaInfo?.nota}</p>
                </div>
                <div className='m-auto'> 
                    <p className='font-bold'>Faltas</p>
                    <p className='text-center'>{MateriaInfo?.faltas}</p>
                </div>
            </div>
        
        
        </div>
    )
}