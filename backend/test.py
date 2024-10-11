def codificar_imagem():
    import base64

    caminho = "scripts/img/teste.jpg"

    with open(caminho, "rb") as imagem:
        imagem_b64 = base64.b64encode(imagem.read()).decode("utf-8")

    print(imagem_b64)



def testar_login():
    import httpx

    with open("base.txt") as f:
        foto = f.read().strip()

    data = {
        "fotos": [foto]
    }

    resposta = httpx.post("http://127.0.0.1:8000/login", json=data)
    print(resposta.status_code)
    print(resposta.json())


if __name__ == "__main__":
    testar_login()
