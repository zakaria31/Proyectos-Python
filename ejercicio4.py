#primero he instalado requests con pip install requests
import requests
import re

def contar_palabras_en_url(url):
    try:
        # Realizar una solicitud GET a la URL
        response = requests.get(url)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Obtener el contenido del archivo
            contenido = response.text
            
            # Contar palabras usando expresiones regulares
            palabras = re.findall(r'\b\w+\b', contenido)
            num_palabras = len(palabras)
            
            print(f"El número de palabras en el archivo de la URL {url} es: {num_palabras}")
        else:
            print("No se pudo acceder al archivo en la URL. Verifica que la URL sea válida.")
    except Exception as e:
        print(f"ERROR: {str(e)}")

# URL del archivo en línea
url = "https://aules.edu.gva.es/fp/mod/resource/view.php?id=4213499"  # Reemplaza esto con la URL real del archivo

contar_palabras_en_url(url)
