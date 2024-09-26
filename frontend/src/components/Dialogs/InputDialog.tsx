import { Input } from "../ui/input";
import { Label } from "../ui/label";
import { Button } from "../ui/button";
import { Check } from "lucide-react"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/dialog"
import { CameraDialog } from "./CameraDialog";
import { useState } from "react";
import { Link } from "@tanstack/react-router";
import { api,makeRequestProps } from "../../api/axios";
import { apiService } from "../../api/api";
interface paramsPost {
  nome: string,
  sobrenome: string,
  fotos: string[]
}

export const InputDialog = () => {

  const [capturedImages, setCapturedImages] = useState<string[]>([]);
  const [buttonDisabled, setButtonDisabled] = useState<boolean>(true)
  const [params, setParams] = useState<paramsPost>({
    nome: '',
    sobrenome: '',
    fotos: []
  }) 
  const apiCall:makeRequestProps = {
    path: "/registrar",
    method: "POST",
    params: {
      nome: `${params.nome} ${params.sobrenome}`,
      fotos: capturedImages
    }
  }
  const handleCapturedImages = (images: string[]) => {
    
    if (images.length == 10) {

      if(params.nome != "" && params.sobrenome != ""){
        setButtonDisabled(false)
      }

      setParams({
        ...params,
        fotos: capturedImages
      })
    }
    setCapturedImages(images);
  };

  const setInputValue = (e:any, inputName:string)=>{

    setParams({
      ...params,
      [inputName]: e.target.value,
    })

    if(params.nome != "" && params.sobrenome != "" && capturedImages.length == 10){
      setButtonDisabled(false)
    }
  
  }
  const apiPostService = async ()=>{

    const data = await apiService().makeRequest(apiCall)
    console.log(data)
  }

  return (
    <Dialog>
      <DialogTrigger> Registar</DialogTrigger>
      <DialogContent className='px-10 max-w-[320px] rounded-xl'>
        <DialogHeader>
          <DialogTitle className="p-4"> Tela de Registro </DialogTitle>
          <DialogDescription>

            <div className="flex flex-col gap-4">
              <div className="flex items-start flex-col gap-2">
                <Label htmlFor="text"> Primeiro Nome </Label>
                <Input type="text" placeholder="Nome" onChange={(e)=>setInputValue(e,"nome")} />
              </div>
              
              <div className="flex items-start flex-col gap-2">
                <Label htmlFor="text"> Sobrenome </Label>
                <Input type="text" placeholder="Sobrenome" onChange={(e)=>setInputValue(e,"sobrenome")}/>
              </div>

              <div className="flex items-start flex-col gap-2">
                <Label htmlFor="text"> Carregar Fotos</Label>
                <div className="flex justify-center items-center gap-2">
                  <CameraDialog
                    onCaptureImages={handleCapturedImages}
                    trigerTitle='Cadastrar Rosto'
                  />
                  {
                    capturedImages.length == 10 && (
                      <Check
                        absoluteStrokeWidth
                        size={15}
                        className="text-green-500"
                      />
                    )
                  }
                </div>
              </div>
            </div>
          </DialogDescription>
        </DialogHeader>
        <DialogFooter className="flex flex-col">
          <Button type="submit" disabled={buttonDisabled} onClick={apiPostService}>
            <Link to="/" >Enviar</Link>
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}

/*
<div>
  {capturedImages.length > 0 && (
    <div className="mt-4">
      <h4>Imagens Capturadas:</h4>
      <div className="flex flex-wrap gap-4 w-full">
        {capturedImages.map((image, index) => (
          <img
            key={index}
            src={image}
            alt={`captured-${index}`}
            width={70}
            height={70}
            className="mt-2"
          />
        ))}
      </div>
    </div>
  )}
</div>
*/