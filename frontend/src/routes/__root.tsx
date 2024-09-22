import { createRootRoute, Outlet } from "@tanstack/react-router";

export const Route = createRootRoute({
    component: () => (
        <main className="w-full min-h-screen bg-gray-100">
            <p 
              className="text-4xl font-bold text-center text-gray-800 pt-10 tracking-widest"
            >
              UBIB
            </p>
            <Outlet/>
        </main>
    ),
    
});