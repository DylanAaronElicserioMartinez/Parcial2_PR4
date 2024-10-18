print(" ")#imprime un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control1179")#imprime mi nombre mi grado y grupo con mi numero de control
print(" ")#imprime un espacio en blanco
# Función para crear un diccionario de traducción
def crear_diccionario(input_string):
    diccionario = {}  # Inicializa un diccionario vacío
    # Separa los pares de traducción por comas
    pares = input_string.split(',')
    for par in pares:
        # Separa cada par por ':'
        español, inglés = par.split(':')
        # Agrega la palabra y su traducción al diccionario
        diccionario[español.strip()] = inglés.strip()
    return diccionario  # Devuelve el diccionario creado

# Función para traducir una frase
def traducir_frase(diccionario, frase):
    # Separa la frase en palabras
    palabras = frase.split()
    traduccion = []  # Lista para almacenar la traducción
    for palabra in palabras:
        # Traduce la palabra o deja sin traducir si no está en el diccionario
        traduccion.append(diccionario.get(palabra, palabra))
    return ' '.join(traduccion)  # Une las palabras traducidas en una cadena

# Solicita al usuario que introduzca las traducciones
input_string = input("Introduce las traducciones (ejemplo: 'hola:hello, adiós:goodbye'): ")
diccionario = crear_diccionario(input_string)  # Crea el diccionario

# Solicita al usuario que introduzca una frase en español
frase = input("Introduce una frase en español para traducir: ")
traduccion = traducir_frase(diccionario, frase)  # Traduce la frase

# Muestra la traducción resultante
print("Traducción:", traduccion)
