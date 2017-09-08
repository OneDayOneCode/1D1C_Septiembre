#!/usr/bin/python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Función con número fijo de parámetros y devuelve algo con return

def area_triangulo(base, altura):  # Se define la función con sus dos parametros (variables) 
	return base * altura / 2  # Simplemente devuelve una operación


print (area_triangulo(10, 5)) # Mandamos a llamar a la función area_triangulo dentro de la función de imprimir (print) y le pasamos dos números como parametros 
                             # que seran el valor de las variables base y altura dentro de nuestra función

# Función con parámetros con valores por defecto

def pagar(importe, dto_aplicado = 10): # Se define la función con dos parametros, uno de ellos contiene un valor
	return importe - (importe * dto_aplicado / 100)


print (pagar(1000)) # Mandamos a llamar con un solo parámetro y el segundo se toma por elque esta en los parentesis de la función
print (pagar(1000, 30)) # Mandamos a llamar con dos parámetros y el segundo sustituye al que tiene valor 5 en los parentesis de la función

# Función con todos los parámetros por defecto

def repite_caracter(caracter="-", repite=3):
    return caracter * repite

print(repite_caracter())  # Se utilizan valores por omisión
print(repite_caracter('.',30))  # Muestra línea con 30 puntos
print(repite_caracter(repite=10, caracter='*'))  # Muestra: **********
