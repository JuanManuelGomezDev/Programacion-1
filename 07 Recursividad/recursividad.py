###############  1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Ingresa un numero: "))
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")



############### 2

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)


n = int(input("Ingresa la posicion de Fibonacci: "))
for i in range(n):
    print(f"F({i}) = {fibonacci(i)}")



############### 3



def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")



############### 4

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)


num = int(input("Tu nmero decimal: "))
binario = decimal_a_binario(num)
print(f"Binario: {binario if binario else '0'}")

############# 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Palabra: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))

########### 6

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

num = int(input("Número: "))
print("Suma de dígitos:", suma_digitos(num))

########## 7

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("Bloques en el nivel más bajo: "))
print("Total de bloques:", contar_bloques(niveles))


########## 8


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)

num = int(input("Número: "))
dig = int(input("Dígito a contar: "))
print("Cantidad de veces:", contar_digito(num, dig))



