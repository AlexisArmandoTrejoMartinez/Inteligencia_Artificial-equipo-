"""
Cada funcion recibe la Carteta donde
empezara a buscar y el archivo a buscar

La funcion retorna True si encuentra
el archivo, e imprime la ruta

en caso contrario retorna falso

def primeroProfundidad(Carpeta,Archivo):
	pass
def primeroAnchura(Carpeta,Archivo):
	pass
"""
# Integrantes:
# Hidalgo Hernandez Juan Daniel
# Trejo Martinez Alexis Armando

import json
with open('base(2).json') as file:
	data = json.load(file)
colaangenda = []
expandido = []
visitados =[]

def hijos(padres):
	if padres in data[1]:
		print(colaangenda[0])
		return colaangenda

def primeroAnchura(carpeta,archivo):
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

print(expandido)
