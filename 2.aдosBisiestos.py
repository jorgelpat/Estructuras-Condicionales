#Escriba un programa que indique si un año es bisiesto o no, 
#teniendo en cuenta cuál era el calendario vigente en ese año:
año = int(input("Indique un año\n"))
noGreg = año%4
gregorio = año%400
div = año%100
bisiesto = False

if año < 1582:
    if noGreg == 0:
        bisiesto = True
if año >1582:
    if noGreg == 0 and div != 0:
        bisiesto = True
    elif gregorio == 0 and div == 0:
        bisiesto = True

if bisiesto == True:
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")