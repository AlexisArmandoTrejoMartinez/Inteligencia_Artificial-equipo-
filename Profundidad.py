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

import json
with open('base3.json') as file:
	data = json.load(file)
camino=[]

def busqueda(cuspide,valorbusqueda):
	
	if cuspide == valorbusqueda:
		return valorbusqueda
		
	for v in data:
		if v[0] == cuspide:
			camino.append(cuspide)
			print(v[0])
			resultado=busqueda(v[1],valorbusqueda)
			if resultado:
				return resultado
	camino.pop()
	
resultado=busqueda("C:","MemoriaRam.exe")
if resultado:
	print ("Archivo encontrado")
	print(camino)
else:
	print("no encontrado")
