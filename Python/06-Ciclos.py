#!/usr/bin/env python
#_*_ coding: utf8 _*_

# while = bucle

numero = int(raw_input("Numero: "))
palabra = raw_input("Palabra: ")

contador = 0
while numero > contador:
    print(palabra)
    contador += 1

# for = bucle

numero = int(raw_input("Numero: "))
mensaje = raw_input("Coloque el mensaje: ")

for i in range(0, numero):
    print(mensaje)