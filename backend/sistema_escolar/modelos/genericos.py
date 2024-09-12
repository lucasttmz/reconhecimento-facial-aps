from pydantic import BaseModel


class MensagemSchema(BaseModel):
    mensagem: str
