import sqlite3

# Conexión
con = sqlite3.connect('db_relacional.sqlite')
cursor = con.cursor()
# Crear tablas
class Clinica:
    def __init__(self, nombre, direccion, capacidad, telefono, especialidad, empleados, sueldo_min, sueldo_max, edad_min, edad_max, exp_min, exp_max, fundado, establecimientos, doctores):
        self.nombre = nombre
        self.direccion = direccion
        self.capacidad = capacidad
        self.telefono = telefono
        self.especialidad = especialidad
        self.empleados = empleados
        self.sueldo_min = sueldo_min
        self.sueldo_max = sueldo_max
        self.edad_min = edad_min
        self.edad_max = edad_max
        self.exp_min = exp_min
        self.exp_max = exp_max
        self.fundado = fundado
        self.establecimientos = establecimientos
        self.doctores = doctores

class Parque:
    def __init__(self, nombre, ciudad, precio_entrada, area_m2, tipo, fundado, establecimientos, canchas, deporte, tematica):
        self.nombre = nombre
        self.ciudad = ciudad
        self.precio_entrada = precio_entrada
        self.area_m2 = area_m2
        self.tipo = tipo
        self.fundado = fundado
        self.establecimientos = establecimientos
        self.canchas = canchas
        self.deporte = deporte
        self.tematica = tematica

def connect_db():
    return sqlite3.connect('db_relacional.sqlite')

def crear_tablas(con):
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clinicas (
            nombre TEXT,
            direccion TEXT,
            capacidad INTEGER,
            telefono TEXT,
            especialidad_principal TEXT,
            empleados INTEGER,
            sueldo_min REAL,
            sueldo_max REAL,
            edad_min INTEGER,
            edad_max INTEGER,
            experiencia_min INTEGER,
            experiencia_max INTEGER,
            fundado INTEGER,
            establecimientos TEXT,
            doctores INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Parques (
            nombre TEXT,
            ciudad TEXT,
            precio_entrada REAL,
            area_m2 INTEGER,
            tipo TEXT,
            fundado INTEGER,
            establecimientos TEXT,
            canchas INTEGER,
            deporte TEXT,
            tematica TEXT
        )
    ''')
    con.commit()
def poblar_datos(cursor, con):
    # Poblar Clinicas si está vacía
    cursor.execute("SELECT COUNT(*) FROM Clinicas")
    if cursor.fetchone()[0] == 0:
        clinicas = [
            ("Clinica Vida", "Av. Quito 123", 50, "0935545643", "Pediatría", 20, 500.0, 1200.0, 25, 60, 2, 30, 1990, "Sucursal Norte,Sucursal Sur", 8),
            ("Clinica Esperanza", "Calle Loja 456", 100, "0988888888", "Traumatología", 35, 600.0, 1500.0, 28, 65, 5, 35, 1985, "Sucursal Centro", 15),
            ("Clinica Virgen del Carmen", "Av. al puerto", 80, "0999999999", "Ginecología", 18, 550.0, 1100.0, 27, 58, 3, 28, 2000, "Sucursal Este", 7),
            ("Clinica Mi Doctor", "Calle sucre y 8va norte", 40, "0977777777", "Dermatología", 10, 480.0, 900.0, 24, 55, 1, 20, 2010, "Sucursal Oeste", 4),
            ("Clinica San José", "Av. América 789", 60, "0966666666", "Cardiología", 22, 700.0, 1300.0, 30, 62, 4, 32, 1995, "Sucursal Norte", 10),
        ]
        cursor.executemany('''
            INSERT INTO Clinicas VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', clinicas)
        con.commit()

    # Poblar Parques si está vacía
    cursor.execute("SELECT COUNT(*) FROM Parques")
    if cursor.fetchone()[0] == 0:
        parques = [
            ("Parque La Alegría", "Guayaquil", 2.5, 5000, "Infantil", 2005, "Zona de juegos,Restaurante", 3, "Fútbol", "Aventura"),
            ("Parque Infantil", "Cuenca", 1.0, 3000, "Infantil", 2010, "Cafetería,Tiendas", 2, "Básquet", "Diversión"),
            ("Parque Central", "Quito", 3.0, 7000, "Familiar", 1998, "Lago,Teatro", 4, "Voleibol", "Cultural"),
            ("Parque de la Paz", "Loja", 1.5, 2000, "Familiar", 2015, "Juegos mecánicos,Heladería", 1, "Tenis", "Tranquilidad"),
            ("Parque del Sol", "Manta", 2.0, 4000, "Deportivo", 2008, "Piscina,Gimnasio", 5, "Natación", "Deporte"),
        ]
        cursor.executemany('''
            INSERT INTO Parques VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', parques)
        con.commit()
        
def ingresar_clinica(cursor):
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    capacidad = int(input("Capacidad: "))
    telefono = input("Teléfono: ")
    especialidad = input("Especialidad principal: ")
    empleados = int(input("Cantidad de empleados: "))
    sueldo_min = float(input("Sueldo mínimo: "))
    sueldo_max = float(input("Sueldo máximo: "))
    edad_min = int(input("Edad mínima: "))
    edad_max = int(input("Edad máxima: "))
    exp_min = int(input("Años de experiencia mínima: "))
    exp_max = int(input("Años de experiencia máxima: "))
    fundado = int(input("Año de fundación: "))
    establecimientos = input("Establecimientos (separados por coma): ")
    doctores = int(input("Cantidad de doctores: "))
    cursor.execute('''
        INSERT INTO Clinicas VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, direccion, capacidad, telefono, especialidad, empleados, sueldo_min, sueldo_max, edad_min, edad_max, exp_min, exp_max, fundado, establecimientos, doctores))
    print(f"\nClínica '{nombre}' ingresada correctamente.\n")

def ingresar_parque(cursor):
    nombre = input("Nombre: ")
    ciudad = input("Ciudad: ")
    precio_entrada = float(input("Precio de entrada: "))
    area_m2 = int(input("Área en m2: "))
    tipo = input("Tipo: ")
    fundado = int(input("Año de fundación: "))
    establecimientos = input("Establecimientos (separados por coma): ")
    canchas = int(input("Cantidad de canchas: "))
    deporte = input("Deporte principal: ")
    tematica = input("Temática del parque: ")
    cursor.execute('''
        INSERT INTO Parques VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, ciudad, precio_entrada, area_m2, tipo, fundado, establecimientos, canchas, deporte, tematica))
    print(f"\nParque '{nombre}' ingresado correctamente.\n")

def buscar_clinica(cursor):
    nombre = input("Nombre de la clínica a buscar: ")
    cursor.execute("SELECT * FROM Clinicas WHERE nombre = ?", (nombre,))
    clinica = cursor.fetchone()
    if clinica:
        print(f"\nClínica encontrada: {clinica}\n")
    else:
        print("\nNo se encontró la clínica.\n")

def buscar_parque(cursor):
    nombre = input("Nombre del parque a buscar: ")
    cursor.execute("SELECT * FROM Parques WHERE nombre = ?", (nombre,))
    parque = cursor.fetchone()
    if parque:
        print(f"\nParque encontrado: {parque}\n")
    else:
        print("\nNo se encontró el parque.\n")

def listar_clinicas(cursor):
    print("\nListado de clínicas:")
    for row in cursor.execute("SELECT nombre, capacidad, fundado, doctores FROM Clinicas"):
        print(f"Nombre: {row[0]}, Capacidad: {row[1]}, Fundado: {row[2]}, Doctores: {row[3]}")

def listar_parques(cursor):
    print("\nListado de parques:")
    for row in cursor.execute("SELECT nombre, ciudad, fundado, tematica FROM Parques"):
        print(f"Nombre: {row[0]}, Ciudad: {row[1]}, Fundado: {row[2]}, Temática: {row[3]}")

def clinicas_sueldo_mayor(cursor):
    sueldo = float(input("Sueldo mínimo a buscar: "))
    for row in cursor.execute("SELECT nombre, sueldo_max FROM Clinicas WHERE sueldo_max >= ?", (sueldo,)):
        print(f"Nombre: {row[0]}, Sueldo máximo: {row[1]}")

def clinicas_por_experiencia(cursor):
    anios = int(input("Años de experiencia mínima: "))
    for row in cursor.execute("SELECT nombre, experiencia_min FROM Clinicas WHERE experiencia_min >= ?", (anios,)):
        print(f"Nombre: {row[0]}, Experiencia mínima: {row[1]}")

def parques_por_deporte(cursor):
    deporte = input("Deporte a buscar: ")
    for row in cursor.execute("SELECT nombre, deporte FROM Parques WHERE deporte = ?", (deporte,)):
        print(f"Nombre: {row[0]}, Deporte: {row[1]}")

# Función principal
def main():
    con = connect_db()
    cursor = con.cursor()
    crear_tablas(con)
    poblar_datos(cursor, con) 
    
    print("Bienvenido al sistema de gestión de Clínicas y Parques\n")
    iteraciones = 0
    while iteraciones < 10:
        print("\nMenú:")
        print("1. Ingresar clínica")
        print("2. Ingresar parque")
        print("3. Buscar clínica")
        print("4. Buscar parque")
        print("5. Listar clínicas")
        print("6. Listar parques")
        print("7. Buscar clínicas por sueldo máximo")
        print("8. Buscar clínicas por experiencia mínima")
        print("9. Buscar parques por deporte")
        print("10. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            ingresar_clinica(cursor)
            con.commit()
        elif opcion == "2":
            ingresar_parque(cursor)
            con.commit()
        elif opcion == "3":
            buscar_clinica(cursor)
        elif opcion == "4":
            buscar_parque(cursor)
        elif opcion == "5":
            listar_clinicas(cursor)
        elif opcion == "6":
            listar_parques(cursor)
        elif opcion == "7":
            clinicas_sueldo_mayor(cursor)
        elif opcion == "8":
            clinicas_por_experiencia(cursor)
        elif opcion == "9":
            parques_por_deporte(cursor)
        elif opcion == "10":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
        iteraciones += 1

    con.close()

# consulta de datos
def mostrar_datos():
    con = connect_db()
    cursor = con.cursor()
    print("Clínicas:")
    for row in cursor.execute("SELECT * FROM Clinicas"):
        print(row)
    print("\nParques:")
    for row in cursor.execute("SELECT * FROM Parques"):
        print(row)
    con.close()


if __name__ == "__main__":
    main()
    mostrar_datos()


