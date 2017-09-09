#include <stdio.h>
#include <stdlib.h>
/*El archivo se corre en la consola de Linux
 * gcc nombre.c
 * ./a.out
 * Debe de haber un archivo de texto con nombre "prueba".
 * */
FILE* abrirArchivo(char *nombre);
void leerArchivo(FILE *archivo);

int main()
{
	FILE* archivo=abrirArchivo("prueba");
	leerArchivo(archivo);
	return 0;
}

FILE* abrirArchivo(char *nombre)
{
	FILE *archivo=NULL;
	archivo = fopen(nombre,"r");
	if (archivo == NULL)
	{
		printf("Error de apertura del archivo.");
	}
	return archivo;
}

void leerArchivo(FILE *archivo)
{
	int caracter;
	printf("El contenido del archivo de prueba es \n");
	while((caracter = fgetc(archivo)) != EOF)
	{
		printf("%c",caracter);
	}
	printf("\n");
	fclose(archivo);
}
