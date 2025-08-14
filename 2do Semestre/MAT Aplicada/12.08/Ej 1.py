# Ejercicio 1

while True:
    print("\n     Real o No")
    print("--Ingrese un número--")
    
    try:
        num_usuario = int(input("\n"))
    except ValueError:
        print("\nERROR - Ingrese un número entero\n")
    else:
        if num_usuario == 0:
            print("-- El número es 0 --")
        elif num_usuario < 0:
            print("-- El número es negativo --")
        elif num_usuario > 0:
            print("-- El número es positivo --")
