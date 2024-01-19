#Escriba un programa que determine si el número entero ingresado por el usuario es par o no.
number = int(input("Indique un numero\n"))
if number%2 == 0:
    input(f"{number} es un nuúmero par")
else:
    input(f"{number} no es un número par")