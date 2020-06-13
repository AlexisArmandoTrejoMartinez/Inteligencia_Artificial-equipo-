import json
import random
from operator import itemgetter

with open('colina.json') as file:
	data = json.load(file)
ruta=[] #Lista para la ruta encontrada
camino=[] #Lista de los caminos a tomar
auxiliar = [] #Lista auxiliar para el siguiente camino
def subidadelacolina(inicial,objetivo,anterior):
	ruta.append(inicial)
	print("Inicio: "+inicial)
	print("Anterior: "+anterior)
	if auxiliar:
		del auxiliar[:]
		del camino[:]
	if objetivo == inicial:
		print("Punto Encontrado")
		return inicial
	if anterior == "":
		anterior = inicial
	for a in data: #el siguiente ciclo  garadara los caminos posibles en la lista cam
		if a[0] == inicial:
			if anterior != "":
				if a[1] != anterior:
					camino.append(a)
	print("Extración de la lista menor de la Lista")
	print(min(camino, key=itemgetter(2))[:]) #Imprimimos la Extracción de la lista menor de una lista de listas en camino
	print (camino) #Caminos menor
	minimo = (min(camino, key=itemgetter(2))[2])
	for b in camino:
		if b[2] == minimo:
			auxiliar.append(b)
	print("Camino menor")
	print(auxiliar)
	cont = 0
	for c in auxiliar:
		cont += 1 #Contador de los siguientes nodos
		if cont > 1: #Si es mayor de 1 tomara la aleatoriedad en los caminos
			r = random.random() #Se implementa el modo random para los caminos alternativos
			print("Aleatoriedad de los caminos")
			#Se borra un nodo aleatorio inicial o final de los caminos mas cortos
			if r < 0.5: #Linea de Error para 50% pŕobablidad de aleatoriedad
				auxiliar.pop()
			else: 
				auxiliar.pop(0)
		else:
			print(auxiliar) #Nodo Final
	if auxiliar:
		for n in auxiliar:
			print("Punto Siguiente")
			print(n[1])
			return subidadelacolina(n[1],objetivo,inicial)
arch=subidadelacolina("Z","I","")
if arch:
	print(arch)
	print("RUTA ENCONTRADA")
	print(ruta)
