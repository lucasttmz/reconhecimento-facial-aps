from fastapi import FastAPI

from sistema_escolar.controladores import boletim, materias, usuarios


app = FastAPI(title="Sistema Escolar")
app.include_router(usuarios.router)
app.include_router(materias.router)
app.include_router(boletim.router)
