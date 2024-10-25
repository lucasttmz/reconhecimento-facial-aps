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
import { makeRequestProps } from "../../api/axios";
import { apiService } from "../../api/api";
import { useToast } from "../../hooks/use-toast";
import { DialogClose } from "@radix-ui/react-dialog";
interface paramsPost {
  nome: string,
  sobrenome: string,
  fotos: string[]
}

export const InputDialog = () => {
  const { toast } = useToast()
  const [capturedImages, setCapturedImages] = useState<string[]>([]);
  const [buttonDisabled, setButtonDisabled] = useState<boolean>(true)
  const [params, setParams] = useState<paramsPost>({
    nome: '',
    sobrenome: '',
    fotos: []
  })
  const apiCall: makeRequestProps = {
    path: "registrar",
    method: "POST",
    body: {
      nome: `${params.nome} ${params.sobrenome}`,
      fotos: capturedImages
    }
  }
  const handleCapturedImages = (images: string[]) => {

    if (images.length == 10) {

      if (params.nome != "" && params.sobrenome != "") {
        setButtonDisabled(false)
      }

      setParams({
        ...params,
        fotos: capturedImages
      })
    }
    setCapturedImages(images);
  };

  const setInputValue = (e: any, inputName: string) => {

    if (inputName == 'nome' || inputName == 'sobrenome') {

      let inputValue: string = e.target.value
      inputValue = inputValue.replace(inputValue[0], inputValue[0].toUpperCase())

      setParams({
        ...params,
        [inputName]: inputValue,
      })
    }
    else {
      setParams({
        ...params,
        [inputName]: e.target.value,
      })
    }



    if (params.nome != "" && params.sobrenome != "" && capturedImages.length == 10) {
      setButtonDisabled(false)
    }

  }
  const apiPostService = async () => {

    const data = await apiService().makeRequest(apiCall)
    if (data.status == 200) {
      console.log(data)
      toast({
        title: `Bem vindo ${data.data.nome}!, Esse é o seu codigo de Usuário ${data.data.codigo}`,
        description: 'Tudo certo para fazer login',
        duration: 15000
      })
    }
    else {
      toast({
        title: "Opss...",
        description: 'Algo deu errado',
        variant: "destructive"
      })

      return;
    }
  }

  return (
    <Dialog>
      <DialogTrigger className="border border-solid rounded border-black">
        <Button variant={"secondary"} className="hover:bg-gray-800 w-full hover:text-white"> Registrar </Button>
      </DialogTrigger>
      <DialogContent className='px-10 max-w-[320px] rounded-xl'>
        <DialogHeader>
          <DialogTitle className="p-4"> Tela de Registro </DialogTitle>
          <DialogDescription>

            <div className="flex flex-col gap-4">
              <div className="flex items-start flex-col gap-2">
                <Label htmlFor="text"> Primeiro Nome </Label>
                <Input type="text" placeholder="Nome" onChange={(e) => setInputValue(e, "nome")} />
              </div>

              <div className="flex items-start flex-col gap-2">
                <Label htmlFor="text"> Sobrenome </Label>
                <Input type="text" placeholder="Sobrenome" onChange={(e) => setInputValue(e, "sobrenome")} />
              </div>

              <div className="flex items-start flex-col gap-2">
                <Label htmlFor="text"> Carregar Fotos</Label>
                <div className="flex justify-center items-center gap-2">
                  <CameraDialog
                    onCaptureImages={handleCapturedImages}
                    trigerTitle='Cadastrar Rosto'
                    codAluno=""
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
          <DialogClose asChild>
            <Button type="submit" disabled={buttonDisabled} onClick={apiPostService}>
              Enviar Cadastro
            </Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}