import cv2
import os
import imutils
#Integrantes
#Alexis Armando Trejo Martinez
#Juan Daniel Hidalgo Hernandez
#Codigo para la creación del data set en tiempo real mendiante video o web cam
personName = 'Uriel' #Nombre de la Carpeta del data set de la persona para el reconocimiento facial
dataPath = 'C:/Users/Lenovo/Documents/reconocimientoFacial/dataset' #Ruta predeterminada
personPath = dataPath + '/' + personName
#Si la carpeta no ha sido creada la creara y verificaremos con un label o mensaje
if not os.path.exists(personPath):
	print('Carpeta creada: ',personPath)
	os.makedirs(personPath)
#Realizamos la captura mediante camara web o por video striming
#cap = cv2.VideoCapture('Uriel.mp4')
webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
#Se realiza la lectura de rostro en video striming o video por fotogramas
	ret, frame = webcam.read()
	if ret == False: break
	frame =  imutils.resize(frame, width=640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		rostro = auxFrame[y:y+h,x:x+w]
		#Se redimenciona el tamaño de las imagenes a guardar en el data set de 150 X 150 px
		rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro) #se establece el formato de imagen en este caso sera .jpg
		count = count + 1
	cv2.imshow('frame',frame)

	k =  cv2.waitKey(1)
	if k == 27 or count >= 300: #Aqui establecemos el numero de imagenes a crear en el dataset
		break

webcam.release()
cv2.destroyAllWindows()