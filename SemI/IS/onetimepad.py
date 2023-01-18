from sympy.crypto.crypto import AZ
from sympy.crypto.crypto import encipher_vigenere, decipher_vigenere

import string
import random

s = AZ(input("Enter Plaintext: "))
key = ''.join(random.choices(string.ascii_uppercase, k=len(s)))
print("Generated Key : " + key)
print("Plain Text:", s)
assert len(key) == len(s)
print("Cipher Text:", encipher_vigenere(s, key))
print("Deciphered Text:", decipher_vigenere(encipher_vigenere(s, key), key))
