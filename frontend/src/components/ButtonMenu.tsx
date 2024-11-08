import { Link } from "@tanstack/react-router"

interface ButtonMenuProps {
    nome: string,
    Icone: React.ComponentType,
    rota: string
}

export const ButtonMenu: React.FC<ButtonMenuProps> = ({ nome, Icone, rota }) => {
    return (
      <div className="w-full h-full mb-2 shadow-md rounded shadow-slate-800 hover:scale-105 ">
        <Link
          to={`/${rota}`}
          className='flex justify-center  items-center w-full h-24 gap-1 bg-bgbutton rounded p-4'
        >
          <Icone/> 
          <p className='text-white'>{nome}</p>
        </Link>
        
      </div>
    );
  };