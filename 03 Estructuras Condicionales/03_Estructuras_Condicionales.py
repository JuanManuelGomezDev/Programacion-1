## EJERCICIO 1
""""
edad = int(input("Ingresa tu edad:"))
if edad >= 18 :

    print("Sos mayor de edad")

"""


## EJERCICIO 2
"""
nota = int(input("Ingresa tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")"
    """

## EJERCICIO 3
"""
numero = int(input('ingrese un numero: '))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print('Por favor, ingrese un numero par')
"""
## EJERCICIO 4
"""
edad = int(input('Ingresa tu edad: '))

if edad < 12:
    print('Chico.')
elif edad >= 12 and edad < 18:
    print('Adolescente.')
elif edad >= 18 and edad < 30:
    print('Adulto/Joven.')
elif edad >= 30:
    print('Adulto.')
"""
## EJERCICIO 5 
"""
contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
"""

# EJERCICIO 7
"""
frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
    
print(frase)
"""
# EJERCICIO 8

nombre = input("Ingrese su nombre: ")
opcion = input("Elija una opción (1: mayúsculas, 2: minúsculas, 3: primera letra en mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")
