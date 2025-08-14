# Ejercicio 9

def calculo_imc(peso,altura):
    imc = peso/altura^2
    return imc

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = calculo_imc(peso,altura)
clasificacion_imc = ""

if imc < 18.5:
    clasificacion_imc = "Bajo Peso"
elif imc >= 18.5 and imc <= 24.9:
    clasificacion_imc = "Peso Normal"
elif imc > 24.9 and imc <= 29.9:
    clasificacion_imc = "Sobrepeso"
elif imc > 29.9:
    clasificacion_imc = "Obesidad"
    
print(f"Usted tiene un IMC de: {imc} o {clasificacion_imc}")

