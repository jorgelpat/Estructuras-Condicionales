Algoritmo añosBisiestos
	
	Definir año Como Entero
	noGreg = año mod 4
	gregorio = año mod 400
	div = año mod 100
	bisiesto = Falso
	
	Si año < 1582 Entonces
		Si noGreg == 0 Entonces
			bisiesto = Verdadero
		FinSi
	FinSi
	
	Si año > 1582 Entonces
		Si noGreg == 0 y div =! 0 Entonces
			bisiesto = Verdadero
		FinSi
		Si gregorio == 0 y div == 0 Entonces
			bisiesto = Verdadero
		FinSi
	FinSi
	
	Si bisiesto == Verdadero Entonces
		Escribir "El año ",año," es bisiesto"
	SiNo
		Escribir "El año ",año," no es bisiesto"
	FinSi
	
	
	
FinAlgoritmo
