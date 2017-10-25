# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 4 - Ejercicio 4 - Escriu un programa que demani un nombre i calculi el seu factorial.
"""
print "Escribe un número, por favor:"
a=(int(raw_input()))
fact=1
for n in range (1,(a+1)):
    fact=fact*n
print "El factorial de",a,"es",fact,
