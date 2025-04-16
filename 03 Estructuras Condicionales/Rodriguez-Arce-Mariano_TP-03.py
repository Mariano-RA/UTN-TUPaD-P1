from statistics import mode, median, mean
import random

print("1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga 'Es mayor de edad'")

edad = int(input("Ingrese su edad: "))
if(edad > 18):
    print("Es mayor de edad")
else:
    print("Es menor de edad")

print("\n\n2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga 'Aprobado'; en caso contrario deberá mostrar el mensaje 'Desaprobado'")

nota_usuario = float(input("Ingrese la nota del usuario: "))

if(nota_usuario >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

print("\n\n3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje 'Ha ingresado un número par'; en caso contrario, imprimir por pantalla 'Por favor, ingrese un número par'. Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.")

numero_ingresado = int(input("Ingrese el numero: "))
if(numero_ingresado % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


print("\n\n4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:\n\t● Niño/a: menor de 12 años. \n\t● Adolescente: mayor o igual que 12 años y menor que 18 años. \n\t● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.\n\t● Adulto/a: mayor o igual que 30 años.")

edad_ingresada = int(input("Ingrese la edad del usuario: "))
if(edad_ingresada > 0 and edad_ingresada < 12):
    print("Usted pertenece a la categoría: Niño/a")
elif(edad_ingresada >= 12 and edad_ingresada < 18):
    print("Usted pertenece a la categoría: Adolescente")
elif(edad_ingresada >= 18 and edad_ingresada < 30):
    print("Usted pertenece a la categoría: Adulto/a joven")
elif(edad_ingresada > 30):
    print("Usted pertenece a la categoría: Adulto/a")
else:
    print("Ingrese un número mayor que 0")

print("\n\n5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje 'Ha ingresado una contraseña correcta'; en caso contrario, imprimir por pantalla 'Por favor, ingrese una contraseña de entre 8 y 14 caracteres'. Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.")

contrasena_ingresada = input("Ingrese la contraseña: ")
if(len(contrasena_ingresada) >= 8 and len(contrasena_ingresada) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print("\n\n6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.")

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if(media > mediana and mediana > moda):
    print("Sesgo positivo o a la derecha")
elif(media < mediana and mediana < moda):
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

print("\n\n7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.")

frase_ingresada = input("Ingrese una frase o palabra: ")
ultima_letra = frase_ingresada[-1]

if(ultima_letra.lower() in ['a','e','i','o','u']):
    frase_ingresada = frase_ingresada + '!'
    print(frase_ingresada)
else:
    print(frase_ingresada)

print("\n\n8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:")

nombre_ingresado = input("Ingresa el nombre: ")
print("Ingresa la opcion que desees: ")
print(" 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO." )
print(" 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro." )
print(" 3. Si quiere su nombre con la primera letra mayúscula. ")
opcion_deseada = int(input("Opcion: "))

if(opcion_deseada == 1):
    print(nombre_ingresado.upper())
elif(opcion_deseada == 2):
    print(nombre_ingresado.lower())
elif(opcion_deseada == 3):
    print(nombre_ingresado.capitalize())
else:
    print("Opcion invalida.")


print("\n\n9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla.")

magnitud_ingresada = int(input("Ingrese la magnitud del terremoto: "))
if(magnitud_ingresada < 3):
    print('Categoría: "Muy leve" (imperceptible)')
elif(magnitud_ingresada >= 3 and magnitud_ingresada < 4):
    print('Categoría: "Leve" (ligeramente perceptible)')
elif(magnitud_ingresada >= 4 and magnitud_ingresada < 5):
    print('Categoría: "Moderado" (sentido por personas, pero generalmente no causa daños)')
elif(magnitud_ingresada >= 5 and magnitud_ingresada < 6):
    print('Categoría: "Fuerte" (puede causar daños en estructuras débiles)')
elif(magnitud_ingresada >= 6 and magnitud_ingresada < 7):
    print('Categoría: "Muy Fuerte" (puede causar daños significativos)')
else:
    print('Categoría: "Extremo" (puede causar graves daños a gran escala)')


print("\n\nEscribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.")

hemisferio = input("Ingrese en cuál hemisferio se encuentra (N/S): ")
mes = int(input("Ingrese que mes del año es: "))
dia = int(input("Ingrese que dia del año es: "))

fecha = (mes, dia)

if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"
