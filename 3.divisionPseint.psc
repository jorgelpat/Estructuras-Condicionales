Algoritmo division
	
	Definir dividendo Como Entero
	Definir divisor Como Entero
	Escribir "Indique un numero"
	Leer dividendo
	Escribir "Indique un segundo numero"
	Leer divisor
	resultado = dividendo/divisor
	sobrante = dividendo mod divisor
	Si sobrante > 0 Entonces
		Escribir "No es una division exacta"
		Escribir "cociente ", resultado
		Escribir "resto ",sobrante
	SiNo
		Escribir "Es una division exacta"
		Escribir "cociente ", resultado
		Escribir "resto ",sobrante
	FinSi
	
FinAlgoritmo
