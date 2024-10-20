from pydantic import BaseModel


class LoginSchema(BaseModel):
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
