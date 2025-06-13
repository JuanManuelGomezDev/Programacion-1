############# 1


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}


precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


############# 2



precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


############# 3 

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)



############ 4

agenda = {}

for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero de telefono: ")
    agenda[nombre] = numero

consulta = input("¿A quien querés buscar?: ")

if consulta in agenda:
    print("Numero:", agenda[consulta])
else:
    print("No se encontr el contacto.")


########### 5

frase = input("Ingrese una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras nicas:", palabras_unicas)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Conteo de palabras:", conteo)

########## 6

alumnos = {}

for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingres la nota {i+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de {promedio}")

############ 7


parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobo solo uno:", parcial1 ^ parcial2)
print("Aprobo al menos uno:", parcial1 | parcial2)


########## 8

stock = {}

producto = input("Producto a consultar o agregar: ")

if producto in stock:
    agregar = int(input("¿Cuntas unidades queres agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto nuevo. ¿Cuantas unidades tiene?: "))
    stock[producto] = nuevo_stock

print("Stock actual:", stock)

########### 9

agenda = {}

for _ in range(3):
    dia = input("Dia del evento: ")
    hora = input("Hora del evento: ")
    evento = input("Descripcion del evento: ")
    agenda[(dia, hora)] = evento

print("Agenda completa:")
for clave, valor in agenda.items():
    print(f"{clave}: {valor}")


######### 10

paises = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Uruguay': 'Montevideo'}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)



