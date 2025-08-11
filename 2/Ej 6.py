# Ejercicio 6

def producto(num1,num2):
    return num1*num2

def rendondeo(num):
    decim = num%1
    if decim >= 0.5:
        return (num-decim)+1
    else:
        return num-decim

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print(f"El resultado es: {rendondeo(producto(num1,num2))}")
