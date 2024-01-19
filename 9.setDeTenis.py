#Desarrolle un programa que solucione el problema de Solarrabietas:
a = int(input("A: "))
b = int(input("B: "))

difer1 = b - a
difer2 = a - b

if a >= 6 and b >= 6:
    if difer2 >= 2 or difer1 >= 2:
        if a > b:
            print("Gana A")
        if b > a:
            print("Gana B")
elif (a >= 0 and a < 6) and (b >= 0 and b < 6):
    print("Aun no termina")
elif (a >= 5 and a <= 7) and (b >= 5 and b <= 7):
    if a == 7:
        print("Gana A")
    elif b == 7:
        print("Gana B")
    else:
        print("Aún no termina")
elif a == 6 and (b >= 0 and b < 5):
    print("Gana A")
elif b == 6 and (a >= 0 and a < 5):
    print("Gana B")
else:
    print("Invalido")