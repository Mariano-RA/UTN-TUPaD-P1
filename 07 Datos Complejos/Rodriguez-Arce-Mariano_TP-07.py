precios_frutas = {'banana': 1200, 'anana': 2500, 'melon': 3000, 'uva': 1450}
listado_frutas = []
numeros_telefonicos = {'mariano': '123456789', 'ana': '987654321', 'luis': '456789123', 'pedro': '321654987', 'laura': '789123456'}
palabras_unicas = set()
alumnos = {}
productos_stock = {'mouse': 10, 'teclado': 5, 'monitor': 2, 'cpu': 8}
agenda = {
    ('lunes', '9:00'): 'Reunión con el equipo',
    ('martes', '10:30'): 'Cita médica',
    ('miercoles', '14:00'): 'Clase de yoga',
    ('jueves', '11:00'): 'Reunión de proyecto',
    ('viernes', '15:00'): 'Cita con el dentista'
}
paises_capitales = {
    'argentina': 'buenos aires',
    'brasil': 'brasilia',
    'chile': 'santiago',
    'colombia': 'bogotá',
    'peru': 'lima'
    }

def mostrar_frutas():
    print("\n=== Lista de Frutas con precio ===")
    for fruta, precio in precios_frutas.items():
        print(f"{fruta.capitalize()}: ${precio}")

def agregar_frutas():
    global precios_frutas
    precios_frutas['naranja'] = 1200
    precios_frutas['manzana'] = 1500
    precios_frutas['pera'] = 2300
    mostrar_frutas()

def modificar_precios():
    global precios_frutas
    precios_frutas['banana'] = 1330
    precios_frutas['manzana'] = 1700
    precios_frutas['melon'] = 2800
    mostrar_frutas()

def listar_frutas():
    global listado_frutas 
    listado_frutas = list(precios_frutas.keys())
    print("\n=== Frutas Disponibles ===")
    for fruta in listado_frutas:
        print(fruta.capitalize())

def agregar_numero_telefonico(cantidad):
    global numeros_telefonicos
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
        numero = input(f"Ingrese el numero telefonico de {nombre}: ")
        if nombre.lower() in numeros_telefonicos:
            print(f"El numero de {nombre} ya existe. Actualizando el numero.")
        else:
            print(f"Agregando numero de {nombre}.")
        numeros_telefonicos[nombre.lower()] = numero

def obtener_numero_telefonico(nombre):
    if nombre.lower() in numeros_telefonicos:
        print(f"El numero de {nombre} es: {numeros_telefonicos[nombre.lower()]}")
    else:
        print(f"No se encontró el número de {nombre}.")

def contador_palabras(palabras):
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    print("\n=== Contador de Palabras ===")
    for palabra, cantidad in contador.items():
        print(f"{palabra}: {cantidad}")

def set_palabras_unicas(frase):
    palabras = frase.split()
    palabras_unicas = set(palabras)
    print("\n=== Palabras únicas en la frase ===")
    print(palabras_unicas)
    contador_palabras(palabras)
    
def agregar_alumno_notas():
    global alumnos
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno: ")
        notas = []
        for j in range(3):
            nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
            notas.append(nota)

        alumnos[nombre.lower()] = tuple(notas)   
    print("\n=== Alumnos y sus Promedios ===")
    for alumno, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{alumno.capitalize()}: {promedio:.2f}")

def lista_aprobados(lista1, lista2):
    set_alumnos = set(lista1)
    set_alumnos_2 = set(lista2)
    
    ambos_parciales_aprobados = set_alumnos.intersection(set_alumnos_2)
    algun_parcial_aprobado = set_alumnos.union(set_alumnos_2)
    un_parcial_aprobado = set_alumnos.symmetric_difference(set_alumnos_2)

    print("\n=== Alumnos que aprobaron ambos parciales ===")
    for alumno in ambos_parciales_aprobados:
        print(alumno)
    print("\n=== Alumnos que aprobaron al menos un parcial ===")
    for alumno in algun_parcial_aprobado:
        print(alumno)
    print("\n=== Alumnos que aprobaron un parcial===")
    for alumno in un_parcial_aprobado:
        print(alumno)

def agregar_producto_stock(producto):
    global productos_stock
    cantidad = int(input("Ingrese la cantidad de stock: "))
    productos_stock[producto] = cantidad
    print(f"Producto {producto.capitalize()} agregado con éxito. Stock actual: {productos_stock[producto]}")

def modificar_stock_producto(producto):
    global productos_stock
    cantidad = int(input("Ingrese la nueva cantidad de stock: "))
    productos_stock[producto] = cantidad
    print(f"Stock de {producto.capitalize()} modificado a {cantidad}.")

def consultar_stock_producto():
    global productos_stock
    print("\n=== Productos ===")
    for producto in productos_stock.keys():
        print(f"{producto.capitalize()}")

    producto = input("Ingrese el nombre del producto a consultar: ").lower()
    if producto in productos_stock:
        print(f"El stock de {producto.capitalize()} es: {productos_stock[producto]}")
        actualizar_stock = input("¿Desea modificar el stock? (s/n)").lower()
        if actualizar_stock == 's':
            modificar_stock_producto(producto)
    else:
        print(f"El producto {producto.capitalize()} no se encuentra en el stock.")
        agregar_producto = input("¿Desea agregarlo al stock? (s/n)").lower()
        if agregar_producto == 's':
            agregar_producto_stock(producto)

def consultar_agenda():
    dia = input("Ingrese el día de la semana: ")
    hora = input("Ingrese la hora (formato HH:MM): ")
    evento = agenda.get((dia.lower(), hora))
    if evento:
        print(f"Evento programado para {dia} a las {hora}: {evento}")
    else:
        print(f"No hay eventos programados para {dia} a las {hora}.")

def invertir_diccionario():
    global paises_capitales
    print("\n=== Diccionario Original (Países a Capitales) ===")
    for pais, capital in paises_capitales.items():
        print(f"{pais.capitalize()}: {capital.capitalize()}")

    paises_invertidos = {capital: pais for pais, capital in paises_capitales.items()}
    print("\n=== Diccionario Invertido (Capitales a Países) ===")
    for capital, pais in paises_invertidos.items():
        print(f"{capital.capitalize()}: {pais.capitalize()}")


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
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Salir")
    opcion = input("Elige el ejercicio a ejecutar: ")
    return opcion


def main():
    while True:
        opcion = menu()

        if opcion == "1":
            agregar_frutas()

        elif opcion == "2":
            modificar_precios()

        elif opcion == "3":
            listar_frutas()
            
        elif opcion == "4":
            cantidad = int(input("Ingrese la cantidad de contactos a agregar: "))
            agregar_numero_telefonico(cantidad)
            nombre = input("Ingrese el nombre del contacto para buscar su numero telefonico: ")
            obtener_numero_telefonico(nombre)            

        elif opcion == "5":
            frase = input("Ingrese una frase para contar palabras: ")
            set_palabras_unicas(frase)

        elif opcion == "6":
            agregar_alumno_notas()

        elif opcion == "7":
            lista1 = input("Ingrese los nombres de los alumnos que aprobaron el primer parcial (separados por comas): ").split(',')
            lista2 = input("Ingrese los nombres de los alumnos que aprobaron el segundo parcial (separados por comas): ").split(',')

            lista_aprobados(lista1, lista2)

        elif opcion == "8":
            consultar_stock_producto()

        elif opcion == "9":
            consultar_agenda()
        
        elif opcion == "10":
            invertir_diccionario()

        elif opcion == "11":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida!.")


if __name__ == "__main__":
    main()
