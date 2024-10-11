import cv2
import os
import numpy as np


TAMANHO_MINIMO = (100, 100)

def carregar_imagens_do_treinamento(diretorio):
    imagens = []
    ids = [] # [1, 1, 1, 2, 2, 2, ...]
    nomes = {}
    id_atual = 1

    haarcascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # type: ignore

    for subdir in os.listdir(diretorio):
        caminho_dir = os.path.join(diretorio, subdir)

        # Se não for diretório já pula
        if not os.path.isdir(caminho_dir):
            continue

        nomes[id_atual] = subdir
        for caminho_imagem in os.listdir(caminho_dir):
            # Utilizar foto 5.jpg de cada pessoa como teste
            if caminho_imagem[0] == '5':
                continue

            caminho_completo = os.path.join(caminho_dir, caminho_imagem)
            imagem = cv2.imread(caminho_completo)

            escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            rostos = haarcascades.detectMultiScale(escala_cinza, minSize=TAMANHO_MINIMO)

            if len(rostos) == 0:
                print(f"Nenhum rosto detectado para {nomes[id_atual]}!")
                continue

            # Encontrar o maior rosto com base na área (largura * altura)
            maior_rosto = max(rostos, key=lambda r: r[2] * r[3])

            (coluna, linha, largura, altura) = maior_rosto
            rosto = escala_cinza[linha:linha+altura, coluna:coluna+largura]

            imagens.append(rosto)
            ids.append(id_atual)
        
        id_atual += 1

    return imagens, np.array(ids), nomes

caminho_das_fotos = "img/treinamento"
imagens, ids, nomes = carregar_imagens_do_treinamento(caminho_das_fotos)

print(f"Treinado com {len(imagens)} fotos para {ids[-1] + 1} pessoas")
lbph = cv2.face.LBPHFaceRecognizer_create() # type: ignore
lbph.train(imagens, ids)
lbph.save("modelo.yml")
