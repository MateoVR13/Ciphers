alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def CrearMatriz(alfa):
    size = len(alfabeto)
    Matriz = list()
    for clave in  range(size):
        lineaMatriz = list()
        for texto in  range(size):
            lineaMatriz.append(alfabeto[(texto+clave) % size])
        Matriz.append(lineaMatriz)
    return Matriz 
  
def CifrarVigenere(texto:str, clave:str):
    MatrizVigenere = CrearMatriz(alfabeto)
    cifrado = ""
    longClave = len(clave)
    IndiceClave = 0
    for letra in texto:
        if letra in alfabeto:
            LineaOrigen = MatrizVigenere[alfabeto.find(letra)]
            cifrado = cifrado + LineaOrigen[alfabeto.find(clave[IndiceClave % longClave])]
            IndiceClave += 1
        else:
            cifrado = cifrado + letra
    print(cifrado)
    return cifrado
        
CifrarVigenere("ESTO ES UN EJEMPLO DE CIFRADO","CAMION")