#Escriba un programa que reciba como entrada la estatura, 
#el peso y la edad de una persona, y le entregue su condición de riesgo.

estatura = float(input("Indique su estatura: "))
peso = float(input("Indique su peso: "))
edad = int(input("Indique su edad: "))

imc = peso/(estatura**2)
if imc < 22 and edad < 45:
    print("Riesgo de Enfermedad Coronaria: Baja")
elif imc < 22 and edad >= 45:
    print("Riesgo de Enfermedad Coronaria: Medio")
elif imc >= 22 and edad < 45:
    print("Riesgo de Enfermedad Coronaria: Medio")
elif imc >= 22 and edad >= 45:
    print("Riesgo de Enfermedad Coronaria: Alto")
