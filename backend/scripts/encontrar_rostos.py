import cv2


COR =  (0, 255, 0) # Verde
LARGURA = 2

haar_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # type: ignore

webcam = cv2.VideoCapture(0)

while True:
    acessou_webcam, frame = webcam.read()  # Le o frame da webcam
    if not acessou_webcam:
        print("Falha ao capturar imagem")
        break

    escala_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = haar_cascades.detectMultiScale(escala_cinza, minSize=(30, 30))

    for (x, y, largura, altura) in rostos:
        cv2.rectangle(frame, (x, y), (x + largura, y + altura), COR, LARGURA)

    cv2.imshow('Reconhecimento Facial', frame)

    # "q" para fechar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
