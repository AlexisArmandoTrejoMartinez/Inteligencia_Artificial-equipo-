"""
Cada funcion recibe la Carteta donde
empezara a buscar y el archivo a buscar

La funcion retorna True si encuentra
el archivo, e imprime la ruta

en caso contrario retorna falso

def primeroProfundidad(Carpeta,Archivo):
	pass
def primeroAnchura(Carpeta,Archivo)P:
	pass
"""
# Integrantes:
# Hidalgo Hernandez Juan Daniel
# Trejo Martinez Alexis Armando

import json
with open('base3.json') as file:
	data = json.load(file)
revisados =[]
camino=[]
auxiliar = []
Nodsig=[]

def primeroAnchura(Carpeta,Archivo):
	#Recorrido Siguiente del Nodo Principal 
	if Carpeta == Archivo:
		return Archivo
	if Nodsig:
		contador = 0
		for X in Nodsig:
			 contador += 1
		if contador > 1:
			print("Nodo principal: " +Nodsig[0])
			Nodsig.pop(0)#Se realiza la eliminación de la cola adyacente
			#Se genera un auxiliar para los nodos ya visitados y asu vez se limpia
	if auxiliar:
		del auxiliar[:]
	for i in data:
		if i[0] == Carpeta:
			Nodsig.append(i[1])
			auxiliar.append(i[0])
			if i[1] == Archivo:
				nodo = primeroAnchura(i[1],Archivo)#Se genera la primera recursividad
				return nodo
	revisados.append(list(set(auxiliar)))
	if revisados:
		print("Nodos Recorridos Adyacentemente")
		print(str(revisados))
		print(Nodsig[0])
		camino.append(Nodsig[0])
		return primeroAnchura(Nodsig[0],Archivo)

nodo = primeroAnchura("C:","Profe de quimica en arrel.jpg")
print("Hijo encontrado en el nodo principal: " +nodo)
cam = []
if nodo:
	for c in camino:
		if c not in cam:
			cam.append(c)
	print("Padres(Nodos Revisados)")
	print(cam)
else:
	print("No se encontro")


"""def primeroAnchura(carpeta,archivo):
	if carpeta == archivo:
		return archivo

	for v in data:
		if v[0] == carpeta:
			print(v[0]+"/"+v[1])
			colaangenda.append(v[0])
			expandido.append(colaangenda.pop(0))
			hijos(colaangenda)
			r = primeroAnchura(v[1],archivo)
			if r:
				return r
primeroAnchura("1","20")

print(expandido)"""
