# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 4 - Ejercicio 9 - Escriu un programa que demani l'amplada i l'al�ada d'un rectangle i ho dibuixi de la seg�ent
manera:"""
print "Escribe la anchura del rect�ngulo:"
a=(int(raw_input()))
print "Escribe la altura del rect�ngulo:"
b=(int(raw_input()))

esp=" "*(a-4)

print "*"*a

for i in range((b-2)):
    print "*",esp,"*"

print "*"*a
