import random

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]|;:',.<>?/~`"

random_alfabeto = list(alfabeto)
random.shuffle(random_alfabeto)
random_alfabeto = "".join(random_alfabeto)

def generar_desplazamientos(clave, longitud):
    desplazamientos = []
    for i in range(longitud):
        desplazamientos.append(ord(clave[i % len(clave)]) % len(alfabeto))
    return desplazamientos

def cifrado_cesar_modificado(texto, clave):
    texto_cifrado = ""
    desplazamientos = generar_desplazamientos(clave, len(texto))
    for i, caracter in enumerate(texto):
        if caracter in alfabeto:
            indice = alfabeto.index(caracter)
            nuevo_caracter = random_alfabeto[(indice + desplazamientos[i]) % len(alfabeto)]
            texto_cifrado += nuevo_caracter
        else:
            texto_cifrado += caracter
    return texto_cifrado

def descifrado_cesar_modificado(texto_cifrado, clave):
    texto_descifrado = ""
    desplazamientos = generar_desplazamientos(clave, len(texto_cifrado))
    for i, caracter in enumerate(texto_cifrado):
        if caracter in random_alfabeto:
            indice = random_alfabeto.index(caracter)
            nuevo_caracter = alfabeto[(indice - desplazamientos[i]) % len(alfabeto)]
            texto_descifrado += nuevo_caracter
        else:
            texto_descifrado += caracter
    return texto_descifrado

secreto = "Hola, este es un mensaje secreto!"
clave = "PYTHON"

texto_cifrado = cifrado_cesar_modificado(secreto, clave)
print("\nTexto cifrado:", texto_cifrado)

texto_descifrado = descifrado_cesar_modificado(texto_cifrado, clave)
print("\nTexto descifrado:", texto_descifrado)