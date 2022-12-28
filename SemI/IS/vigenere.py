from sympy.crypto.crypto import AZ
from sympy.crypto.crypto import encipher_vigenere, decipher_vigenere

s = AZ(input("Enter Plaintext: "))
key = input("Enter Key: ")
print("Plain Text:", s)
print("Cipher Text:", encipher_vigenere(s, key))
print("Deciphered Text:", decipher_vigenere(encipher_vigenere(s, key), key))
