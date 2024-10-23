from pydantic import BaseModel


class LoginSchema(BaseModel):
    codigo: str
    fotos: list[str]


class RegistroSchema(BaseModel):
    nome: str
    fotos: list[str]


class Token(BaseModel):
    token: str
    tipo: str


class UsuarioToken(BaseModel):
    sub: str
    user_id: int
    permissions: int


class UsuarioRegistradoSchema(BaseModel):
    codigo: str
    nome: str
