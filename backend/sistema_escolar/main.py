from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sistema_escolar.rotas import boletim, materias, usuarios, autenticacao

load_dotenv()

app = FastAPI(title="Sistema Escolar")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(autenticacao.router)
app.include_router(usuarios.router)
app.include_router(materias.router)
app.include_router(boletim.router)
