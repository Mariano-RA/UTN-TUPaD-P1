def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def valor_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return valor_fibonacci(n - 1) + valor_fibonacci(n - 2)

def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

def calcular_binario(n):
    if n == 0:
        return ""
    else:
        return calcular_binario(n // 2) + str(n % 2)

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    if len(palabra) <= 1:
        return True
    else:
        return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return 1 + contar_bloques(n // 10)

def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)



def ejercicio_1(n):
    for i in range(1, n+1):
        print(f"Factorial de {i} es: {factorial(i)}")

def ejercicio_2(n):
    print(f"Serie de Fibonacci hasta la posición {n}")
    for i in range(n+1):
        print(f"Fibonacci de {i} es: {valor_fibonacci(i)}")

def ejercicio_3(base, exponente):
    print(f"{base} elevado a {exponente} es: {calcular_potencia(base, exponente)}")

def ejercicio_4(n):
    print(f"El numero {n} en binario es: {calcular_binario(n)}")

def ejercicio_5(palabra):
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo")

def ejercicio_6(n):
    print(f"La suma de los digitos de {n} es: {suma_digitos(n)}")

def ejercicio_7(n):
    print(f"El nivel mas bajo de la piramide tiene {n} bloques y el total de bloques a utilizar es: {contar_bloques(n)}")

def ejercicio_8(numero, digito):    
    cantidad = contar_digito(numero, digito)
    print(f"El digito {digito} aparece {cantidad} veces en el numero {numero}.")



def menu():
    print("\n=== Menú de Ejercicios ===")
    print("1. Ejericio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Salir")
    opcion = input("Elige el ejercicio a ejecutar: ")
    return opcion


def main():
    while True:
        opcion = menu()

        if opcion == "1":
            n = int(input("Ingrese un numero entero positivo: "))
            ejercicio_1(n)

        elif opcion == "2":
            n = int(input("Ingrese la posición para la serie Fibonacci: "))
            ejercicio_2(n)

        elif opcion == "3":
            base = int(input("Ingrese la base: "))
            exponente = int(input("Ingrese el exponente: "))
            ejercicio_3(base, exponente)

        elif opcion == "4":
            n = int(input("Ingrese el numero que desea convertir a binario: "))
            ejercicio_4(n)

        elif opcion == "5":
            palabra = input("Palabra elegida para chequear si es palindromo: ")
            ejercicio_5(palabra)

        elif opcion == "6":
            n = int(input("Ingrese el numero al que quieres sumarle todos los digitos: "))
            ejercicio_6(n)

        elif opcion == "7":
            n = int(input("Ingrese la cantidad de bloques que tiene la base: "))
            ejercicio_7(n)

        elif opcion == "8":
            numero = int(input("Ingrese un numero entero positivo: "))
            digito = int(input("Ingrese un digito a buscar: "))
            if digito < 0 or digito > 9:
                print("El digito debe ser un numero entre 0 y 9")
            else:
                ejercicio_8(numero, digito)

        elif opcion == "9":
            print("Nos vemos!")
            break

        else:
            print("Opcion invalida!.")


if __name__ == "__main__":
    main()
