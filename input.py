#!/usr/bin/python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Ejemplo con un while y excepciones para input 
# Inicializamos dos variables


while True:
	try:
		name = input('Hola, cual es su nombre?  ') # Entrada que guarda unString
		peso = float(input('Ingrese su peso:  ')) # Entrada que guarda un flotante
		edad = int(input('Ingresa tu edad:  '))   # Entrada que guarda un entero
		if (edad > 20 and peso >= 60):
			print (name, ' usted tiene ', edad, ' anios y pesa ', peso, ' kg\nSu peso anda bien :), continue cuidando su salud :D')	
		else:
			print ('Para ser adulto, según su edad y peso, no anda muy sano que digamos :/')
		break
	except:
		print ('Ingrese bien sus datos por favor')


