#Escriba un programa que pida dos números enteros y que calcule la división, 
#indicando si la división es exacta o no.

dividendo = int(input("indique un numero\n"))
divisor = int(input("indique un segundo numero\n"))
resultado = dividendo / divisor
sobrante = dividendo % divisor
if sobrante > 0:
    print("No es una division exacta")
    print(f"cociente {int(resultado)}")
    print(f"resto {sobrante}")
else:
    print("Es una division exacta")
    print(f"cociente {int(resultado)}")
    print(f"resto {sobrante}")