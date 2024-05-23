import random

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def cifrado(texto, clave):
    
    resultado = ""
    for letra in texto:
        if alfabeto.find(letra) >= 0:
            resultado = resultado + alfabeto[((alfabeto.find(letra)+clave) % len(alfabeto))]
        else:
            resultado = resultado + letra
            
    return resultado
cif = cifrado("Hola este es un mensaje secreto", random.randint(1, 7))
print(cif)