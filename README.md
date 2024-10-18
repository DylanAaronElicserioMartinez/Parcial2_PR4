# Parcial2_PR4
Actividad en clase


#Codigo 1

print(" ")#imprime un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control1179")#imprime mi nombre mi grado y grupo con mi numero de control

print(" ")#imprime un espacio en blanco

dic = {#crear un diccionario en blanco

}#cerrar diccionario

n=input("Ingresa tu nombre:")#pide al usuario ingresar su nombre

e=input("Ingresa tu edad:")#pide al usuario ingresar su edad

s=input("Ingresa tu sexo:")#pide al usuario ingresar su sexo

t=input("Ingresa tu numero de telefono:")#pide al usuario ingresar su numero de telefono

c=input("ingresa tu correo electronico:")#pide al usuario ingresar su correo

dic["Nombre"] = n#lo anterior mente pedido lo agrega en el diccionario

dic["Edad"] = e#lo anterior mente pedido lo agrega en el diccionario

dic["Sexo"] = s#lo anterior mente pedido lo agrega en el diccionario

dic["Telefono"] = t#lo anterior mente pedido lo agrega en el diccionario

dic["Correo"] = c#lo anterior mente pedido lo agrega en el diccionario

print(dic)#imprime el diccionario

![image](https://github.com/user-attachments/assets/ecab3972-6377-406e-a1ca-fdf3fb6f4298)

![image](https://github.com/user-attachments/assets/a20bab72-38cd-4824-90f8-20744b23cd97)


#Codigo 2

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

![image](https://github.com/user-attachments/assets/bce6968d-f830-4a3a-9c57-705e1d366544)


![image](https://github.com/user-attachments/assets/54ff594c-f7b7-4fab-b116-e7ebec46c4b8)
