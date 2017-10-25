# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 4 - Ejercicio 9 - Escriu un programa que demani l'amplada i l'alçada d'un rectangle i ho dibuixi de la següent
manera:"""
print "Escribe la anchura del rectángulo:"
a=(int(raw_input()))
print "Escribe la altura del rectángulo:"
b=(int(raw_input()))

esp=" "*(a-4)

print "*"*a

for i in range((b-2)):
    print "*",esp,"*"

print "*"*a
