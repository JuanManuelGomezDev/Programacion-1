empleados = [
    {"nombre": "Laura", "sector": "RRHH", "legajo": 1001, "antiguedad": 5},
    {"nombre": "Carlos", "sector": "Sistemas", "legajo": 1002, "antiguedad": 3},
    {"nombre": "Ana", "sector": "Contabilidad", "legajo": 1003, "antiguedad": 6},
    {"nombre": "Martín", "sector": "Logística", "legajo": 1004, "antiguedad": 4}
]

def ordenar_empleados(lista, clave):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][clave] > lista[j + 1][clave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def buscar_empleado(nombre):
    for emp in empleados:
        if emp["nombre"].lower() == nombre.lower():
            return emp
    return None

def agregar_empleado():
    nombre = input("Nombre: ")
    sector = input("Sector: ")
    legajo = int(input("Legajo: "))
    antiguedad = int(input("Años de antigüedad: "))
    empleados.append({"nombre": nombre, "sector": sector, "legajo": legajo, "antiguedad": antiguedad})
    print("Empleado agregado correctamente.")

def modificar_empleado():
    nombre = input("Nombre del empleado a modificar: ")
    emp = buscar_empleado(nombre)
    if emp:
        print("Empleado encontrado. Ingrese nuevos datos:")
        emp["nombre"] = input(f"Nuevo nombre ({emp['nombre']}): ") or emp["nombre"]
        emp["sector"] = input(f"Nuevo sector ({emp['sector']}): ") or emp["sector"]
        legajo_input = input(f"Nuevo legajo ({emp['legajo']}): ")
        emp["legajo"] = int(legajo_input) if legajo_input else emp["legajo"]
        antig_input = input(f"Nueva antigüedad ({emp['antiguedad']}): ")
        emp["antiguedad"] = int(antig_input) if antig_input else emp["antiguedad"]
        print("Empleado modificado correctamente.")
    else:
        print("Empleado no encontrado.")

def eliminar_empleado():
    nombre = input("Nombre del empleado a eliminar: ")
    emp = buscar_empleado(nombre)
    if emp:
        empleados.remove(emp)
        print("Empleado eliminado.")
    else:
        print("Empleado no encontrado.")

def mostrar_lista():
    for emp in empleados:
        print(f"{emp['nombre']} - {emp['sector']} - Legajo {emp['legajo']} - {emp['antiguedad']} años")

while True:
    print("\n--- Menú de Opciones ---")
    print("1. Mostrar empleados ordenados por nombre")
    print("2. Mostrar empleados ordenados por antigüedad")
    print("3. Mostrar empleados ordenados por legajo")
    print("4. Buscar empleado por nombre")
    print("5. Agregar empleado")
    print("6. Modificar empleado")
    print("7. Eliminar empleado")
    print("8. Salir")

    opcion = input("Elegí una opción (1-8): ")

    if opcion == "1":
        ordenar_empleados(empleados, "nombre")
        mostrar_lista()
    elif opcion == "2":
        ordenar_empleados(empleados, "antiguedad")
        mostrar_lista()
    elif opcion == "3":
        ordenar_empleados(empleados, "legajo")
        mostrar_lista()
    elif opcion == "4":
        nombre = input("Nombre del empleado a buscar: ")
        resultado = buscar_empleado(nombre)
        if resultado:
            print(f"Empleado encontrado: {resultado['nombre']} - {resultado['sector']} - Legajo {resultado['legajo']} - {resultado['antiguedad']} años")
        else:
            print("Empleado no encontrado.")
    elif opcion == "5":
        agregar_empleado()
    elif opcion == "6":
        modificar_empleado()
    elif opcion == "7":
        eliminar_empleado()
    elif opcion == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intentalo de nuevo.")
