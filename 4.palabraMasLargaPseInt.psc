Algoritmo palabraMasLarga
	
	Definir palabra1 Como Caracter
	Definir palabra2 Como Caracter
	Definir wordCounter Como Entero
	
	Escribir "Escriba una palabra"
	Leer palabra1
	Escribir "Escriba otra palabra"
	Leer palabra2
	
	Si Longitud(palabra1) > Longitud(palabra2) Entonces
		wordCounter = Longitud(palabra1) - Longitud(palabra2)
		Escribir "La palabra "+palabra1+" tiene",wordCounter," letras mas que "+palabra2
	FinSi
	Si Longitud(palabra1) < Longitud(palabra2) Entonces
		wordCounter = Longitud(palabra2) - Longitud(palabra1)
		Escribir "La palabra "+palabra2+" tiene",wordCounter," letras mas que "+palabra1
	FinSi
	Si Longitud(palabra1) == Longitud(palabra2) Entonces
		Escribir "Las 2 palabras tienen el mismo largo"
	FinSi
	
	
FinAlgoritmo
