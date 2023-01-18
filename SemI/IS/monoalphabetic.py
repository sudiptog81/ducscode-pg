from sympy.crypto.crypto import encipher_substitution, AZ

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mapping = "QWERTYUIOPASDFGHJKLZXCVBNM"

s = AZ(input("Enter Plaintext: "))
print("Plain Text:", s)
print("Cipher Text:", encipher_substitution(s, alphabet, mapping))
print(
  "Deciphered Text:", 
  encipher_substitution(
    encipher_substitution(s, alphabet, mapping), 
    mapping,
    alphabet
  )
)
  