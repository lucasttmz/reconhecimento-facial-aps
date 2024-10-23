from os import environ
from random import choice, randint
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from sistema_escolar.controladores.autenticacao import AutenticacaoControle
from sistema_escolar.controladores.biometria import BiometriaControle
from sistema_escolar.modelos.autenticacao import LoginSchema, RegistroSchema, Token, UsuarioRegistradoSchema


MODO_DEV = environ.get("DEV", "false").lower() in ("true", "1")

router = APIRouter(tags=["autenticacao"])
T_AutenticacaoControle = Annotated[AutenticacaoControle, Depends(AutenticacaoControle)]
T_BiometriaControle = Annotated[BiometriaControle, Depends(BiometriaControle)]

@router.post("/login", response_model=Token)
def login(dados: LoginSchema, autenticacao: T_AutenticacaoControle, biometria: T_BiometriaControle):
    """Realiza login por meio do reconhecimento facial"""

    # Somente durante o desenvolvimento para não precisar do reconhecimento facial
    if MODO_DEV:
        usuarios = [(19, "Vinicius", 1), (15, "Lucas", 2), (20, "Josué", 3)]
        aleatorio = choice(usuarios)
        token = autenticacao.criar_token({
            "sub": aleatorio[1], "user_id":aleatorio[0], "permissions": aleatorio[2]
        })
        return {"token": token, "tipo": "Bearer"}

    return autenticacao.realizar_login(dados.codigo, dados.fotos, biometria)


@router.post("/registrar", response_model=UsuarioRegistradoSchema)
def registrar(dados: RegistroSchema, controle: T_AutenticacaoControle, biometria: T_BiometriaControle):
    """Registra um novo usuário"""

    # Somente durante o desenvolvimento para não precisar do reconhecimento facial
    if MODO_DEV:
        falhar = randint(0, 1)
        if falhar:
            raise HTTPException(status_code=422, detail="Nenhum rosto encontrado na imagem")

    return controle.registrar_usuario(dados, biometria)
