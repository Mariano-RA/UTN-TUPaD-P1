import random

print("1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.")

for i in range(0, 100):
    print(i)

print("2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.")

enteroIngresado = int(input("Ingresa un numero: "))
enteroAbsoluto = str(abs(enteroIngresado))
contadorDigitos = 0

for i in range(len(enteroAbsoluto)):
    contadorDigitos +=1
print(f"El numero {enteroIngresado} tiene {contadorDigitos} digitos")


print("3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores ")

primerNumero = abs(int(input("Ingresa el primer numero del rango: ")))
segundoNumero = abs(int(input("Ingresa el segundo numero del rango: ")))
acumulador = 0

inicio = min(primerNumero, segundoNumero) + 1
fin = max(primerNumero, segundoNumero)

for i in range(inicio, fin):
    acumulador += i

print(f"La suma entre los valores es: {acumulador}")


print("4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.")

acumulador_ej_4 = 0

while True:
    numeroIngresado_ej_4 = int(input("Ingresa el numero que quieras sumar: "))
    if(numeroIngresado_ej_4 == 0):
        break
    acumulador_ej_4 += numeroIngresado_ej_4

print(f"La suma total de los numeros ingresados es: {acumulador_ej_4}")


print("5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.")

numeroRandom = random.randint(0, 9)
intentos = 0

while True:
    eleccionUsuario = int(input("Ingresa el numero: "))
    intentos += 1
    if(eleccionUsuario == numeroRandom):
        break
print(f"Se necesitaron {intentos} intentos para adivinar el numero!")

print("6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.")

for i in range(100, -1, -1):
    if(i % 2 == 0):
        print(i)


print("7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.")

numeroIngresado_ej7 = int(input("Ingresa un numero entero positivo: "))
suma = 0

for i in range(numeroIngresado_ej7 + 1):
    suma += i
print(f"La suma de todos los numeros en el rango entre 0 y {numeroIngresado_ej7} es: {suma}")


print("8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).")

cantidadPares = 0
cantidadImpares = 0
cantidadPositivos = 0
cantidadNegativos = 0

for i in range(100):
    num = int(input("Ingrese el número: "))
    if num % 2 == 0:
        cantidadPares += 1
    else:
        cantidadImpares += 1
    if num > 0:
        cantidadPositivos += 1
    elif num < 0:
        cantidadNegativos += 1

print(f"Pares: {cantidadPares}")
print(f"Impares: {cantidadImpares}")
print(f"Positivos: {cantidadPositivos}")
print(f"Negativos: {cantidadNegativos}")


print("9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).")

cantidadRepeticiones = 100
sumaTotal = 0

for i in range(cantidadRepeticiones):
    num = int(input("Ingrese el número: "))
    sumaTotal += num

print(f"El promedio total es: {sumaTotal / cantidadRepeticiones}")


print("10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.")

numeroParaInvertir = abs(int(input("Ingrese un numero entero: ")))
invertido = 0

while numeroParaInvertir > 0:
    digito = numeroParaInvertir % 10
    invertido = invertido * 10 + digito
    numeroParaInvertir = numeroParaInvertir // 10

print(f"El numero invertido es: {invertido}")