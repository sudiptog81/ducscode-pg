from sympy.crypto.crypto import AZ
from sympy.crypto.crypto import encipher_railfence, decipher_railfence

s = AZ(input("Enter Plaintext: "))
tracks = int(input("Enter No. of Tracks: "))
print("Plain Text:", s)
print("Cipher Text:", encipher_railfence(s, tracks))
print("Deciphered Text:", decipher_railfence(encipher_railfence(s, tracks), tracks))
