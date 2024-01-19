#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

if a < (b+c) or b < (a+c) or c < (a+b):
    if a == b or b ==c or a == c:
        print("Es un triangulo isóceles")
    else:
        print("Es un triangulo escaleno")
else:
    print("No es un triangulo válido")