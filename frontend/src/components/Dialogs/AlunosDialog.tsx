import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"

import { Button } from "../ui/button"
import { Checkbox } from "../ui/checkbox"
import { ScrollArea } from "../ui/scroll-area"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "../ui/form"
import { apiService } from "../../api/api"
import { CONST } from "../../const/Index"
import { useEffect, useState } from "react"
import { Ialuno } from "../../const/Users.const"

const FormSchema = z.object({
  alunos: z.array(z.string()).refine((value) => value.some((item) => item), {
    message: "Necessario ter pelo menos um aluno selecionado.",
  }),
})
interface listAlunos {
  alunos: string[]
}
interface FilhoProps {
  atualizarEstado: (novoValor: listAlunos) => void;
}
export function AlunosDialog({ atualizarEstado }:FilhoProps) {

  const [alunos, setAlunos] = useState<Ialuno[]>()

  const getAllAlunos = async () => {
    const data = await apiService().makeRequest({
      method: CONST.HTTP.GET,
      path: 'alunos'
    })

    setAlunos(data)
  }
  
  useEffect(() => {
    getAllAlunos()
  }, [])

  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
    defaultValues: {
      alunos: [],
    },
  })

  function onSubmit(data: z.infer<typeof FormSchema>) {
    atualizarEstado(data)
  }

  return (
    <ScrollArea className="w-full h-[100px] border p-1">
      <Form {...form}>
        <form onChange={form.handleSubmit(onSubmit)} className="space-y-8">
          <FormField
            control={form.control}
            name="alunos"
            render={() => (
              <FormItem>
                {alunos?.map((item) => (
                  <FormField
                    key={item.id_usuario}
                    control={form.control}
                    name="alunos"
                    render={({ field }) => {
                      return (
                        <FormItem
                          key={item.id_usuario}
                          className="flex flex-row items-start space-x-3 space-y-0"
                        >
                          <FormControl>
                            <Checkbox
                              checked={field.value?.includes(item.id_usuario.toString())}

                              onCheckedChange={(checked) => { //Adiciona ou remove os alunos da lista dependendo da seleção
                                return checked
                                  ? field.onChange([...field.value, item.id_usuario.toString()])
                                  : field.onChange(
                                    field.value?.filter(
                                      (value) => value !== item.id_usuario.toString()
                                    )
                                  )
                              }}
                            />
                          </FormControl>
                          <FormLabel className="text-sm font-normal">
                            {item.nome}
                          </FormLabel>
                        </FormItem>
                      )
                    }}
                  />
                ))}
                <FormMessage />
              </FormItem>
            )}
          />
        </form>
      </Form>
    </ScrollArea>
  )
}
