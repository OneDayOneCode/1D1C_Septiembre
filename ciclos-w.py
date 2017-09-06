#!/usr/bin/python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

contador = 0
limite = 10

print ('contador básico con un ciclo while\n') # Este ciclo imprime el contenido de la variable contador mientras se cumpla la condición
while contador < 11:
	print ('---->', contador)
	contador +=1

var1 = int(input('Ingrese un número:  ')) # Pedimos un número

# Declaramos una función que usa un while para hacer multiplicaciones

def ciclo1(x): # Recibe un parametro
	contador = 1  # Declaramos una variable como contador con 1 para comenzar
	while contador <=10:  # Mientras nuestra variable contador sea menor o igual a 10
		print (x, ' X ', contador, ' = ', x * contador) # Se multiplica y se concatena
		contador += 1  # La variable contador incrementa en 1 y el ciclo se repite


print ('Vamos a imprimir la tabla de multiplicar de su variable, usando una función con ciclos...')

# Mandamos a llamar a la función pasando como parametro nuestra variable capturada por teclado

ciclo1(var1)
