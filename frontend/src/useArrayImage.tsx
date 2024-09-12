import { create } from "zustand";

type Arraylmages = { 
    imagens: string[]; 
    adicionarImagem: (novaImagem: string) => void; 
    removerImagem: (indexImagem:number) => void;
} 

export const useArrayImages = create<Arraylmages>((set)=> ({
    imagens: [],
    adicionarImagem: (novaImagem) => (set((state)=> ({imagens: [...state.imagens, novaImagem]}))),
    removerImagem: (indexImagem) => (set((state)=> ({imagens: state.imagens.filter((_,index)=> index !== indexImagem)})))
}));