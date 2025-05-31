from pymongo import MongoClient

def connect_to_mongo():
    cliente = MongoClient('mongodb://localhost:27017/')
    db = cliente.db_no_relacional
    return db

# Ingresar clínicas y parques en MongoDB
def ingresar_clinica(coleccion):
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    capacidad = int(input("Capacidad: "))
    especialidades = input("Especialidades (separadas por coma): ").split(",")
    empleados = int(input("Cantidad de empleados: "))
    sueldo_min = float(input("Sueldo mínimo: "))
    sueldo_max = float(input("Sueldo máximo: "))
    edad_min = int(input("Edad mínima: "))
    edad_max = int(input("Edad máxima: "))
    experiencia_min = int(input("Años de experiencia mínima: "))
    experiencia_max = int(input("Años de experiencia máxima: "))
    fundado = int(input("Año de fundación: "))
    establecimientos = input("Establecimientos (separados por coma): ").split(",")
    doctores = int(input("Cantidad de doctores: "))
    clinica = {
        "nombre": nombre,
        "direccion": direccion,
        "capacidad": capacidad,
        "especialidades": especialidades,
        "empleados": empleados,
        "sueldo_min": sueldo_min,
        "sueldo_max": sueldo_max,
        "edad_min": edad_min,
        "edad_max": edad_max,
        "experiencia_min": experiencia_min,
        "experiencia_max": experiencia_max,
        "fundado": fundado,
        "establecimientos": establecimientos,
        "doctores": doctores
    }
    # Insertar la clínica en la colección
    coleccion.insert_one(clinica)
    print(f"\nClinica '{nombre}' ingresada correctamente.\n")

# Ingresar parques en MongoDB
def ingresar_parque(coleccion):
    nombre = input("Nombre: ")
    ciudad = input("Ciudad: ")
    precio_entrada = float(input("Precio de entrada: "))
    area_m2 = int(input("Área en m2: "))
    tipo = input("Tipo: ")
    fundado = int(input("Año de fundación: "))
    establecimientos = input("Establecimientos (separados por coma): ").split(",")
    canchas = int(input("Cantidad de canchas: "))
    deporte = input("Deporte principal: ")
    tematica = input("Temática del parque: ")
    parque = {
        "nombre": nombre,
        "ciudad": ciudad,
        "precio_entrada": precio_entrada,
        "area_m2": area_m2,
        "tipo": tipo,
        "fundado": fundado,
        "establecimientos": establecimientos,
        "canchas": canchas,
        "deporte": deporte,
        "tematica": tematica
    }
    
    # Insertar el parque en la colección
    coleccion.insert_one(parque)
    print(f"\nParque '{nombre}' ingresado correctamente.\n")


# Buscar clínicas y parques en MongoDB
def buscar_clinica(coleccion):
    nombre = input("Nombre de la clínica a buscar: ")
    clinica = coleccion.find_one({"nombre": nombre})
    
    if clinica:
        print(f"\n{clinica}\n")
    else:
        print("\nNo se encontró la clínica.\n")

def buscar_parque(coleccion):
    nombre = input("Nombre del parque a buscar: ")
    parque = coleccion.find_one({"nombre": nombre})
    
    if parque:
        print(f"\n{parque}\n")
    else:
        print("\nNo se encontró el parque.\n")

def listar_clinicas(coleccion):
    print("\nListado de clínicas:")
    for c in coleccion.find():
        print(f"Nombre: {c['nombre']}, Capacidad: {c['capacidad']}, Fundado: {c['fundado']}, Doctores: {c['doctores']}")

def listar_parques(coleccion):
    print("\nListado de parques:")
    for p in coleccion.find():
        print(f"Nombre: {p['nombre']}, Ciudad: {p['ciudad']}, Fundado: {p['fundado']}, Temática: {p['tematica']}")

def main():
    db = connect_to_mongo()
    clinicas = db.clinicas
    parques = db.parques


    while True:
        print("\nMenú:")
        print("1. Ingresar clínica")
        print("2. Ingresar parque")
        print("3. Buscar clínica")
        print("4. Buscar parque")
        print("5. Listar clínicas")
        print("6. Listar parques")
        print("7. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            ingresar_clinica(clinicas)
        elif opcion == "2":
            ingresar_parque(parques)
        elif opcion == "3":
            buscar_clinica(clinicas)
        elif opcion == "4":
            buscar_parque(parques)
        elif opcion == "5":
            listar_clinicas(clinicas)
        elif opcion == "6":
            listar_parques(parques)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# basenorelacional/main_norela.py
if __name__ == "__main__":
    main()
