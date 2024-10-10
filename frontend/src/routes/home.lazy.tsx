import { createLazyFileRoute, useNavigate } from '@tanstack/react-router'
import { useUserStore } from '../store/user'
import { CONST } from '../const/Index';
import { Button } from '../components/ui/button';

export const Route = createLazyFileRoute('/home')({
  component: Home,
})

function Home() {
  const navigate = useNavigate({ from: '/home' })
  const { states: { user }, actions: { removeUser } } = useUserStore();
  const roleUser = CONST.PERMISSIONS[user?.permissions as keyof typeof CONST.PERMISSIONS]
  const permissions = CONST.PERMISSIONS_ACTIONS[roleUser as keyof typeof CONST.PERMISSIONS_ACTIONS]

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
      
      <div 
        className='flex flex-col gap-4 w-full'
      >
        <p> 
          Olá, {user?.sub}!
        </p>

        <p>
          Vocé é um {roleUser}!
        </p>

        <pre>
          { JSON.stringify(permissions, null, 2) }
        </pre>

        <Button onClick={test}>
          Deslogar
        </Button>
      </div>
    </section>
  )
}
