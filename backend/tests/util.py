from sistema_escolar.controladores.autenticacao import AutenticacaoControle


def criar_jwt(permissao: int):
    if permissao not in (1, 2, 3):
        assert False

    usuario = [(19, "Vinicius", 1), (15, "Lucas", 2), (20, "Josué", 3)][permissao - 1]
    token = AutenticacaoControle().criar_token(
        {"sub": usuario[1], "user_id": usuario[0], "permissions": usuario[2]}
    )
    return {"token": token, "tipo": "Bearer"}
