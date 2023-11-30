def mostrar_linea_de_tabla(n, m):

    # Verificar si los números están entre el 1 y 10
    if n < 1 or n > 10 or m < 1 or m > 10:
        print("Los números deben estar entre 1 y 10.")
        return
    
    nombre_archivo = f"tabla-{n}.txt"
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if len(lineas) >= m:
                linea = lineas[m - 1]  # El índice es m - 1 ya que las listas comienzan en 0
                print(f"Línea {m} de la tabla de multiplicar del número {n}:\n{linea}")
            else:
                print(f"La línea {m} no existe en la tabla de multiplicar del número {n}.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe. Debes crear la tabla de multiplicar para ese número primero.")

# Pedimos al usuario los dos números
try:
    n = int(input("Introduce el primer número (entre 1 y 10): "))
    m = int(input("Introduce el segundo número (entre 1 y 10): "))
    mostrar_linea_de_tabla(n, m)
    #recogemos la excepción para que cuando dé error al introducir algo que no sea un numero no lo acepte y muestre un mensaje.
except ValueError:
    print("Debes introducir números  válidos.")
