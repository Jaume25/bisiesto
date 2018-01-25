#coding: utf-8

def esBisiesto(anyo):

	if anyo%400 == 0:
		print "True"

	else:
		if anyo%100 == 0:
			print "False"
		else:

			if anyo%4 == 0:
				print "True"

anyo1=int(input("Introduzca un año: "))
(esBisiesto(anyo1))

anyo2=int(input("Introduzca otro año: "))
(esBisiesto(anyo2))
	
anyo3=int(input("Introduzca otro año: "))
(esBisiesto(anyo3)) 

