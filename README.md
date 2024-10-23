# Python Classical Ciphers Implementation

This repository contains implementations of two classic cryptographic algorithms: a modified Caesar cipher and a modified Vigenère cipher. Both implementations include additional features and modifications to enhance their security compared to their traditional versions.

## Features

- Modified Caesar Cipher with:
  - Random alphabet shuffling
  - Multi-shift based on key characters
  - Extended character set including special characters
- Modified Vigenère Cipher with:
  - Extended alphabet including numbers and special characters
  - Key expansion functionality
  - Support for maintaining non-alphabet characters

## Cipher Implementations

### Modified Caesar Cipher

This implementation extends the traditional Caesar cipher by using a randomized substitution alphabet, generating multiple shifts based on the key, and supporting an extended character set.

Example usage:
```python
secreto = "Hola, este es un mensaje secreto!"
clave = "PYTHON"
texto_cifrado = cifrado_cesar_modificado(secreto, clave)
print("\nTexto cifrado:", texto_cifrado)
texto_descifrado = descifrado_cesar_modificado(texto_cifrado, clave)
print("\nTexto descifrado:", texto_descifrado)
```

### Modified Vigenère Cipher

This version enhances the classic Vigenère cipher with an extended alphabet and key expansion for messages longer than the key.

Example usage:
```python
secreto = "ESTO ES UN EJEMPLO DE CIFRADO"
clave = "CAMION"
texto_cifrado = CifrarVigenere(secreto, clave)
texto_descifrado = DescifrarVigenere(texto_cifrado, clave)
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MateoVR13/Ciphers.git
```

2. No additional dependencies are required - the implementation uses only Python standard library.

## Requirements

- Python 3.x

## Usage Instructions

1. Import the cipher modules in your Python script
2. For Caesar Cipher:
```python
# Encryption
texto_cifrado = cifrado_cesar_modificado("Tu mensaje", "TU_CLAVE")
# Decryption
texto_descifrado = descifrado_cesar_modificado(texto_cifrado, "TU_CLAVE")
```

3. For Vigenère Cipher:
```python
# Encryption
texto_cifrado = CifrarVigenere("Tu mensaje", "TU_CLAVE")
# Decryption
texto_descifrado = DescifrarVigenere(texto_cifrado, "TU_CLAVE")
```

## Function Descriptions

### Caesar Cipher Functions:
- `cifrado_cesar_modificado(texto, clave)`: Encrypts the input text using the modified Caesar algorithm
- `descifrado_cesar_modificado(texto_cifrado, clave)`: Decrypts the encrypted text using the same key
- `generar_desplazamientos(clave, longitud)`: Generates the shift values based on the key

### Vigenère Cipher Functions:
- `CifrarVigenere(texto, clave)`: Encrypts the input text using the modified Vigenère algorithm
- `DescifrarVigenere(texto_cifrado, clave)`: Decrypts the encrypted text
- `CrearMatriz(alfa)`: Creates the Vigenère matrix using the extended alphabet
- `ExpandirClave(clave, longitud)`: Expands the key to match the message length

## Security Considerations

While these implementations add additional security features to the classical ciphers, they are still primarily for educational purposes and should not be used for securing sensitive data in production environments. For real-world applications, please use standard cryptographic libraries and modern encryption algorithms.

## Contributing

Feel free to submit issues and enhancement requests! 

## License

This project is licensed under the MIT License - see the LICENSE file for details.
