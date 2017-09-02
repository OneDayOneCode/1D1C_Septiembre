/*
 ============================================================================
 Name        : OneDayOneCodeC.c
 Author      : Token
 Version     : 0.0
 Copyright   : Done by Token
 Description : Suma y multiplicación de dos números.
 ============================================================================
 */
#include <stdio.h>

void pedirNumeros();
void sumar(int numeroUno, int numeroDos);
void multiplicar(int numeroUno, int numeroDos);

int numeroUno, numeroDos;

int main()
{
	pedirNumeros();
	sumar(numeroUno,numeroDos);
	multiplicar(numeroUno,numeroDos);
	return 0;
}

void pedirNumeros()
{
	printf("Introduzca el primer numero (entero): ");
	scanf("%d", &numeroUno);
	printf("Introduzca el segundo numero (entero): ");
	scanf("%d", &numeroDos);
}

void sumar(int numeroUno, int numeroDos) {
	printf("La suma es: %d", numeroUno + numeroDos);
}

void multiplicar(int numeroUno, int numeroDos) {
	printf("\nLa multiplicación es: %d", numeroUno * numeroDos);
}
