import { Link, Outlet, useNavigate } from "@tanstack/react-router";
import { useUserStore } from "../../store/user";
import Logo from '../../assets/images/logo.png'
import { useEffect } from "react";
import { Toaster } from "../ui/toaster"

export const RootPage: React.FC = () => {
  const navigate = useNavigate({ from: '/' })
  const { actions: { addUser, removeUser } } = useUserStore()

  useEffect(() => {
    if (localStorage.getItem('token')) {
      addUser(localStorage.getItem('token') as string)

      navigate({ to: '/home' });

      return
    }

    navigate({ to: '/' })
  }, [addUser, removeUser])

  return (
    <main className="w-full min-h-screen bg-gray-100">
      <Link to="/home">
        <img
          src={Logo}
          alt="logo"
          className="w-2/4 mx-auto"
        />
      </Link>

      <Outlet />
      <Toaster />
    </main>

  );
}