#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nreinas.py
#  
#  Copyright 2020 alexis <alexis@alexis-HP-Pavilion-Notebook>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def entradasegura(matriz,fila,columna):
	N = len(matriz)
	#revisar a la izquierda
	for i in range(columna):
		if matriz[fila][i] == "2":
			return False

	#revisa a la derecha
	for i in range(columna,N,1):
		if matriz[fila][i] == "2":
			return False

	#revisa diagonal superior izquierda:
	for f,c in zip(range(fila,-1,-1), range(columna,-1,-1)):
		if matriz[f][c] == "2":
			return False

	#revisa diagonal inferior izquierda:
	for f,c in zip(range(fila, N, 1), range(columna,-1,-1)):
		if matriz[f][c] == "2":
			return False

	#revisa diagonal superior derecha:
	for f,c in zip(range(fila,-1,-1), range(columna,N,1)):
		if matriz[f][c] == "2":
			return False

	#revisa diagonal inferior derecha:
	for f,c in zip(range(fila,N,1), range(columna,N,1)):
		if matriz[f][c] == "2":
			return False
	return True

def iterarfilas(matriz,columna):
	N = len(matriz)
	if columna >=N:
		return True
	if columnaOcupada(matriz,columna):
		if iterarfilas(matriz,columna + 1)== True:
			return True
			
	for i in range(N):
		if entradasegura(matriz,i,columna):
			matriz[i][columna] = "2"
			if iterarfilas(matriz, columna + 1) == True:
				return True
			
			matriz[i][columna] = 0
		matriz[i][columna] = 0
	return False
	
def columnaOcupada (matriz,columna):
	N = len(matriz)
	for i in range(N):
		if matriz[i][columna]== "2":
			return True
	return False

def imprimeMatriz(matriz):
	N = len(matriz)
	for i in range(N):
		for j in range(N):
			print(matriz[i][j],end = " ")
		print()

def validareina(matriz):
	if iterarfilas(matriz,0)== False:
		print("\n No hay Solución")
		return False
		
	print ("\n Solucion")
	imprimeMatriz(matriz)
	return True

def escribeCeros(N):
	Lista = []
	for i in range(N):
		Lista.append(0)
	return Lista
	
N = int(input("Esbribe el tamaño de la matriz"))
f = int(input("Cordenada de la fila de la reina"))
c = int(input("Cordenada de la columna de la reina"))

matriz = []
for i in range(N):
	matriz.append(escribeCeros(N))
matriz[f][c]="2"
validareina(matriz)


