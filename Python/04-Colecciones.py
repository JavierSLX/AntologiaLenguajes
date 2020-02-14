#!/usr/bin/env python
#_*_ coding: utf8 _*_

# ----- Lista -----
lista = list()
print(type(lista))

lista = []
print(type(lista))

lista = [1, 2, 3, 4, 5, 6, 7, 8, "a", "b", 2.5, 19.4, True, False]
print(lista)
print(lista[1])

for element in lista:
    print(element)

# Accediendo al ultimo elemento de la lista
print(lista[len(lista) - 1])

# Eliminando elemento
lista.pop(0)
print(lista)

# Imprimiendo de la posicion 0 a la 10
print(lista[0:10])

# Añadiendo valores a la lista
lista.append(25)
print(lista)

lista = ['h', 'o', 'l', 'a']

# Convierte la lista en cadena
lista = ''.join(lista)
print(lista)

# ----- Tupla (Es fija, no puede cambiar sus valores) -----
tupla = ("a", 1, 2, 3, 1.5, "c")
print(tupla[1])
print(tupla)
print(tupla[0:2])
print(type(tupla))

# ----- Diccionario -----
diccionario = dict(nombre = "alumno", plataforma = "Udemy", edad = 18)
print(diccionario)
print(diccionario['nombre'])
print(diccionario.viewkeys())

# Recorriendo un diccionario con las llaves
for i in range(0, len(diccionario)):
    keys = diccionario.keys()
    print(diccionario[keys[i]])

for i in diccionario.keys():
    print(diccionario[i])

# Lo convierte en una lista de tuplas
a = diccionario.items()
print(a)

# Obtiene solo los valores del diccionario
values = diccionario.values()
print(values)