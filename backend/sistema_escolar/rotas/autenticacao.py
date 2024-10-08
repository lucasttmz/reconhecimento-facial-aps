from fastapi import APIRouter

from sistema_escolar.modelos.autenticacao import LoginSchema, RegistroSchema, Token
from sistema_escolar.modelos.genericos import MensagemSchema


router = APIRouter(tags=["autenticacao"])


@router.post("/login", response_model=Token)
def login(fotos: LoginSchema):
    return {"token": "temporario", "tipo": "bearer"}


@router.post("/registrar")
def registrar(dados: RegistroSchema):
    return MensagemSchema(mensagem="Registrado com sucesso!")
