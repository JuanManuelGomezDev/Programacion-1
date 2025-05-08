# EJERCICIO 1
"""
for i in range(101):  
    print(i)
"""
# EJERCICIO 2
"""
numero = input("Ingresa un nmero entero: ")


cantidad_digitos = len(numero.lstrip('-'))  

print(f"El numero ingresado tiene {cantidad_digitos} digitos.")
"""
# EJERCICIO 3
"""
primer_valor = int(input("Ingresa el primer valor: "))
segundo_valor = int(input("Ingresa el segundo valor: "))

suma = sum(range(primer_valor + 1, segundo_valor))

print(f"La suma de los números entre {primer_valor} y {segundo_valor} (excluidos) es: {suma}")
"""

# EJERCICIO 4
"""

total = 0

while True:
    
    numero = int(input("Ingresa un número entero (0 para detenerte y mostrar lo acumulado): "))
    
    if numero == 0:
        break
    
    total += numero


print(f"El total acumulado es: {total}")
"""

# EJERCICIO 5
"""
import random


num_secreto = random.randint(0, 9)


intentos = 0


print("¡Bienvenido al juego! Adivina un número entre 0 y 9.")


while True:
    
    adivinanza = int(input("Ingresa un número: "))
    
    
    intentos += 1
    
    
    if adivinanza == num_secreto:
        print(f"¡Felicidades! adivinaste el número en {intentos} intentos.")
        break
    elif adivinanza < num_secreto:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

"""
# EJERCICIO 6

"""
for i in range(100, -1, -2):  
    print(i)
"""

# EJERCICIO 7
"""

numero = int(input("Ingresa un número entero positivo: "))


if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    suma = sum(range(numero + 1))  
    print(f"La suma de los números comprendidos entre 0 y {numero} es: {suma}")

"""
# EJERCICIO 10


numero = input("Ingresa un número: ")


num_invertido = numero[::-1]


print(f"El número invertido es: {num_invertido}")


