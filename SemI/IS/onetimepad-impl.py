import string
import random

def encipher_vigenere(s, key):
  s = s.upper()
  key = key.upper()
  assert len(key) == len(s)
  return ''.join([chr((ord(s[i]) - 65 + ord(key[i]) - 65) % 26 + 65) for i in range(len(s))])

def decipher_vigenere(s, key):
  s = s.upper()
  key = key.upper()
  assert len(key) == len(s)

  return ''.join([chr((ord(s[i]) - 65 - (ord(key[i]) - 65)) % 26 + 65) for i in range(len(s))])

if __name__ == '__main__':
  s = input("Enter Plaintext: ")
  key = ''.join(random.choices(string.ascii_uppercase, k=len(s)))
  print("Generated Key : " + key)
  print("Plain Text:", s)
  print("Cipher Text:", encipher_vigenere(s, key))
  print("Deciphered Text:", decipher_vigenere(encipher_vigenere(s, key), key))
