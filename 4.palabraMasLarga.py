#Escriba un programa que pida al usuario dos palabras, 
#y que indique cuál de ellas es la más larga y por cuántas letras lo es.
palabra1 = str(input("Escriba una palabra\n"))
palabra2 = str(input("Escriba otra palabra\n"))
wordCounter = int()

if len(palabra1) > len(palabra2):
    wordCounter = len(palabra1) - len(palabra2)
    print(f"La palabra {palabra1} tiene {wordCounter} letras más que {palabra2}")
elif len(palabra2) > len(palabra1):
    wordCounter = len(palabra2) - len(palabra1)
    print(f"La palabra {palabra2} tiene {wordCounter} letras más que {palabra1}")
else:
    print("Las dos palabras tienen el mismo largo")