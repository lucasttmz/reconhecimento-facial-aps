import { createLazyFileRoute } from '@tanstack/react-router'
import { Button } from '../components/ui/button'

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../components/ui/dialog";
import { useEffect, useRef, useState } from 'react';
import Webcam from 'react-webcam';
import { Disc, LoaderCircle } from 'lucide-react';

export const Route = createLazyFileRoute('/')({
  component: Index,
})

function Index() {
  const webcamRef = useRef<Webcam>(null);
  const [arrayImagens, setArrayImagens] = useState<string[]>([])
  const [counterToPhoto, setCounterToPhoto] = useState<number>(3);
  const [authenticating, setAuthenticating] = useState<boolean>(false);
  const videoConstraints = {facingMode: "user"};

  const statusButton: { [key: string]: boolean } = {
    'Autenticando': authenticating,
    'Iniciar': !authenticating,
  }

  const statusTitle: { [key: string]: boolean } = {
    'Prepara-se para a autenticação': !authenticating,
    'Autenticando': authenticating,
  };

  const initCounter = () => {
    const timeToGetPhoto = 3000
    const timeToUser = timeToGetPhoto / 1000
    const timeForUs = timeToGetPhoto / 10

    setCounterToPhoto(timeToUser)
    setAuthenticating(true)

    const intervalPhoto = setInterval(() => {
      const novaImagem = webcamRef?.current?.getScreenshot();

      if (novaImagem) {
        setArrayImagens((prev) => [...prev, novaImagem])
      }
    }, timeForUs)

    const interval = setInterval(() => {
      setCounterToPhoto((prev) => prev - 1)
    }, 1000)

    setTimeout(() => {
      clearInterval(interval)
      clearInterval(intervalPhoto)
    }, 3000);
  }

  useEffect(() => {
    console.log(arrayImagens)
  }, [arrayImagens])


  return (
    <section 
      className="h-[calc(100vh-120px)] flex flex-col items-center gap-2 justify-center px-8"
    >
      <h3 
        className='font-bold text-1xl text-gray-800'
      >
        Bem vindo a página de login!
      </h3>
      
      <div 
        className='flex flex-col gap-4 w-full'
      >
        <Dialog>
          <DialogTrigger>Entrar</DialogTrigger>
          <DialogContent className='px-10 max-w-[320px] rounded-xl'>
            <DialogHeader> 
                {Object.keys(statusTitle).map((key) => (
                  statusTitle[key] && (
                    <DialogTitle
                      key={key}
                      className='text-gray-800'
                    >
                      {key}
                    </DialogTitle>
                  )
                ))}
              <DialogDescription className='relative'>
                <Webcam
                  width={512}
                  height={512}
                  audio={false}
                  ref={webcamRef}
                  screenshotFormat="image/jpeg"
                  videoConstraints={videoConstraints}
                />

                { authenticating && (
                   <div 
                    className='absolute inset-0'
                    >
                    { counterToPhoto !== 0 && (
                      <p>
                        {counterToPhoto}
                      </p>
                    )}

                    { counterToPhoto === 0 && (
                      <p>
                       Foto tirada
                      </p>
                    )}
                   </div>
                )
                }
              </DialogDescription>
            </DialogHeader>
            <DialogFooter className='flex items-center justify-center'>
              <Button 
                className='bg-gray-800 w-fit'
                onClick={() => initCounter()}
              >
                {Object.keys(statusButton).map((key) => (
                  statusButton[key] && (
                    <span 
                      key={key}
                      className='text-white'
                    >
                      {key}
                    </span>
                  )
                ))}

                {  !authenticating && (
                  <Disc 
                    size={24}
                    className='text-red-800 ml-2'
                  />
                )}

                {  authenticating && (
                  <LoaderCircle 
                    size={24}
                    className='text-white ml-2 animate-spin'
                  />
                )}
              </Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>

        <Button
          variant='default'
          className='text-white outline-none ring-0 focus:ring-0 h-[45px]'
        >
          Registrar-se
        </Button>
      </div>

      
    </section>
  )
}
