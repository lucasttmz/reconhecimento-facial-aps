from fastapi import FastAPI

from sistema_escolar.controllers import AlunoRouter, MateriaRouter


app = FastAPI(title="Sistema Escolar")
app.include_router(AlunoRouter)
app.include_router(MateriaRouter)

