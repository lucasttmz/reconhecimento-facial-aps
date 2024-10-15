import { Link } from "@tanstack/react-router"

interface ButtonMenuProps {
    nome: string,
    Icone: React.ComponentType,
    rota: string
}

export const ButtonMenu: React.FC<ButtonMenuProps> = ({ nome, Icone, rota }) => {
    return (
      <div className="w-full h-full mb-2">
        <Link
          to={`/${rota}`}
          className='flex justify-center flex-col items-center w-full h-24 gap-1 bg-bgbutton rounded p-4'
        >
          <Icone/> 
          <p className='text-white'>{nome}</p>
        </Link>
        
      </div>
    );
  };