from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sistema_escolar.rotas import boletim, materias, usuarios


app = FastAPI(title="Sistema Escolar")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(usuarios.router)
app.include_router(materias.router)
app.include_router(boletim.router)
