# En esta ocasión realizaremos un generador de contraseñas seguras para cualquier log in o sign up.
# El siguiente código en python es de libre uso.
# Visita http://zackdev.atwebpages.com para conocerme más a fondo 
# ZACKDEV

import random
import string

def generate_password(length):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    passwd = ''.join(random.choice(caracteres) for i in range(length))
    return passwd

def generate_alfapassword(longitud):
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena


longitud = int(input("Ingresa la longitud deseada para la contraseña: "))
opcion = input("¿Quieres que la contraseña tenga signos de puntuación? (Sí/No): ")

nueva_contrasena=None

if opcion.lower() == "sí" or opcion.lower() == "si" or opcion.lower() == "s":
    nueva_contrasena = generate_password(longitud)
elif opcion.lower() == "no" or opcion.lower() == "n" :
    nueva_contrasena = generate_alfapassword(longitud)
elif nueva_contrasena==None:
    print("NO se ha podido crear su contraseña: ERROR en la introducción de datos")
else:
    print("Error, introducción inválida")
    
    

print(f"Tu nueva contraseña es: {nueva_contrasena}")