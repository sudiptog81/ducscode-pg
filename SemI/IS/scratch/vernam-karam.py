def encipher_vernam(plaintext, key):
  # Ensure the key is the same length as the plain_text
  key = key[:len(plaintext)]
  
  # Convert plain_text and key to binary strings
  plain_text_binary = [int(i) for i in plaintext]
  key_binary = [int(i) for i in key]
  #
  # XOR the binary strings
  cipher_text_binary = [a ^ b for a, b in zip(plain_text_binary, key_binary)]

  # Convert cipher_text_binary to a string of characters
  cipher_text = ''.join([str(i) for i in cipher_text_binary])
  
  return cipher_text


def decipher_vernam(ciphertext, key):
      # Ensure the key is the same length as the cipher_text
    key = key[:len(ciphertext)]
    
    # Convert cipher_text and key to binary strings
    cipher_text_binary = ''.join(format(ord(c), '08b') for c in ciphertext)
    key_binary = ''.join(format(ord(c), '08b') for c in key)
    
    # XOR the binary strings
    plain_text_binary = ''.join(str(int(a) ^ int(b)) for a, b in zip(cipher_text_binary, key_binary))
    
    # Convert plain_text_binary to a string of characters
    plain_text = ''
    for i in range(0, len(plain_text_binary), 8):
        plain_text += chr(int(plain_text_binary[i:i+8], 2))
    
    return plain_text


s = input('Enter Plaintext: ')
key = input('Enter Key: ')
print("Plain Text:", s)
print("Cipher Text:", encipher_vernam(s, key))
print("Deciphered Text:", decipher_vernam(encipher_vernam(s, key), key))
