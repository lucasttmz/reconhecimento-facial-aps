from typing import Annotated

from fastapi import APIRouter, Depends

from sistema_escolar.controladores.autenticacao import AutenticacaoControle
from sistema_escolar.controladores.biometria import BiometriaControle
from sistema_escolar.modelos.autenticacao import (
    LoginSchema,
    RegistroSchema,
    Token,
    UsuarioRegistradoSchema,
)


# Injeção de dependência dos controladores
T_AutenticacaoControle = Annotated[AutenticacaoControle, Depends(AutenticacaoControle)]
T_BiometriaControle = Annotated[BiometriaControle, Depends(BiometriaControle)]
# Declaração do roteador de autenticação
router = APIRouter(tags=["autenticacao"])


@router.post("/login", response_model=Token)
def login(
    dados: LoginSchema,
    autenticacao: T_AutenticacaoControle,
    biometria: T_BiometriaControle,
):
    """Realiza login por meio do reconhecimento facial"""

    return autenticacao.realizar_login(dados.codigo, dados.fotos, biometria)


@router.post("/registrar", response_model=UsuarioRegistradoSchema)
def registrar(
    dados: RegistroSchema,
    controle: T_AutenticacaoControle,
    biometria: T_BiometriaControle,
):
    """Registra um novo usuário"""

    return controle.registrar_usuario(dados, biometria)
