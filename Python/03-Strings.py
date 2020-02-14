#!/usr/bin/env python
#_*_ coding: utf8 _*_

cadena = "esta es una cadena"

# Accede a un caracter
print(cadena[3])

# El largo de una cadena
print(len(cadena))

# Convierte en mayuscula
print(cadena.upper())

# Checa si es mayuscula
print(cadena.isupper())

# Convierte en minuscula
print(cadena.lower())

# Checa si es minuscula
print(cadena.islower())

# Checa si existe un caracter en la cadena
print(cadena.find('a'))

# Checa si el caracter es un digito
print(cadena.isdigit())

# Checa si la cadena termina con un caracter en especial
print(cadena.endswith('a'))

# Checa si la cadena comienza con un caracter en especial
print(cadena.startswith('a'))

# Separa la cadena a partir de uno de sus caracteres
print(cadena.split('n'))

# Separa cada caracter con un simbolo especial
print('-'.join(cadena))

# De toda la cadena en saltos de 2 myString[inicio:final:saltos]
print(cadena[1:6:2])

# Invertir la cadena
print(cadena[::-1])