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

This implementation extends the traditional Caesar cipher by:
- Using a randomized substitution alphabet
- Generating multiple shifts based on the key
- Supporting an extended character set (uppercase, lowercase, numbers, and special characters)

Example usage:
```python
secret = "Hello, this is a secret message!"
key = "PYTHON"
encrypted = cipher_caesar_modified(secret, key)
decrypted = decipher_caesar_modified(encrypted, key)
```

### Modified Vigenère Cipher

This version enhances the classic Vigenère cipher with:
- Extended alphabet (uppercase, lowercase, numbers, and special characters)
- Key expansion for messages longer than the key
- Preserving non-alphabet characters in the original text

Example usage:
```python
secret = "THIS IS AN ENCRYPTION EXAMPLE"
key = "TRUCK"
encrypted = cipher_vigenere(secret, key)
decrypted = decipher_vigenere(encrypted, key)
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-ciphers.git
```

2. No additional dependencies are required - the implementation uses only Python standard library.

## Requirements

- Python 3.x

## Usage Instructions

1. Import the desired cipher module:
```python
from caesar_cipher import cipher_caesar_modified, decipher_caesar_modified
# or
from vigenere_cipher import cipher_vigenere, decipher_vigenere
```

2. For Caesar Cipher:
```python
# Encryption
encrypted_text = cipher_caesar_modified("Your message", "YOUR_KEY")
# Decryption
decrypted_text = decipher_caesar_modified(encrypted_text, "YOUR_KEY")
```

3. For Vigenère Cipher:
```python
# Encryption
encrypted_text = cipher_vigenere("Your message", "YOUR_KEY")
# Decryption
decrypted_text = decipher_vigenere(encrypted_text, "YOUR_KEY")
```

## Security Considerations

While these implementations add additional security features to the classical ciphers, they are still primarily for educational purposes and should not be used for securing sensitive data in production environments. For real-world applications, please use standard cryptographic libraries and modern encryption algorithms.

## Contributing

Feel free to submit issues and enhancement requests! 

## License

This project is licensed under the MIT License - see the LICENSE file for details.
