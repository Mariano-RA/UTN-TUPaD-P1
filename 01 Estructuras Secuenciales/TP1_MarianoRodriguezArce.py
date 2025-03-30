# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("1) Crear un programa que imprima por pantalla el mensaje: Hola Mundo!.")
print("Hola Mundo!")
print("\n\n")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

print("2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.")
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")
print("\n\n")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

print("3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.")
nombre3 = input("Ingresa tu nombre: ")
apellido3 = input("Ingresa tu apellido: ")
edad3 = input("Ingresa tu edad: ")
residencia3 = input("Ingresa tu lugar de residencia: ")

print(f"Soy {nombre3} {apellido3}, tengo {edad3} años y vivo en {residencia3}")
print("\n\n")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

print("4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.")
radio4 = float(input("Ingresa el radio del circulo: "))
perimetro = (radio4 * 2) * 3.14
area = 3.14 * (radio4**2)

print(f"El area del circulo es: {area} \nEl perimetro del circulo es: {perimetro}")
print("\n\n")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

print("5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.")
segundos5 = int(input("Ingrese la cantidad de segundos: "))
horas5 = segundos5 / 3600

print(f"{segundos5} segundos equivalen a {horas5} horas")
print("\n\n")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

print("6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.")
numero6 = int(input("Ingresa el numero: "))
for i in range(1,11):
    multiplicacion = numero6 * i
    print(f"{numero6} * {i} = {multiplicacion}")
print("\n\n")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.")
primerNum7 = int(input("Ingresa el primer numero: "))
segundoNum7 = int(input("Ingresa el segundo numero: "))

suma = primerNum7 + segundoNum7
resta = primerNum7 - segundoNum7
multiplicacion = primerNum7 * segundoNum7
division = primerNum7 / segundoNum7

print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")
print(f"El resultado de la division es: {division}")
print("\n\n")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

print("8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.")
altura8 = float(input("Ingrese su altura en metros: "))
peso8 = float(input("Ingrese su peso: "))

imc8 = peso8 / (altura8 ** 2)
print(f"Su indice de masa corporal es: {imc8}")
print("\n\n")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 

print("9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. ")
gradosCelsius9 = float(input("Ingrese la temperatura en grados celsius: "))
gradosFahrenheit9 = (9/5 * gradosCelsius9) + 32

print(f"{gradosCelsius9} grados celsius equivalen a {gradosFahrenheit9} grados fahrenheit")
print("\n\n")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

print("10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.")
num1_10 = float(input("Ingresa el primer numero: "))
num2_10 = float(input("Ingresa el segundo numero: "))
num3_10 = float(input("Ingresa el tercer numero: "))

promedio_10 = (num1_10 + num2_10 + num3_10) / 3
print(f"El promedio de los numeros {num1_10}, {num2_10} y {num3_10} es: {promedio_10}")