Algoritmo a�osBisiestos
	
	Definir a�o Como Entero
	noGreg = a�o mod 4
	gregorio = a�o mod 400
	div = a�o mod 100
	bisiesto = Falso
	
	Si a�o < 1582 Entonces
		Si noGreg == 0 Entonces
			bisiesto = Verdadero
		FinSi
	FinSi
	
	Si a�o > 1582 Entonces
		Si noGreg == 0 y div =! 0 Entonces
			bisiesto = Verdadero
		FinSi
		Si gregorio == 0 y div == 0 Entonces
			bisiesto = Verdadero
		FinSi
	FinSi
	
	Si bisiesto == Verdadero Entonces
		Escribir "El a�o ",a�o," es bisiesto"
	SiNo
		Escribir "El a�o ",a�o," no es bisiesto"
	FinSi
	
	
	
FinAlgoritmo
