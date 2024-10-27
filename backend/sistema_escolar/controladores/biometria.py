import base64
from http import HTTPStatus
from pathlib import Path

import cv2
from fastapi import HTTPException
import numpy as np


CAMINHO_MODELO = "modelo.yml"  # Modelo do LBPH
CONFIANCA_MINIMA = 10  # Valor para considerar correto o reconhecimento facial
QTD_VIZINHOS = 5  # Quantidade de ret. na detecção do rosto (haarcascades)
TAMANHO_MINIMO = (75, 75)  # Tamanho mínimo do rosto, se for menor é ignorado
USUARIO_NAO_RECONHECIDO = 0  # Constante para indicar falha no reconhecimento
QTD_MINIMA_TREINAMENTO = 8  # Qtd mínima de fotos para treinar o modelo


class BiometriaControle:
    def realizar_biometria(self, id_esperado: int, fotos: list[str]) -> int:
        """Realiza o processo de reconhecimento facial"""

        # Se nenhuma foto foi enviada (algo errado no front)
        if not fotos:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail="Nenhuma foto enviada para autenticação",
            )

        # Modelo não existe (nenhum usuário esta cadastrado)
        if not Path(CAMINHO_MODELO).exists():
            return USUARIO_NAO_RECONHECIDO

        # Tenta autenticar com cada imagem enviada
        for foto in fotos:
            # Imagem está em base64 e colorida, então lê ela e converte pra escala cinza
            imagem = decodificar_base64(foto)
            escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

            # Se não encontrar o rosto, tenta a próxima foto (não entra no if)
            rosto = self.encontrar_rosto(escala_cinza)
            if rosto is not None:
                id_usuario = self.reconhecer_rosto(rosto)

                # Retorna o usuário reconhecido se ele reconheceu e o código tbm bateu
                if id_usuario != USUARIO_NAO_RECONHECIDO and id_usuario == id_esperado:
                    return id_usuario

        # Se chegar aqui é que nenhuma das fotos reconheceu o usuário
        return USUARIO_NAO_RECONHECIDO

    def encontrar_rosto(self, escala_cinza):
        """Utiliza o modelo do haarcascades para encontra o rosto na foto"""

        # Encontra o rosto na imagem com o haar cascade
        haar_cascades = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"  # type: ignore
        )
        rostos = haar_cascades.detectMultiScale(
            escala_cinza, minNeighbors=QTD_VIZINHOS, minSize=TAMANHO_MINIMO
        )

        # Se não tiver nenhum rosto na imagem (ou não atingir o tamanho mínimo)
        if len(rostos) == 0:
            return None

        # Para o caso de falsos positivos, usa o maior rosto na imagem (area w * h)
        maior_rosto = max(rostos, key=lambda r: r[2] * r[3])

        # Separa o rosto do resto da imagem
        (x, y, w, h) = maior_rosto
        rosto = escala_cinza[y : y + h, x : x + w]

        return rosto

    def reconhecer_rosto(self, rosto) -> int:
        """Utiliza o modelo treinado do LBPH para reconhecer o rosto do usuário"""

        # Carrega o modelo do LBPH treinado anteriormente
        lbph = cv2.face.LBPHFaceRecognizer_create()  # type: ignore
        lbph.read("modelo.yml")

        # Reconhece o rosto com o LBPH
        id_pessoa, distancia = lbph.predict(rosto)

        # Checa se tem confiança suficiente no resultado
        confianca = 100 - distancia
        print(f"CONFIANÇA: {confianca}")
        if confianca >= CONFIANCA_MINIMA:
            return id_pessoa
        else:
            return USUARIO_NAO_RECONHECIDO

    def registrar_rosto(self, fotos: list[str], id_usuario: int) -> int:
        """Atualiza o modelo do LBPH com os rostos do novo usuário"""

        # Separa os rostos para o treinamento
        rostos = []
        for foto in fotos:
            # Imagem está em base64 e colorida, então lê ela e converte pra escala cinza
            imagem = decodificar_base64(foto)
            escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

            # Se não tiver um rosto na imagem, pula pra próxima
            rosto = self.encontrar_rosto(escala_cinza)
            if rosto is not None:
                rostos.append(rosto)

        # Caso não encontre a quantidade mínima de rostos para treinar o modelo
        if len(rostos) < QTD_MINIMA_TREINAMENTO:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail="Centralizar o rosto antes de tirar as fotos",
            )

        # Se o modelo existir, atualizar ele; se não, cria o modelo.
        if Path(CAMINHO_MODELO).exists():
            self.atualizar_modelo_lbph(rostos, id_usuario)
        else:
            self.criar_modelo_lbph(rostos, id_usuario)

        return id_usuario

    def criar_modelo_lbph(self, rostos, id_pessoa: int) -> None:
        """Cria o arquivo do modelo e treina com o primeiro usuário"""

        lbph = cv2.face.LBPHFaceRecognizer_create()  # type: ignore
        ids = np.array([id_pessoa] * len(rostos))  # ids precisam estar no formato do np
        lbph.train(rostos, ids)
        lbph.save(CAMINHO_MODELO)

    def atualizar_modelo_lbph(self, rostos, id_pessoa: int) -> None:
        """Carrega o modelo existente e treina com o novo usuário"""

        lbph = cv2.face.LBPHFaceRecognizer_create()  # type: ignore
        ids = np.array([id_pessoa] * len(rostos))  # ids precisam estar no formato do np
        lbph.read(CAMINHO_MODELO)
        lbph.update(rostos, ids)
        lbph.save(CAMINHO_MODELO)


def decodificar_base64(imagem_base64: str):
    """Transforma a imagem vinda do frontend (base64) em uma matriz do Numpy"""

    try:
        # Remove o prefixo do formato
        if imagem_base64.startswith("data:image/jpeg;base64,"):
            imagem_base64 = imagem_base64.split(",")[1]

        # Converte p/ formato que consegue ser interpretado no reconhecimento facial
        dados_imagem = base64.b64decode(imagem_base64)
        array = np.frombuffer(dados_imagem, dtype=np.uint8)
        imagem = cv2.imdecode(array, cv2.IMREAD_COLOR)
    except Exception:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="Foto de autenticação em formato inválido",
        )

    return imagem
