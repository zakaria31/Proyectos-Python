def mostrar_tablaMultiplicar(numero):
    # Verificar si el número está entre el 1 y 10
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return
    
    nombre_archivo = f"tabla-{numero}.txt"
    
    try:
        # Abrimos el archivo en modo lectura
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Tabla de multiplicar del número {numero}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe. Debes crear la tabla de multiplicar de ese número.")

# Pedimos al usuario un número
try:
    numero = int(input("Introduce un número entero entre 1 y 10: "))
    mostrar_tablaMultiplicar(numero)
    
    #recogemos la excepción para que cuando dé error al introducir algo que no sea un numero no lo acepte y muestre un mensaje.
except ValueError:
    print("ERROR!!! Introduzca un número válido.")
