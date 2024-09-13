import cv2
import numpy as np


TAMANHO_MINIMO = (100, 100)

def LBP_3x3(imagem):
    imagem_final = np.zeros_like(imagem)  # Vazia
    vizinhos = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for linha in range(1, imagem.shape[0] - 1):
        for coluna in range(1, imagem.shape[1] - 1):
            centro_matriz = imagem[linha, coluna]
            binario = "0"

            for x, y in vizinhos:
                binario += "1" if imagem[linha + x, coluna + y] >= centro_matriz else "0"

            imagem_final[linha, coluna] = int(binario, 2)

    return imagem_final


imagem = cv2.imread('img/treinamento/p1/1.jpg', cv2.IMREAD_GRAYSCALE)
haarcascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # type: ignore
rostos = haarcascades.detectMultiScale(imagem, minSize=TAMANHO_MINIMO)

# Linha e coluna no NumPy invertidos
coluna, linha, largura, altura = rostos[0]
rosto = imagem[linha:linha+altura, coluna:coluna+largura]
contornos = LBP_3x3(rosto)

cv2.imshow("LBP", contornos)
cv2.waitKey(0)
cv2.destroyAllWindows()