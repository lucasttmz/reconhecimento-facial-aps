import { useCallback, useEffect, useRef, useState } from "react";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/dialog";
import Webcam from "react-webcam";
import { Button } from "../ui/button";
import { Disc, LoaderCircle } from "lucide-react";
import { CameraHook } from "../../hooks/CameraHook";
import { makeRequestProps } from "../../api/axios";
import { CONST } from "../../const/Index";
import { useNavigate } from "@tanstack/react-router";
import { useUserStore } from "../../store/user";
import { useToast } from "../../hooks/use-toast";

interface CameraDialogProps {
  trigerTitle: string;
  onCaptureImages?: (images: string[]) => void;
  codAluno: string
}

export const CameraDialog = ({ trigerTitle, onCaptureImages, codAluno }: CameraDialogProps) => {
  const navigate = useNavigate({ from: '/' })
  const webcamRef = useRef<Webcam>(null);
  const videoConstraints = { facingMode: "user" };
  const onCaptureImagesR: boolean = onCaptureImages ? true : false;
  const { actions: { addUser } } = useUserStore()
  const { toast } = useToast()
  
  const dataRequest = useCallback(async (codAluno:string) => {
    console.log(codAluno)
    await getPhotos(codAluno);
  }, []);

  

  const apiCall: makeRequestProps = {
    method: CONST.HTTP.POST,
    path: 'login',
  }
  
  const {authenticating, toggleIsAuthenticating, getPhotos, arrayImagens, responseData} = CameraHook({ webcamRef, apiCall, onCaptureImagesR});
  
  
  useEffect(() => {
    if (onCaptureImages) {
      onCaptureImages(arrayImagens)
    }
    
  }, [arrayImagens, onCaptureImages]);

  useEffect(() => {
    if(!responseData) return
    if (responseData?.error as unknown) {
      toggleIsAuthenticating()
      toast({
        title: "Oops...",
        description: 'Algo deu errado',
        variant: "destructive"
      })

      console.log('caiu aqui')
      return;
    }
    
    console.log(responseData)
    const { data } = responseData as { data: { token: string, tipo: string, message: string } };

    if (data.token) {
      localStorage.setItem('token', data.token);

      addUser(data.token)

      navigate({ to: '/home' });
    }
  }, [responseData]);
  
  
  const statusButton: { [key: string]: boolean } = {
    'Autenticando': authenticating,
    'Iniciar': !authenticating,
  }

  const statusTitle: { [key: string]: boolean } = {
    'Prepara-se para a autenticação': !authenticating,
    'Autenticando': authenticating,
  };

  return (
    <Dialog>
      <DialogTrigger 
        className="bg-slate-900 text-white p-2 rounded font-bold"
      >{trigerTitle}
      </DialogTrigger>
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
          <DialogDescription className='relative' style={{transform: 'scaleX(-1)'}}>
            <Webcam
              width={512}
              height={512}
              audio={false}
              ref={webcamRef}
              screenshotFormat="image/jpeg"
              videoConstraints={videoConstraints}
            />
          </DialogDescription>
        </DialogHeader>
        <DialogFooter className='flex items-center justify-center '>
          <Button
            className='bg-gray-800 w-fit'
            onClick={()=> dataRequest(codAluno)}
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

            {!authenticating && (
              <Disc
                size={24}
                className='text-red-800 ml-2'
              />
            )}

            {authenticating && (
              <LoaderCircle
                size={24}
                className='text-white ml-2 animate-spin'
              />
            )}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}