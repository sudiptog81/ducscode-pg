def encipher_vernam(plaintext, key):
    return ''.join(['{}'.format(int(i) ^ int(j)) for i, j in zip(plaintext, key)])

def decipher_vernam(ciphertext, key):
    return ''.join(['{}'.format(int(i) ^ int(j)) for i, j in zip(ciphertext, key)])

s = input('Enter Plaintext: ')
key = input('Enter Key: ')
print("Plain Text:", s)
print("Cipher Text:", encipher_vernam(s, key))
print("Deciphered Text:", decipher_vernam(encipher_vernam(s, key), key))
