# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 4 - Ejercicio 2 - Escriu un programa que demani dos nombres i escrigui quins nombres son parells i quins s�n
senars (=�impares�) des del primer fins al segon."""
print "Escribe un numero, por favor:"
a=(int(raw_input()))
print "Escribe un n�mero mayor que",a,"para que se ejecute el programa:"
b=(int(raw_input()))
for i in range(a,b+1):
   if i % 2 is 0:
       print "El n�mero",i,"es par."
   else:
       print "El n�mero",i,"es impar."
