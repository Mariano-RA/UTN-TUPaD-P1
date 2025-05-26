
def ejercicio_1():
    return list(range(4, 101, 4))


def ejercicio_2():
    lista = ["Teclado", "Mouse", "Monitor", "Silla", "Escritorio"]
    print(f"La lista es: {lista}")
    print(f"El penúltimo elemento es: {lista[-2]}")


def ejercicio_3():
    lista = []
    lista.append("Gato")
    lista.append("Perro")
    lista.append("Loro")
    print(f"La lista resultante es: {lista}")


def ejercicio_4():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print(f"La lista modificada es: {animales}")

def ejercicio_5():
    print("Lo que se esta realizando en el ejercicio 5 es que de la lista que nos brindan [8, 15, 3, 22, 7] se obtiene el valor mas alto con la funcion max() y luego utilizando la funcion remove() lo elimina de la lista. Por ultimo se muestra en pantalla la lista modificada.")

def ejercicio_6():
    lista = list(range(10, 31, 5))
    print(f"La lista de números del 10 al 30 (incluido) con saltos de 5 es: {lista}")
    print(f"Los dos primeros numeros de la lista son: {lista[:2]}")


def ejercicio_7():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1] = "corsa"
    autos[2] = "focus"
    print(f"La lista modificada de autos es: {autos}")


def ejercicio_8():
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print(f"La lista de dobles es: {dobles}")


def ejercicio_9():
    compras = [
        ["pan", "leche"],
        ["arroz", "fideos", "salsa"],
        ["agua"]
    ]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print(f"La lista de compras modificada es: {compras}")


def ejercicio_10():
    lista_anidada = []
    lista_anidada.append(15)
    lista_anidada.append(True)
    lista_anidada.append([25.5, 57.9, 30.6])
    lista_anidada.append(False)
    print(f"La lista anidada es: {lista_anidada}")


def menu():
    print("\n=== Menú de Ejercicios ===")
    print("1. Lista con los números del 1 al 100 que sean múltiplos de 4")
    print("2. Crear lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.")
    print("3. Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla")
    print("4. Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.")
    print("5. Ejercicio 5")
    print("6. Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros")
    print("7. Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera")
    print("8. Crear una lista vacía llamada 'dobles' y agregar el doble de 5, 10 y 15 usando append directamente")
    print("9. Operaciones con la lista “compras”")
    print("10. Elaborar una lista anidada")
    print("11. Salir")
    opcion = input("Elige una opción: ")
    return opcion


def main():
    while True:
        opcion = menu()

        if opcion == "1":
            ej1 = ejercicio_1()
            print(f"Lista de números del 1 al 100 que son múltiplos de 4 es: {ej1}")

        elif opcion == "2":
            ejercicio_2()

        elif opcion == "3":
            ejercicio_3()

        elif opcion == "4":
            ejercicio_4()

        elif opcion == "5":
            ejercicio_5()

        elif opcion == "6":
            ejercicio_6()

        elif opcion == "7":
            ejercicio_7()

        elif opcion == "8":
            ejercicio_8()

        elif opcion == "9":
            ejercicio_9()

        elif opcion == "10":
            ejercicio_10()

        elif opcion == "11":
            print("Nos vemos!")
            break

        else:
            print("Opcion invalida!.")


if __name__ == "__main__":
    main()
