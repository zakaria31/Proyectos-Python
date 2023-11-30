def tablaMultiplicar(numero):

    # Verificamos si el número está entre el 1 y 10

    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return
    

    nombre_archivo = f"tabla_de_{numero}.txt"

    try:
        # Abrimos el archivo en modo escritura
        with open(nombre_archivo, 'w') as archivo:
            # Escribimos la tabla de multiplicar en el archivo
            for i in range(1, 11):
                resultado = numero * i
                archivo.write(f"{numero} x {i} = {resultado}\n")

        print(f"La tabla de multiplicar del número {numero} ha sido guardada en {nombre_archivo}")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {str(e)}")

# Pedimos al usuario un número valido
try:
    numero = int(input("Introduce un número entero entre 1 y 10: "))
    tablaMultiplicar(numero)
    #recogemos la excepción para que cuando dé error al introducir algo que no sea un numero no lo acepte y muestre un mensaje.
except ValueError:
    print("ERROR!!! Debes introducir un número entero válido.")
