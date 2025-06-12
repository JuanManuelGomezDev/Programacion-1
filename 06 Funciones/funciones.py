
### 1


def imprimir_hola_mundo():
    print("Hola mundo")

imprimir_hola_mundo()





### 2

def saludar_usuario(nombre):
    print("Hola", nombre)

saludar_usuario("juan")


###  3

def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy", nombre, apellido,"tengo", edad,"y vivo en", residencia)

nombre = input("Decime tu nombre: ")
apellido = input("Decime tu apellido: ")
edad = input("Decime tu edad: ")
residencia = input("Decime tu residencia: ")

informacion_personal(nombre, apellido, edad, residencia)



### 4
 

def calcular_area_circulo(radio):
    return 3.14 * (radio ** 2)


def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = float(input("Ingresa el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area}")

print(f"El area del circulo es: {perimetro}")



### 5

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresa la cantidad de segundos "))

total = segundos_a_horas(segundos)

print(f"Tus {segundos} equivalen a {total} de horas")


### 6 

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


### 7

def operaciones_basicas(a, b):
    print(f"El total de {a} + {b} es: ", a+b)
    print(f"El total de {a} * {b} es: ", a*b)
    print(f"El total de {a} - {b} es: ", a-b)
    print(f"El total de {b} - {a} es: ", b-a)
    print(f"El total de {a} / {b} es: ", a/b)
    print(f"El total de {b} / {a} es: ", b/a)
    
primer_num = int(input("Ingresa el primer numero: "))
segundo_num = int(input("Ingresa el segundo numero: "))

tupla = operaciones_basicas(primer_num, segundo_num)

print(tupla)




### 8

def calcular_imc(peso, altura):
    
    return peso / (altura ** 2)

peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))

total = calcular_imc(peso, altura)

print(f"Tu IMC es: {total:.2f}")



### 9 

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = int(input("Ingresa los grados celsius: "))

conversion = celsius_a_fahrenheit(celsius)

print(f"{celsius} equivalen a {conversion} grados fahrenheit")


### 10 

def calcular_promedio(a, b, c):
    total = a+b+c
    return total / 3 

nota1 = int(input("Ingresa el primer numero: "))
nota2 = int(input("Ingresa el segundo numero: "))
nota3 = int(input("Ingresa el tercer numero: "))

promedio = calcular_promedio(nota1, nota2, nota3)

print(f"El promedio de tus 3 numeros es {promedio}")