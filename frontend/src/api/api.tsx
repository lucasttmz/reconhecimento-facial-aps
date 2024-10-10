import { api } from "./axios";

export const apiService = () => {
    const apiInstace = new api();

    return apiInstace;
};