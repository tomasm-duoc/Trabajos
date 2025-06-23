estudiantes = {
    "lista":
    [
        {
            "id": "1",
            "nombre": "nombre1",
            "apellido": "apellido1",
            "genero": "N/A",
            "promedio": 0.0
        },
        {
            "id": "2",
            "nombre": "nombre2",
            "apellido": "apellido2",
            "genero": "N/A",
            "promedio": 0.0
        }
    ]
}

def verificacion_entero(mensaje:str):
    """Esta función recibira como argumento el mensaje que desea mostrar en la terminal y seguidamente verificara si el valor entregado sea entero."""
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("\nERROR - Ingrese un valor númerico.")
        else:
            return numero

def verificacion_string(mensaje:str):
    while True:
        string = input(mensaje)
        if len(string.strip()) < 1:
            print("\nERROR - No puede dejar un texto vacio.")
        else:
            return string

def mostrar_estudiantes(cantidad):
    """La función mostrar_estudiantes recibe un solo argumento para identificar si mostrara 1 estudiante especifico o todos.
    Si el argumento cantidad == Y mostrara todos los estudiantes de la lista, de lo contrario solamente mostrara el estudiante
    que tenga la id correspondiente entregada en el mismo argumento."""
    if cantidad == "Y":    
        for i in estudiantes["lista"]:
            print(f"\nID: {i["id"]}")
            print(f"Nombre: {i["nombre"]}")
            print(f"Apellido: {i["apellido"]}")
            if i["genero"] == "M" or i["genero"] == "m":
                print("Genero: Masculino")
            elif i["genero"] == "F" or i["genero"] == "f":
                print("Genero: Femenino")
            else:
                print("Genero: N/A")
            print(f"Promedio: {i["promedio"]}")
            
    else:
        for i in estudiantes["lista"]:
            if i["id"] == cantidad:
                print(f"\nID: {i["id"]}")
                print(f"Nombre: {i["nombre"]}")
                print(f"Apellido: {i["apellido"]}")
                if i["genero"] == "M" or i["genero"] == "m":
                    print("Genero: Masculino")
                elif i["genero"] == "F" or i["genero"] == "f":
                    print("Genero: Femenino")
                else:
                    print("Genero: N/A")
                print(f"Promedio: {i["promedio"]}")
                break
        print("\nERROR - ID no encontrada. Revise los datos proporcionados.")
                
    
"""
1. Registrar estudiante
2. Buscar estudiante
3. Modificar datos de estudiante
4. Eliminar estudiante
5. Mostrar todos los estudiantes
6. Salir """

while True:
    print("\n1. Registrar estudiante")
    print("2. Buscar estudiante")
    print("3. Modificar datos de estudiante")
    print("4. Eliminar estudiante")
    print("5. Mostrar todos los estudiantes")
    print("6. Salir\n")
    
    opcion = verificacion_entero("Ingrese la opción que desea ejecutar: ")
    
    #opc 1 Registrar
    if opcion == 1:
        print("ola")
        
    #opc 2 Buscar
    elif opcion == 2:
        id = verificacion_string("Ingrese la id del estudiante que desea buscar: ")
        mostrar_estudiantes(id)   
         
    #opc 3 MOdificar
    elif opcion == 3:
        print(f"opcion = {opcion}")
    
    #opc 4 ELiminar
    elif opcion == 4:
        print(f"opcion = {opcion}")
    
    #opc 5 Mostrar
    elif opcion == 5:
        mostrar_estudiantes("Y")
        
    #opc 6 Salir
    elif opcion == 6:
        print(f"opcion = {opcion}")
        break
    
    else:
        print(f"opcion = {opcion}")
        print("Ingrese una opción valida.")