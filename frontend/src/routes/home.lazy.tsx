import { createLazyFileRoute, Link, useNavigate } from '@tanstack/react-router'
import { useUserStore } from '../store/user'
import { CONST } from '../const/Index';
import { Button } from '../components/ui/button';
import { ButtonMenu } from '../components/ButtonMenu';
import { Book, GraduationCap, User, BookOpen } from "lucide-react"

export const Route = createLazyFileRoute('/home')({
  component: Home,
})

function Home() {
  const navigate = useNavigate({ from: '/home' })
  const { states: { user }, actions: { removeUser } } = useUserStore();
  const roleUser = CONST.PERMISSIONS[user?.permissions as keyof typeof CONST.PERMISSIONS]

  const test = () => {
    localStorage.removeItem('token')
    removeUser()
    navigate({ to: '/' });
  }

  return (
    <section
      className="h-[calc(100vh-120px)] flex flex-col items-start gap-2 justify-start px-8"
    >
      <h3
        className='font-bold text-1xl text-gray-800'
      >
        Bem vindo a página home!
      </h3>

      <div className='flex flex-col gap-4 w-full'>
        <p> Olá, {user?.sub}! </p>

        <p> Vocé é um {roleUser}! </p>

        <div className='w-full'>

          {

            user?.permissions == 1 && (
              <div className=''>
                <ButtonMenu nome='Boletim' Icone={() => <BookOpen color='#fff' />} rota='boletim' />
              </div>

            )
          }
          {
            user?.permissions == 2 && (

              <div className='lg:flex'>
                <ButtonMenu nome='Matéria' Icone={() => <Book color='#fff' />} rota='materias' />
                <ButtonMenu nome='Alunos' Icone={() => <GraduationCap color='#fff' />} rota='alunos' />
              </div>

            )
          }
          {
            user?.permissions == 3 && (

              <div className='lg:flex gap-2'>
                <ButtonMenu nome='Matéria' Icone={() => <Book color='#fff' />} rota='materias' />
                <ButtonMenu nome='Alunos' Icone={() => <GraduationCap color='#fff' />} rota='alunos' />
                <ButtonMenu nome='Professores' Icone={() => <User color='#fff' />} rota='professores' />
              </div>
            )
          }

        </div>

        <Button onClick={test}>
          Deslogar
        </Button>
      </div>
    </section>
  )
}
