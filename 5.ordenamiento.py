#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

cant = int(input("Elija la cantidad de números de 2 a 4 que va a ordenar\n"))

if cant == 2:
    number1 = int(input("Ingrese un número\n"))
    number2 = int(input("Ingrese un número\n"))
    lista = [number1,number2]
    lista.sort()
    print(f"{lista[0]} {lista[1]}")

elif cant == 3:
    number1 = int(input("Ingrese un número\n"))
    number2 = int(input("Ingrese un número\n"))
    number3 = int(input("Ingrese un número\n"))
    lista = [number1,number2,number3]
    lista.sort()
    print(f"{lista[0]} {lista[1]} {lista[2]}")

elif cant == 4:
    number1 = int(input("Ingrese un número\n"))
    number2 = int(input("Ingrese un número\n"))
    number3 = int(input("Ingrese un número\n"))
    number4 = int(input("Ingrese un número\n"))
    lista = [number1,number2,number3,number4]
    lista.sort()
    print(f"{lista[0]} {lista[1]} {lista[2]} {lista[3]}")

