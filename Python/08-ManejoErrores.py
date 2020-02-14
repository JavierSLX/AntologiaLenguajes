#!/usr/bin/env python
#_*_ coding: utf8 _*_

try:
    print('La poblacion de {} es: {} millones'.format("México", 100))
except KeyError:
    print('El pais {} no esta en la informacion'.format("México"))