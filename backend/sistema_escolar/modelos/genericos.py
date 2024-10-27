from pydantic import BaseModel


class MensagemSchema(BaseModel):
    """Mensagem retornada p/ informar sucesso ou falha em várias rotas"""

    mensagem: str
