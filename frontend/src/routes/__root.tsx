import { createRootRoute, redirect } from "@tanstack/react-router";
import { RootPage } from "../components/page/RootPage";
import { CONST } from '../const/Index'
import { useUserStore } from "../store/user";
import { jwtDecode } from "jwt-decode";


export const Route = createRootRoute({
    component: () => (
        <RootPage />
    ),

    // beforeLoad: async ({ location }) => { NÃO USEE ISSO ☣️

    //     const token = localStorage.getItem('token')
    //     const pathName = window.location.pathname.replace('/', '')
    //     console.log(pathName);
    //     console.log(location)

    //     if (token) {
    //         const User = jwtDecode(token)

    //         console.log(CONST.PERMISSIONS_ACTIONS.some((permission) => {
    //             console.log("Essas sao as permisoess = ", JSON.stringify(permission))
    //             return !(permission.permissionId == User?.permissions && permission.permissionRoutes.includes(pathName))
    //         }))


    //         if (CONST.PERMISSIONS_ACTIONS.some((permission) => {
    //             return !(permission.permissionId == User?.permissions && permission.permissionRoutes.includes(pathName))
    //         })) {
    //             console.log('redirecionou')
    //             // throw redirect({
    //             //     to: '/home',
    //             // })
    //         }
    //     }
    //     //     permissions.some((permission) => {
    //     //     return !(permission.permissionId == user?.permissions && permission.permissionRoutes.includes(pathName))
    //     //   })) navigate({ to: '/home' });
    // },




});