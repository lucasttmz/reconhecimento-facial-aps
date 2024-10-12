import cv2
import os
import numpy as np


TAMANHO_MINIMO = (100, 100)

def carregar_imagens_nova_pessoa(diretorio, id_pessoa):
    imagens = []
    ids = []  # [id_pessoa, id_pessoa, id_pessoa, ...]
    
    haarcascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # type: ignore

    for caminho_imagem in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, caminho_imagem)
        imagem = cv2.imread(caminho_completo)

        escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        rostos = haarcascades.detectMultiScale(escala_cinza, minSize=TAMANHO_MINIMO)

        if len(rostos) == 0:
            print(f"Nenhum rosto detectado na imagem {caminho_imagem}!")
            continue

        # Encontrar o maior rosto com base na área (largura * altura)
        maior_rosto = max(rostos, key=lambda r: r[2] * r[3])  # Seleciona o maior

        (coluna, linha, largura, altura) = maior_rosto
        rosto = escala_cinza[linha:linha+altura, coluna:coluna+largura]

        imagens.append(rosto)
        ids.append(id_pessoa)

    return imagens, np.array(ids)


# Carregar novas imagens
caminho_nova_pessoa = "img/treinamento/vinicius"
id_nova_pessoa = 4  # Importante ser um ID diferente dos já treinados!!!!!
novas_imagens, novos_ids = carregar_imagens_nova_pessoa(caminho_nova_pessoa, id_nova_pessoa)

lbph = cv2.face.LBPHFaceRecognizer_create()  # type: ignore
lbph.read("modelo_sem_vinicius.yml")
lbph.update(novas_imagens, novos_ids)
lbph.save("modelo.yml")

print(f"Modelo atualizado com {len(novas_imagens)} novas fotos da pessoa {id_nova_pessoa}.")
