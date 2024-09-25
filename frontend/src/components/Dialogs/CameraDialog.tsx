import { useEffect, useRef } from "react";
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

interface CameraDialogProps {
  trigerTitle: string;
  onCaptureImages?: (images: string[]) => void;
}

export const CameraDialog = ({ trigerTitle, onCaptureImages }: CameraDialogProps) => {
 
  const webcamRef = useRef<Webcam>(null);
  const videoConstraints = { facingMode: "user" };
  let onCaptureImagesR: boolean = onCaptureImages ? true : false;

  const apiCall: makeRequestProps = {
    method: 'GET',
    path: 'autenticacao',
    subpath: 'autenticar-usuario',
    urlParams: [],
  }
  
  const {authenticating, getPhotos, arrayImagens} = CameraHook({ webcamRef, apiCall, onCaptureImagesR});
  
  
  useEffect(() => {
    if (onCaptureImages) {
      onCaptureImages(arrayImagens)
    }
    
  }, [arrayImagens, onCaptureImages]);
  
  
  const statusButton: { [key: string]: boolean } = {
    'Autenticando': authenticating,
    'Iniciar': !authenticating,
  }

  const statusTitle: { [key: string]: boolean } = {
    'Prepara-se para a autenticação': !authenticating,
    'Autenticando': authenticating,
  };

  return (
    <Dialog >
      <DialogTrigger className="bg-slate-900 text-white p-2 rounded font-bold">{trigerTitle}</DialogTrigger>
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
          </DialogDescription>
        </DialogHeader>
        <DialogFooter className='flex items-center justify-center '>
          <Button
            className='bg-gray-800 w-fit'
            onClick={()=> getPhotos()}
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