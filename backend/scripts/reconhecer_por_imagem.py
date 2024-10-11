import cv2


QTD_VIZINHOS = 5
TAMANHO_MINIMO = (75, 75)
CONFIANCA_MINIMA = 85
NOMES = {0: 'Josue', 1: 'Lucas', 2: 'Raul', 3: 'Samuel', 4: 'Vinicius'}


def reconhecimento_facial(imagem_colorida):
    # Pré processamento
    escala_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

    # Carregar modelo
    haar_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # type: ignore
    lbph = cv2.face.LBPHFaceRecognizer_create() #type: ignore
    lbph.read("modelo.yml")

    # Encontrar rostos nas imagens
    rostos = haar_cascades.detectMultiScale(escala_cinza, minNeighbors=QTD_VIZINHOS, minSize=TAMANHO_MINIMO)

    # Se não tiver nenhum rosto
    if len(rostos) == 0:
        print(f"Nenhum rosto detectado!")
        return

    # Encontrar o maior rosto com base na área (largura * altura)
    maior_rosto = max(rostos, key=lambda r: r[2] * r[3])
    (x, y, w, h) = maior_rosto
    rosto = escala_cinza[y:y + h, x:x + w]

    # Reconhece o rosto
    id_pessoa, distancia = lbph.predict(rosto)

    # Compara a confiança
    confianca = 100 - distancia
    if confianca >= CONFIANCA_MINIMA:  
        nome = NOMES.get(id_pessoa, "Desconhecido")
        cor = (0, 255, 0)
    else:
        nome = "Desconhecido"
        cor = (0, 0, 255)
    
    cv2.putText(imagem, f"{nome} {confianca}%", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, cor, 2)
    cv2.rectangle(imagem, (x, y), (x + w, y + h), cor, 2)
    cv2.imshow('Reconhecimento Facial', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    imagem = cv2.imread('img/treinamento/lucas/5.jpg')
    reconhecimento_facial(imagem)
