import { Button } from "../ui/button"
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "../ui/dialog"
import { Input } from "../ui/input"
import { Label } from "../ui/label"
import { useState } from "react"
import { CameraDialog } from "./CameraDialog"

export const RaDialog = () => {

    const [codAluno, setCodAluno] = useState<string>('')

    return (

        <Dialog>
            <DialogTrigger asChild className="bg-slate-900 text-white p-2 rounded font-bold">
                <Button variant="outline">Login</Button>
            </DialogTrigger>
            <DialogContent className="px-10 max-w-[420px] p-8 rounded-lg">
                <DialogHeader>
                    <DialogTitle>Login</DialogTitle>
                    <DialogDescription>
                    </DialogDescription>
                </DialogHeader>
                <div className="grid gap-4 py-4">
                    <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="name" className="text-center">
                            Código de Usuário
                        </Label>
                        <Input id="name" onChange={(e)=> setCodAluno(e.target.value)} className="col-span-3" />
                    </div>
                </div>
                <DialogFooter className="m-auto">
                    <CameraDialog
                        trigerTitle='Iniciar Biometria'
                        codAluno={codAluno}
                    />
                </DialogFooter>
            </DialogContent>
        </Dialog>
    )
}


