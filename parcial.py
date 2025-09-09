# EJERCICIO NUMERO 1

# Le pedimos al usuario que ingrerese un numero entero positivo
num = int(input("Por favor ingresar un numero entero positivo:"))

# Creamos una variable para contar cuántos números primos encontramos
num_de_primos = 0

# Recorremos todos los números desde 2 hasta el numero que el usuario ingresado
for i in range(2, num + 1):

    # Ahora verificamos si el número es primo
    Es_primo = True
    for j in range(2, i):
        if i % j == 0:
            Es_primo = False
            break
    if Es_primo:
        print(i)
        num_de_primos += 1

# Mostramos la cantidad de primos encontrados
print("Se encontraron:", num_de_primos, "numeros primos.")

# EJERCICIO NUMERO 2

# Definimos la función con un descuento del 10%
def calcular_descuento(precio, descuento=10):

       # Calculamos el precio con el descuento 
    precio_final = precio - (precio * descuento / 100)
    return precio_final

# Creamos una variable para almacenar el total a pagar
total_a_pagar = 0

#Ahora le pedimos al usuario tres precios de productos
for i in range(3):
    precio_producto = float(input(f"Introduce el precio del producto {i+1}: "))

    #Calculamos el valor a pagar con el descuento
    con_descuento = calcular_descuento(precio_producto)

    # Mostramnos el precion con el descuento aplicado
    print(f"El precio con descuento del producto {i+1} es: {con_descuento:.2f}")

    # Sumamos el precio con descuento al total a pagar
    total_a_pagar += con_descuento
# Mostramos el total a pagar 
print(f"El total que debe pagar por los tres productos es: {total_a_pagar:.2f}")

# EJERCICIO NUMERO 4
def dividir_nums():
    try: 
    #Ahora le pedimos al usuario que ingrese dos numeros enteros
        num1 = int(input("Por favor ingresar el primer numero: "))
        num2 = int(input("Por favor ingresar el segundo numero: "))

        #Calculamos
        resultado = num1 / num2
        print(f"El resultado de la division es: {resultado}")

    except ValueError:
        # Si el usuario ingresa un valor no numérico se mostrara un error
        print("Error: Por favor ingresar números enteros.")
    
    except ZeroDivisionError:
        # Si el usuario intenta dividir entre cero igualmente se mostrara un error
        print("Error: No se puede dividir entre cero.")

# Llamamos a la función para ejecutar el programa
dividir_nums()

# EJERCICIO NUMERO 5
def promedio_notas(estudiantes):

    # Primero calculamos el promedio de las notas de los estudiantes
    if not estudiantes:
        return 0
    total_notas = sum(estudiante['nota'] for estudiante in estudiantes)
    return total_notas / len(estudiantes)

def mejor_estud(estudiantes):
    # Retorna la nota y nombre de mejor estudiante 
    if not estudiantes:
        return None
    mejor = max(estudiantes, key=lambda estudiante: estudiante['nota'])
    return mejor['nombre'], mejor['nota']

def peor_estud(estudiantes):
    # Ahora retornamos el nombre y la nota pero del peor estudiante
    if not estudiantes:
        return None
    peor = min(estudiantes, key=lambda estudiante: estudiante['nota'])
    return peor['nombre'], peor['nota']

def ingresar_estud():
    # Esto nos permite ingresar estudiantes con su nombre y nota
    estudiantes = []
    
    while True:
        nombre = input("Introduzca el nombre del estudiante (escriba 'finalizar' si desea terminar): ")
        if nombre.lower() == 'finalizar':
            break
        
        try:
            nota = float(input(f"Introduce la nota de {nombre}: "))
        except ValueError:
            print("ERROR: La nota ingresada debe ser un número, Intentelo de nuevo")
            continue
        
        estudiantes.append({"nombre": nombre, "nota": nota})
    
    return estudiantes

def imprimir_reporte(estudiantes):
    # Imprime un reporte final con los resultadosde los estudiantes
    if not estudiantes:
        print("Aun no se han ingresado estudiantes")
        return

    # Mostramos el número de estudiantes
    print(f"\nNúmero de estudiantes: {len(estudiantes)}")

    # Calculamos y mostramos el promedio de las notas que se ingresaron
    promedio = promedio_notas(estudiantes)
    print(f"Promedio de notas: {promedio:.2f}")

    # Reflejamos el mejor y peor estudiante
    mejor = mejor_estud(estudiantes)
    if mejor:
        print(f"Mejor estudiante: {mejor[0]} con nota {mejor[1]:.2f}")

    peor = peor_estud(estudiantes)
    if peor:
        print(f"Peor estudiante: {peor[0]} con nota {peor[1]:.2f}")

    # Mostramos los estudiantes ordenados por sus notas
    estudiantes_ordenados = sorted(estudiantes, key=lambda estudiante: estudiante['nota'])
    print("\nEstudiantes ordenados por nota (de menor a mayor):")
    for estudiante in estudiantes_ordenados:
        print(f"Nombre: {estudiante['nombre']}, Nota: {estudiante['nota']:.2f}")


# sistema de gestion de estudiantes
def gestionar_estud():
    estudiantes = ingresar_estud()
    imprimir_reporte(estudiantes)

# Ejecutar el sistema
gestionar_estud()


