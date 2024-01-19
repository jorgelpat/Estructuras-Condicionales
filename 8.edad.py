#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
from time import localtime
t = localtime()
t.tm_mday
t.tm_mon
t.tm_year

fechaNac = []
diaNac = int(input("Indique el dia de nacimiento\n"))
mesNac = int(input("Indique el mes de nacimiento\n"))
añoNac = int(input("Indique el año de nacimiento\n"))

print(fechaNac)
if t.tm_mon >= mesNac and t.tm_mday >= diaNac:
    edad = t.tm_year - añoNac
    print("Su edad en el momento es de {} años".format(edad))
else:
    edad = (t.tm_year - añoNac) - 1
    print("Su edad en el momento es de {} años".format(edad))




