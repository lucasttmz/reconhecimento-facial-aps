from pydantic import BaseModel


class LoginSchema(BaseModel):
    """Dados necessários para efetuar o login em /login"""

    codigo: str
    fotos: list[str]


class RegistroSchema(BaseModel):
    """Dados necessários para efetuar o registro em /registrar"""

    nome: str
    fotos: list[str]


class Token(BaseModel):
    """Formato do JWT retornado no /login"""

    token: str
    tipo: str


class UsuarioToken(BaseModel):
    """Formato do usuário codificado dentro do token"""

    sub: str
    user_id: int
    permissions: int


class UsuarioRegistradoSchema(BaseModel):
    """Dados retornados quando um usuário é registrado"""

    codigo: str
    nome: str
