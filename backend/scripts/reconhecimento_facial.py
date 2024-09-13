import cv2


QTD_VIZINHOS = 5
TAMANHO_MINIMO = (75, 75)
LIMITE_CONFIANCA = 50 # 30 parece funcionar bem

haar_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # type: ignore
lbph = cv2.face.LBPHFaceRecognizer_create() #type: ignore
lbph.read("modelo.yml")

nomes = {0: "Lucas", 1: "Outro"}

webcam = cv2.VideoCapture(0)

while True:
    acessou_webcam, frame = webcam.read()  # Le o frame da webcam
    if not acessou_webcam:
        print("Falha ao capturar imagem")
        break

    escala_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = haar_cascades.detectMultiScale(escala_cinza, minNeighbors=QTD_VIZINHOS, minSize=TAMANHO_MINIMO)

    # TODO: reescrever para considerar apenas o rosto com maior tamanho
    for (x, y, w, h) in rostos:
        rosto = escala_cinza[y:y + h, x:x + w]

        id_pessoa, confianca = lbph.predict(rosto)

        # TODO: Prefirivel falhar do que reconhecer errado, achar um valor bom
        if confianca < LIMITE_CONFIANCA:  # Quanto menor o valor, maior a confiança
            nome = nomes.get(id_pessoa, "Desconhecido")
            cv2.putText(frame, f"{nome} {confianca}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, f"Desconhecido {confianca}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Reconhecimento Facial', frame)

    # "q" para fechar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()