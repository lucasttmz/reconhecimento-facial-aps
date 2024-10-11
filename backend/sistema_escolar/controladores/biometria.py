import base64
from http import HTTPStatus

import cv2
from fastapi import HTTPException
import numpy as np


CAMINHO_MODELO = "modelo.yml"
CONFIANCA_MINIMA = 85
QTD_VIZINHOS = 5
TAMANHO_MINIMO = (75, 75)
USUARIO_NAO_RECONHECIDO = 0

class BiometriaControle():
    def realizar_biometria(self, fotos: list[str]) -> int:
        # Se nenhuma foto foi enviada (algo errado no front)
        if not fotos:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Nenhuma foto enviada para autenticação"
            )
        
        # Tenta autenticar com cada imagem enviada
        for foto in fotos:
            imagem = decodificar_base64(foto)
            escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

            rosto = self.encontrar_rosto(escala_cinza)
            if rosto is not None:
                id_usuario = self.reconhecer_rosto(rosto)

                if id_usuario != USUARIO_NAO_RECONHECIDO:
                    return id_usuario

        return USUARIO_NAO_RECONHECIDO
    
    def encontrar_rosto(self, escala_cinza):
        # Encontra o rosto na imagem
        haar_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # type: ignore
        rostos = haar_cascades.detectMultiScale(escala_cinza, minNeighbors=QTD_VIZINHOS, minSize=TAMANHO_MINIMO)

        # Se não tiver nenhum rosto
        if len(rostos) == 0:
            return None
        
        # Para o caso de falsos positivos, usa o maior rosto na imagem (area w * h)
        maior_rosto = max(rostos, key=lambda r: r[2] * r[3])

        # Separa o rosto do resto da imagem
        (x, y, w, h) = maior_rosto
        rosto = escala_cinza[y:y + h, x:x + w]

        return rosto
    
    def reconhecer_rosto(self, rosto) -> int:
        # Carrega o modelo
        lbph = cv2.face.LBPHFaceRecognizer_create() #type: ignore
        lbph.read("modelo.yml")

        # Reconhece o rosto
        id_pessoa, distancia = lbph.predict(rosto)

        # Checa se tem confiança suficiente no resultado
        confianca = 100 - distancia
        if confianca >= CONFIANCA_MINIMA:  
            return id_pessoa
        else:
            return 0

def decodificar_base64(imagem_base64: str):
    try:
        dados_imagem = base64.b64decode(imagem_base64)
        array = np.frombuffer(dados_imagem, dtype=np.uint8)
        imagem = cv2.imdecode(array, cv2.IMREAD_COLOR)
    except Exception:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="Foto de autenticação em formato inválido"
        )

    return imagem
