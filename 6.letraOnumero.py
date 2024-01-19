#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. 
#En caso que sea letra, determine si es mayúscula o minúscula.

caract = input("Escriba un caracter\n")

digito = [caracter.isdigit() for caracter in caract]
letra = [caracter.isalpha() for caracter in caract]

if any(digito) == True:
    print("Es número")
elif any(letra) == True:
    if caract.isupper() == True:
        print("Es letra mayúscula")
    else:
        print("Es letra minúscula")
else:
    print("No es letra ni número")

