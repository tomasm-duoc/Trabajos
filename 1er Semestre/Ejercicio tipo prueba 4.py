estudiantes = {
    "lista":
    [
        {
            "id": "d23afd",
            "nombre": "nombre1",
            "apellido": "apellido1",
            "genero": "M",
            "promedio": 0.0
        },
        {
            "id": "2P4Gfd",
            "nombre": "nombre2",
            "apellido": "apellido2",
            "genero": "F",
            "promedio": 1.0
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

def verificacion_float(mensaje:str):
    """Esta función recibira como argumento el mensaje que desea mostrar en la terminal y seguidamente verificara si el valor entregado sea decimal."""
    while True:
        try:
            numero = float(input(mensaje))
        except ValueError:
            print("\nERROR - Ingrese un valor númerico con un decimal.")
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
    
    # Si se define el argumento con "Y" esta funcion mostrara todos los estudiantes disponibles
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
    
    # Si se define el argumento con cualquier cosa aparte de "Y" checkeara por el estudiante especifico que se entregue   
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
                # Si encuentra la id recorriendo la lista retornara True
                return i
        # Si no encuentra la id recorriendo la lista retornara False
        return False
    
def buscar_estudiante(id):
    for i in estudiantes["lista"]:
        if i == id:
            return i
    return False
        
while True:
    print("\n1. Registrar estudiante")  
    print("2. Buscar estudiante") 
    print("3. Modificar datos de estudiante") 
    print("4. Eliminar estudiante")   #
    print("5. Mostrar todos los estudiantes")
    print("6. Salir\n")
    
    opcion = verificacion_entero("Ingrese la opción que desea ejecutar: ")
    
    #opc 1 Registrar
    if opcion == 1:
        while True:    
            id = verificacion_string("\nIngrese la ID del nuevo estudiante: ")
            if len(id) > 6:
                print("\nERROR - La ID no puede ser tener mas de 6 caracteres de largo")
                continue
            verificacion_id = mostrar_estudiantes(id)
            if verificacion_id == False:
                print("ID valida!")
            else:
                print("\n^ Esa ID ya existe! ^")
                print("\nSi desea modificar un estudiante dirigase a la opcion 3 del menú.")
                exit = verificacion_string('Ingrese "Y" para salir de esta opción: ')
                if exit.lower() == "y":
                    break
                else:
                    continue
                
            nombre = verificacion_string("\nIngrese el nombre del nuevo estudiante: ")
            apellido = verificacion_string("\nIngrese el apellido del nuevo estudiante: ")
            while True:
                genero = verificacion_string("\nIngrese el genero del nuevo estudiante (F/M): ")
                if genero.lower() == "f" or genero.lower() == "m":
                    break
                else:
                    print("\nERROR - Ingrese el genero de la manera especificada.")
                    
            while True:
                promedio = verificacion_float("\nIngrese el promedio del nuevo estudiante: ")
                if promedio > 7 or promedio < 1:
                    print("\n ERROR - el promedio no puede ser menor que 1.0 o mayor que 7.0.")
                else:
                    break
                    
            print(f"ID: {id}")
            print(f"Nombre: {nombre}")
            print(f"Apellido: {apellido}")
            print(f"Genero: {genero}")
            print(f"Promedio: {promedio}")
            
            correccion = verificacion_string('\nEstan bien los datos ingresados? Ingrese "Y" para confirmar: ')
            if correccion.lower() == "y":
                estudiante_nuevo = {
                    "id": id,
                    "nombre": nombre,
                    "apellido": apellido,
                    "genero": genero.upper(),
                    "promedio": promedio
                }
                estudiantes["lista"].append(estudiante_nuevo)
                print("\nEstudiante nuevo añadido exitosamente!")
                break
            else:
                continue
            
    #opc 2 Buscar
    elif opcion == 2:
        id = verificacion_string("Ingrese la ID del estudiante que desea buscar: ")
        if len(id) > 6:
            print("\nERROR - La ID no puede ser tener mas de 6 caracteres de largo")
            continue
        if mostrar_estudiantes(id) == False:
            print("\nERROR - ID no encontrada. Revise los datos proporcionados.")          
         
    #opc 3 MOdificar
    elif opcion == 3:
        while True:
            id = verificacion_string("Ingrese la ID del estudiante que desea modificar: ")
            if len(id) > 6:
                print("\nERROR - La ID no puede ser tener mas de 6 caracteres de largo")
                continue
            estudiante = mostrar_estudiantes(id)
            if estudiante == False:
                print("\nERROR - ID no encontrada. Revise los datos proporcionados.")
                continue     
            else:
                nombre = verificacion_string("\nIngrese el nombre del nuevo estudiante: ")
                apellido = verificacion_string("\nIngrese el apellido del nuevo estudiante: ")
                while True:
                    genero = verificacion_string("\nIngrese el genero del nuevo estudiante (F/M): ")
                    if genero.lower() == "f" or genero.lower() == "m":
                        break
                    else:
                        print("\nERROR - Ingrese el genero de la manera especificada.")
                        
                while True:
                    promedio = verificacion_float("\nIngrese el promedio del nuevo estudiante: ")
                    if promedio > 7 or promedio < 1:
                        print("\n ERROR - el promedio no puede ser menor que 1.0 o mayor que 7.0.")
                    else:
                        break
                    
                print(f"Nombre: {nombre}")
                print(f"Apellido: {apellido}")
                print(f"Genero: {genero}")
                print(f"Promedio: {promedio}")
                
                if verificacion_string('\nEstan bien los datos ingresados? Ingrese "Y" para confirmar: ').lower() == "y":
                    estudiante["nombre"] = nombre
                    estudiante["apellido"] = apellido
                    estudiante["genero"] = genero.upper()
                    estudiante["promedio"] = promedio
                    print("\nEstudiante modificado exitosamente!")  
                    break
                else:
                    break
                                 
    #opc 4 ELiminar
    elif opcion == 4:
        id = verificacion_string("Ingrese la ID del estudiante que desea eliminar: ")
        if len(id) > 6:
            print("\nERROR - La ID no puede ser tener mas de 6 caracteres de largo")
            continue
        estudiante_eliminar = mostrar_estudiantes(id)
        if estudiante_eliminar == False:
            print("\nERROR - ID no encontrada. Revise los datos proporcionados.")   
        else:
            if verificacion_string('\nIngrese "Y" para confirmar la eliminacion de este estudiante: ').lower() == "y":
                estudiantes["lista"].remove(estudiante_eliminar)
    #opc 5 Mostrar
    elif opcion == 5:
        mostrar_estudiantes("Y")
        
    #opc 6 Salir
    elif opcion == 6:
        break
    
    else:
        print("\nERROR - Ingrese una opción valida.")
        
print("Adios!!!")