import math

def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    if b != 0:
        division = a / b
    else:
        division = "Division por cero"

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicacion: {multiplicacion}")
    print(f"Division: {division}")


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

def menu():
    print("\n=== Menú de Ejercicios ===")
    print("1. Imprimir 'Hola Mundo!'")
    print("2. Saludar usuario")
    print("3. Informacion personal")
    print("4. Calcular area y perimetro del circulo")
    print("5. Convertir segundos a horas")
    print("6. Mostrar tabla de multiplicar")
    print("7. Operaciones basicas (suma, resta, multiplicacion, division)")
    print("8. Calcular IMC")
    print("9. Convertir Celsius a Fahrenheit")
    print("10. Calcular promedio de tres numeros")
    print("11. Salir")
    opcion = input("Elige una opción: ")
    return opcion

def main():
    while True:
            opcion = menu()
            
            if opcion == "1":
                imprimir_hola_mundo()

            elif opcion == "2":
                nombre = input("Ingresa tu nombre: ")
                print(saludar_usuario(nombre))

            elif opcion == "3":
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apellido: ")
                edad = int(input("Ingresa la edad: "))
                residencia = input("Ingresa la residencia: ")
                infoPers = informacion_personal(nombre, apellido, edad, residencia)
                print(infoPers)

            elif opcion == "4":
                radio = float(input("Ingresa el radio del circulo: "))
                print(f"Area: {calcular_area_circulo(radio)}")
                print(f"Perimetro: {calcular_perimetro_circulo(radio)}")

            elif opcion == "5":
                segundos = int(input("Ingresa la cantidad de segundos: "))
                print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

            elif opcion == "6":
                numero = int(input("Ingresa el numero para mostrar su tabla de multiplicar: "))
                tabla_multiplicar(numero)

            elif opcion == "7":
                a = float(input("Ingresa el primer numero: "))
                b = float(input("Ingresa el segundo numero: "))
                operaciones_basicas(a, b)

            elif opcion == "8":
                peso = float(input("Ingresa el peso (kg): "))
                altura = float(input("Ingresa la altura (m): "))
                imc = calcular_imc(peso, altura)
                print(f"Tu IMC es: {imc}")

            elif opcion == "9":
                celsius = float(input("Ingresa la temperatura en Celsius: "))
                fahrenheit = celsius_a_fahrenheit(celsius)
                print(f"{celsius}°C es igual a {fahrenheit}°F")

            elif opcion == "10":
                a = float(input("Ingresa el primer numero: "))
                b = float(input("Ingresa el segundo numero: ")) 
                c = float(input("Ingresa el tercer numero: "))
                promedio = calcular_promedio(a, b, c)
                print(f"El promedio de los numeros {a}, {b} y {c} es: {promedio}")

            elif opcion == "11":
                print("Nos vemos!")
                break
            
            else:
                print("Opcion invalida!.")

if __name__ == "__main__":
    main()