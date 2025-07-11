#  Hill Cipher - Cryptography Project (Python)

This project demonstrates how to encrypt and decrypt text using the **Hill Cipher algorithm**, implemented in Python using matrix operations and ASCII mapping.

It supports all standard characters: uppercase, lowercase, numbers, symbols, and even space, not just alphabets. The encryption and decryption both use a 2x2 cipher key matrix and modular arithmetic.

---

##  How It Works

- Converts all characters in the message into numeric values based on a custom ASCII dictionary (0–95)
- Pads the message if its length is odd
- Encrypts the message using matrix multiplication with a cipher key (2x2)
- Applies mod with dictionary size to keep values within range
- Decrypts using modular inverse of the determinant and matrix inverse

---

##  How to Run

1. Make sure Python is installed
2. Run the script:

```bash
python hill_cipher.py
