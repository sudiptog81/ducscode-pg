def encipher_vigenere(s, key):
  s = s.upper()
  key = key.upper()
  key = key * (len(s) // len(key) + 1)
  key = key[:len(s)]
  return ''.join([chr((ord(s[i]) - 65 + ord(key[i]) - 65) % 26 + 65) for i in range(len(s))])

def decipher_vigenere(s, key):
  s = s.upper()
  key = key.upper()
  key = key * (len(s) // len(key) + 1)
  key = key[:len(s)]
  return ''.join([chr((ord(s[i]) - 65 - (ord(key[i]) - 65)) % 26 + 65) for i in range(len(s))])

if __name__ == '__main__':
  s = input("Enter Plaintext: ")
  key = input("Enter Key: ")
  print("Plain Text:", s)
  print("Cipher Text:", encipher_vigenere(s, key))
  print("Deciphered Text:", decipher_vigenere(encipher_vigenere(s, key), key))
