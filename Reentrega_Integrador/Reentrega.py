empleados = [
    {"nombre": "Laura", "sector": "RRHH", "legajo": 1001, "antiguedad": 15},
    {"nombre": "Carlos", "sector": "Sistemas", "legajo": 1002, "antiguedad": 13},
    {"nombre": "Ana", "sector": "Contabilidad", "legajo": 1003, "antiguedad": 6},
    {"nombre": "Martín", "sector": "Logística", "legajo": 1004, "antiguedad": 24},
    {"nombre": "Bruno", "sector": "Ventas", "legajo": 1005, "antiguedad": 2},
    {"nombre": "Zoe", "sector": "Compras", "legajo": 1006, "antiguedad": 10},
    {"nombre": "Florencia", "sector": "Marketing", "legajo": 1007, "antiguedad": 9},
    {"nombre": "Emilia", "sector": "Atención al cliente", "legajo": 1008, "antiguedad": 6},
    {"nombre": "Santiago", "sector": "Sistemas", "legajo": 1009, "antiguedad": 7},
    {"nombre": "Valentina", "sector": "Contabilidad", "legajo": 1010, "antiguedad": 8},
    {"nombre": "Ignacio", "sector": "RRHH", "legajo": 1011, "antiguedad": 8},
    {"nombre": "Julieta", "sector": "Marketing", "legajo": 1012, "antiguedad": 12},
    {"nombre": "Nicolás", "sector": "Logística", "legajo": 1013, "antiguedad": 25},
    {"nombre": "Camila", "sector": "Compras", "legajo": 1014, "antiguedad": 8},
    {"nombre": "Marcos", "sector": "Ventas", "legajo": 1015, "antiguedad": 42},
    {"nombre": "Lucía", "sector": "Sistemas", "legajo": 1016, "antiguedad": 30},
    {"nombre": "Diego", "sector": "RRHH", "legajo": 1017, "antiguedad": 6},
    {"nombre": "Andrea", "sector": "Contabilidad", "legajo": 1018, "antiguedad": 21},
    {"nombre": "Franco", "sector": "Compras", "legajo": 1019, "antiguedad": 11},
    {"nombre": "Rocío", "sector": "Atención al cliente", "legajo": 1020, "antiguedad": 3},
    {"nombre": "Pedro", "sector": "Logística", "legajo": 1021, "antiguedad": 14},
    {"nombre": "Sofía", "sector": "Marketing", "legajo": 1022, "antiguedad": 12},
    {"nombre": "Leandro", "sector": "Ventas", "legajo": 1023, "antiguedad": 11},
    {"nombre": "Milagros", "sector": "RRHH", "legajo": 1024, "antiguedad": 14},
    {"nombre": "Tomás", "sector": "Sistemas", "legajo": 1025, "antiguedad": 2},
    {"nombre": "Natalia", "sector": "Contabilidad", "legajo": 1026, "antiguedad": 5},
    {"nombre": "Federico", "sector": "Compras", "legajo": 1027, "antiguedad": 3},
    {"nombre": "Daniela", "sector": "Marketing", "legajo": 1028, "antiguedad": 1},
    {"nombre": "Esteban", "sector": "Logística", "legajo": 1029, "antiguedad": 6},
    {"nombre": "Gimena", "sector": "Ventas", "legajo": 1030, "antiguedad": 2}
]

def bubble_sort_empleados(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["nombre"] > lista[j + 1]["nombre"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def buscar_empleado(lista, nombre):
    for empleado in lista:
        if empleado["nombre"].lower() == nombre.lower():
            return empleado
    return None

bubble_sort_empleados(empleados)

while True:
    print("\nOpciones:")
    print("1. Mostrar lista de empleados.")
    print("2. Buscar empleado:")
    print("3. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print("\nLista de empleados:")
        for emp in empleados:
            print(f"{emp['nombre']} - {emp['sector']} - Legajo {emp['legajo']} - {emp['antiguedad']} años")

    elif opcion == "2":
        nombre_buscado = input("Ingresá el nombre del empleado que querés buscar: ")
        resultado = buscar_empleado(empleados, nombre_buscado)
        if resultado:
            print(f"\nInformacion del empleado: {resultado['nombre']} trabaja en {resultado['sector']}, su legajo es {resultado['legajo']} y hace {resultado['antiguedad']} años trabaja en la empresa.")
        else:
            print(f"\nEl nombre {nombre_buscado} no pertenece a ningun empleado de la empresa.")

    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("La opción no es válida. Intentalo de nuevo porfavor.")