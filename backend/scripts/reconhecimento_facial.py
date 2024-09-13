import cv2


QTD_VIZINHOS = 5
TAMANHO_MINIMO = (75, 75)
LIMITE_CONFIANCA = 50 # 30 parece funcionar bem

haar_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # type: ignore
lbph = cv2.face.LBPHFaceRecognizer_create() #type: ignore
lbph.read("modelo.yml")

nomes = {0: "p1", 1: "p2"}
imagem = cv2.imread("img/teste.jpg")
escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Detecta os rostos
rostos = haar_cascades.detectMultiScale(escala_cinza, minNeighbors=QTD_VIZINHOS, minSize=TAMANHO_MINIMO)

# TODO: reescrever para considerar apenas o rosto com maior tamanho
for (x, y, w, h) in rostos:
    rosto = escala_cinza[y:y + h, x:x + w]
    
    id_pessoa, confianca = lbph.predict(rosto)
    
    # TODO: Prefirivel falhar do que reconhecer errado, achar um valor bom
    if confianca < LIMITE_CONFIANCA:  # Quanto menor o valor, maior a confiança
        nome = nomes.get(id_pessoa, "Desconhecido")
        cv2.putText(imagem, f"{nome} {confianca}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(imagem, f"Desconhecido {confianca}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 0, 255), 2)


cv2.imshow('Reconhecimento Facial', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()