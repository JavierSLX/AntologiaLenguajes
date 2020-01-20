#include <stdio.h>

//CONSTANTE
#define PI 3.14

int main()
{
   printf("Esta es una constante: %.2f\n", PI);

   //VARIABLES
   //int => Guarda un numero entero en memoria
   int entero = 3;
   printf("Este un numero entero: %d\n", entero);

   //char => Guarda un caracter en memoria
   char caracter = 'c';
   printf("Este es un caracter: %c\n", caracter);

   //float => Guarda un numero flotante simple con 6 digitos de precision en memoria
   float flotante = 5.46;
   printf("Este es un numero flotante simple: %f\n", flotante);

   //double => Guarda un numero flotante doble lo que da 12 digitos de precision en memoria
   double doble = 1.2345678865;
   printf("Este es un numero flotante doble: %lf", doble);

   return 0;
}
