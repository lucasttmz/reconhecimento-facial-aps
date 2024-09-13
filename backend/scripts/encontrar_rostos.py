import cv2


COR =  (0, 255, 0) # Verde
LARGURA = 2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #type: ignore
imagem = cv2.imread('img/teste.jpg')
escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
rostos = face_cascade.detectMultiScale(escala_cinza, minSize=(30, 30))

for (x, y, largura, altura) in rostos:
    cv2.rectangle(imagem, (x, y), (x + largura, y + altura), COR, LARGURA)

cv2.imshow(f'LBPH', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()