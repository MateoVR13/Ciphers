alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789!@#$%^&*()'

def CrearMatriz(alfa):
    size = len(alfa)
    Matriz = list()
    for clave in range(size):
        lineaMatriz = list()
        for texto in range(size):
            lineaMatriz.append(alfa[(texto + clave) % size])
        Matriz.append(lineaMatriz)
    return Matriz

def ExpandirClave(clave, longitud):
    return (clave * (longitud // len(clave))) + clave[:longitud % len(clave)]

def CifrarVigenere(texto, clave):
    MatrizVigenere = CrearMatriz(alfabeto)
    cifrado = ""
    longClave = len(clave)
    IndiceClave = 0
    clave_expandida = ExpandirClave(clave, len(texto))
    for letra in texto:
        if letra in alfabeto:
            LineaOrigen = MatrizVigenere[alfabeto.find(letra)]
            cifrado += LineaOrigen[alfabeto.find(clave_expandida[IndiceClave])]
            IndiceClave += 1
        else:
            cifrado += letra
    print(cifrado)
    return cifrado

def DescifrarVigenere(texto, clave):
    MatrizVigenere = CrearMatriz(alfabeto)
    descifrado = ""
    longClave = len(clave)
    IndiceClave = 0
    clave_expandida = ExpandirClave(clave, len(texto))
    for letra in texto:
        if letra in alfabeto:
            LineaOrigen = alfabeto.find(clave_expandida[IndiceClave])
            columna = MatrizVigenere[LineaOrigen]
            descifrado += alfabeto[columna.index(letra)]
            IndiceClave += 1
        else:
            descifrado += letra
    print(descifrado)
    return descifrado


secreto = "ESTO ES UN EJEMPLO DE CIFRADO"
clave = "CAMION"

texto_cifrado = CifrarVigenere(secreto, clave)

texto_descifrado = DescifrarVigenere(texto_cifrado, clave)