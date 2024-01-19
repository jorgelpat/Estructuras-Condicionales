#Escriba un programa que simule una calculadora básica, 
#este puede realizar operación de suma, resta, multiplicación y división.

operando = float(input("Escriba un numero\n"))
operador = str(input("Escriba un operador matemático (+,-,*,/)\n"))
operando2 = float(input("Escriba un numero\n"))

if operador == "+":
    operacion = operando + operando2
    print(f"{operando} {operador} {operando2} = {operacion}")
elif operador == "-":
    operacion = operando - operando2
    print(f"{operando} {operador} {operando2} = {operacion}")
elif operador == "*":
    operacion = operando * operando2
    print(f"{operando} {operador} {operando2} = {operacion}")
elif operador == "/":
    operacion = operando / operando2
    print(f"{operando} {operador} {operando2} = {operacion}")