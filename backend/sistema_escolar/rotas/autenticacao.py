from os import environ
from random import randint
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException

from sistema_escolar.controladores.autenticacao import AutenticacaoControle, usuario_autenticado
from sistema_escolar.controladores.biometria import BiometriaControle
from sistema_escolar.modelos.autenticacao import LoginSchema, RegistroSchema, Token
from sistema_escolar.modelos.genericos import MensagemSchema


MODO_DEV = environ.get("DEV", "false").lower() in ("true", "1")

router = APIRouter(tags=["autenticacao"])
T_AutenticacaoControle = Annotated[AutenticacaoControle, Depends(AutenticacaoControle)]
T_BiometriaControle = Annotated[BiometriaControle, Depends(BiometriaControle)]
T_Usuario = Annotated[dict[str, Any], Depends(usuario_autenticado)]

@router.post("/login", response_model=Token)
def login(dados: LoginSchema, autenticacao: T_AutenticacaoControle, biometria: T_BiometriaControle):
    """Realiza login por meio do reconhecimento facial"""

    # Somente durante o desenvolvimento para não precisar do reconhecimento facial
    if MODO_DEV:
        permissao = randint(1, 3)
        usuarios = ["Aluno", "Professor", "Diretor"]
        token = autenticacao.criar_token(dados={"sub": usuarios[permissao-1], "user_id":permissao+3, "permissions": permissao})
        return {"token": token, "tipo": "Bearer"}

    return autenticacao.realizar_login(dados.fotos, biometria)


@router.post("/registrar", response_model=MensagemSchema)
def registrar(dados: RegistroSchema, controle: T_AutenticacaoControle, biometria: T_BiometriaControle):
    """Registra um novo usuário"""

    # Somente durante o desenvolvimento para não precisar do reconhecimento facial
    if MODO_DEV:
        falhar = randint(0, 1)
        if falhar:
            raise HTTPException(status_code=422, detail="Nenhum rosto encontrado na imagem")

    return controle.registrar_usuario(dados, biometria)


@router.get("/protegida")
def rota_protegida_testes(usuario: T_Usuario):
    """Testes temporários"""

    return {"message": "Acesso permitido", "usuario": usuario}
