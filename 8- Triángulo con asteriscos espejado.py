# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 4 - Ejercicio 8 - Escriu un programa que demani l'alçada d'un triangle i ho dibuixi de la següent manera:"""
print "Escribe la altura del triángulo:"
a=(int(raw_input()))

for n in range(1,(a+1)):
    print n*"*"

for n in range((a-1),0,-1):
    print n*"*"
