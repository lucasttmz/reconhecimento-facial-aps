from os import environ
from random import randint
from typing import Annotated, Any

from fastapi import APIRouter, Depends

from sistema_escolar.controladores.autenticacao import AutenticacaoControle, usuario_autenticado
from sistema_escolar.modelos.autenticacao import LoginSchema, RegistroSchema, Token
from sistema_escolar.modelos.genericos import MensagemSchema


MODO_DEBUG = bool(environ.get("DEBUG", False))

router = APIRouter(tags=["autenticacao"])
T_AutenticacaoControle = Annotated[AutenticacaoControle, Depends(AutenticacaoControle)]
T_Usuario = Annotated[dict[str, Any], Depends(usuario_autenticado)]

@router.post("/login", response_model=Token)
def login(dados: LoginSchema, controle: T_AutenticacaoControle):
    """Realiza login por meio do reconhecimento facial"""

    # Somente durante o desenvolvimento para não precisar do reconhecimento facial
    if MODO_DEBUG:
        permissao = randint(1, 3)
        usuarios = ["Aluno", "Professor", "Diretor"]
        token = controle.criar_token(dados={"sub": usuarios[permissao-1], "user_id":permissao+3, "permissions": permissao})
        return {"token": token, "tipo": "Bearer"}

    return controle.realizar_login(dados.fotos)


@router.post("/registrar", response_model=MensagemSchema)
def registrar(dados: RegistroSchema, controle: T_AutenticacaoControle):
    """Registra um novo usuário"""

    return controle.registrar_usuario(dados)


@router.get("/protegida")
def rota_protegida_testes(usuario: T_Usuario):
    """Testes temporários"""

    return {"message": "Acesso permitido", "usuario": usuario}
