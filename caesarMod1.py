import random

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

random_alfabeto = list(alfabeto)
random.shuffle(random_alfabeto)
random_alfabeto = "".join(random_alfabeto)

def cifrado_cesar_modificado(texto, desplazamiento):
  
    texto_cifrado = ""
    for caracter in texto:
        if caracter in alfabeto:
            indice = alfabeto.index(caracter)
            nuevo_caracter = random_alfabeto[(indice + desplazamiento) % len(alfabeto)]
            texto_cifrado += nuevo_caracter
            desplazamiento -=1
        else:
            texto_cifrado += caracter
    return texto_cifrado
    
def descifrado_cesar_modificado(texto_cifrado, desplazamiento_inicial):
    texto_descifrado = ""
    desplazamiento = desplazamiento_inicial
    for caracter in texto_cifrado:
        if caracter in random_alfabeto:
            indice = random_alfabeto.index(caracter)
            nuevo_caracter = alfabeto[(indice - desplazamiento) % len(alfabeto)]
            texto_descifrado += nuevo_caracter
            desplazamiento -= 1
        else:
            texto_descifrado += caracter
    return texto_descifrado

secreto = "Hola, este es un mensaje secreto."

desplazamiento = 3

texto_cifrado = cifrado_cesar_modificado(secreto, desplazamiento)

texto_descifrado = descifrado_cesar_modificado(texto_cifrado, desplazamiento)

print("\nTexto cifrado:", texto_cifrado)
print("\nTexto descrifrado:", texto_descifrado)