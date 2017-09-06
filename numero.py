"""
    Programa que realiza lo siguiente

    10 - 1
    9 - 2
    8 - 3

    Para ejecturarlo se usa python3 script.py

"""

def numero(numero_i, numero_fi):
    if(numero_i != 0):
        print(f"{numero_i} - {numero_fi}")
        numero(numero_i-1, numero_fi+1)

numero(10, 1)
