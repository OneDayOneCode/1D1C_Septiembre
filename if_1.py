#!/usr/bin/python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Evaluar un valor si esta entre varios posibles

acepta = input('Esta seguro de realizar la actualización (Y, y, S, s:  ')

if acepta in ('Y', 'y', 'S', 's'):
	print ('''Actualizando
	------------------------------
	------------------------------
	---------------***)''')
else:
	print ('Ha cancelado la actualización')

# Evaluar variables booleanas

respuesta = True

if respuesta:
	print ('La respuesta es True')
else:
	print ('La respuesta es False')


# Evaluar variables por tipo de dato usando función 'type'

v1 = 'Python 3.5.6'
v2 = 20
v3 = 3.1416
v4 = True
v5 = [1, 2, 3, 4, 5]
v6 = ('uno', 'dos', 'tres', 'cuatro')
v7 = {'a':1, 'b':2, 'c':3, 'd':4}

if type(v1) is str:
	print ('v1 es un String')

if type(v2) is int:
	print ('v2 es un entero')
	

print (type(v3), type(v4), type(v5), type(v6), type(v7))


# Evaluar si una cadena, lista o diccionario están vacíos

var1 = ""
var2 = []
var3 = {}

if not var1:
    print("Cadena vacía")

if not var2:
    print("Lista sin elementos")
    
if not var3:
    print("Diccionario sin claves/valores")
