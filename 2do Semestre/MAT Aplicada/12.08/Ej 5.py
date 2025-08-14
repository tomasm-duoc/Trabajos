# Ejercicio 5

try:
    numero_usuario = int(input("Ingrese un número para mostrar su tabla de multiplicación: "))
except ValueError:
    print("\nERROR - Ingrese un valor númerico.")
else:
    for i in range(1,13):
        print(f"{numero_usuario} x {i} = {i*numero_usuario} ")
    