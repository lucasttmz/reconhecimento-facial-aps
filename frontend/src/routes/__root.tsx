import { createRootRoute } from "@tanstack/react-router";
import { RootPage } from "../components/page/RootPage";

export const Route = createRootRoute({
    component: () => (
        <RootPage/>
    ),
});