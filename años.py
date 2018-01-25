#coding: utf-8

anyo=int(input("Introduzca un año: "))

if anyo%400 == 0:
	print "Si es bisiesto!"
else:

	if anyo%100 == 0:
		print "No es bisiesto!"
	else:

		if anyo%4 == 0:
			print "Si es bisiesto!"



