import { createLazyFileRoute } from '@tanstack/react-router'

import { CameraDialog } from '../components/Dialogs/CameraDialog';
import { InputDialog } from '../components/Dialogs/InputDialog';

export const Route = createLazyFileRoute('/')({
  component: Index,
})

function Index() {
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
       
          <CameraDialog
            trigerTitle='Login'
          />

        
          <InputDialog/>
        
      </div>
    </section>
  )
}
