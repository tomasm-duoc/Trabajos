# Ejercicio 2

while True:
    print("\n     Par o Impar")
    print("--Ingrese un número--")
    
    try:
        num_usuario = int(input("\n"))
    except ValueError:
        print("\nERROR - Ingrese un número entero\n")
    else:
        if num_usuario == 0:
            print("El número es 0.")
        elif num_usuario % 2  == 0:
            print("El número es par.")
        else:
            print("El número es impar.")