# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 4 - Ejercicio 3 - Escriu un programa que demani 2 nombres i escrigui la suma de sencers des del primer nombre
fins al segon."""
print "Escribe un n�mero, por favor:"
a=(int(raw_input()))
print "Escribe un n�mero mayor que",a,"para que se ejecute el programa:"
b=(int(raw_input()))
suma=0
for i in range(a,b+1):
    suma=suma+i
print "La suma de los n�meros entre",a,"y",b,"es de",suma,
