from sympy.crypto.crypto import AZ
from sympy.crypto.crypto import encipher_hill, decipher_hill
from sympy import Matrix

s = AZ(input("Enter Plaintext: "))
key = Matrix([[6, 15], [13, 4]])
print("Key:", key)
print("Plain Text:", s)
print("Cipher Text:", encipher_hill(s, key))
print("Deciphered Text:", decipher_hill(encipher_hill(s, key), key))
