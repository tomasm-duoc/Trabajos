# Ejercicio 4

password = "contraseña"

while True:
    intento_usuario = input("Ingrese la contraseña: ")
    if len(intento_usuario) <= 0:
        print("\nERROR - Debe ingresar un texto con al menos un caracter.")
    else:
        if intento_usuario == password:
            print("Verificacion completada!")
            break
        else:
            print("Contraseña Incorrecta.") 