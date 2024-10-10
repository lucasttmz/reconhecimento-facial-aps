import { Outlet, useNavigate } from "@tanstack/react-router";
import { useUserStore } from "../../store/user";
import Logo from '../../assets/images/logo.png'
import { useEffect } from "react";

export const RootPage: React.FC = () => {
    const navigate = useNavigate({ from: '/' })
    const { actions: { addUser, removeUser } } = useUserStore()

    useEffect(() => {
      if (localStorage.getItem('token')) {
        addUser(localStorage.getItem('token') as string)

        navigate({ to: '/home' });

        return
      }
    }, [addUser, removeUser])

    return (
        <main className="w-full min-h-screen bg-gray-100">
              <img 
                src={Logo} 
                alt="logo"
                className="w-2/4 mx-auto" 
              />
          
            <Outlet/>
        </main>
    );
}