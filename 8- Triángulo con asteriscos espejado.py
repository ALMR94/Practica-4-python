# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 4 - Ejercicio 8 - Escriu un programa que demani l'al�ada d'un triangle i ho dibuixi de la seg�ent manera:"""
print "Escribe la altura del tri�ngulo:"
a=(int(raw_input()))

for n in range(1,(a+1)):
    print n*"*"

for n in range((a-1),0,-1):
    print n*"*"
