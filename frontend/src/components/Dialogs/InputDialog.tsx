import { Input } from "../ui/input";
import { Label } from "../ui/label";
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


export const InputDialog = () => {

    return (
        <Dialog>
            <DialogTrigger> Registar</DialogTrigger>
            <DialogContent className='px-10 max-w-[320px] rounded-xl'>
                <DialogHeader>
                    <DialogTitle> Tela de Registro </DialogTitle>
                    <DialogDescription>
                        
                        <div className="flex flex-col gap-4">
                            <div className="flex items-start flex-col gap-2">
                                <Label htmlFor="text"> Nome </Label>
                                <Input type="text" placeholder="Digite seu nome ..."/>
                            </div>
                            

                            <div className="flex items-start flex-col gap-2">
                                <Label htmlFor="text"> Carregar Fotos</Label>
                                <CameraDialog
                                    trigerTitle='Regsitrar'
                                />
                            </div>
                        </div>
                    </DialogDescription>
                </DialogHeader>
                <DialogFooter>
                        
                </DialogFooter>    
            </DialogContent>
        </Dialog>
    )
}