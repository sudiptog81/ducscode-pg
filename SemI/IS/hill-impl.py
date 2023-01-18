import numpy as np

def invert(key):
  det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
  det = det % 26
  for i in range(26):
      if (det * i) % 26 == 1:
          det = i
          break
  return [[det * key[1][1], -det * key[0][1]], [-det * key[1][0], det * key[0][0]]]

def str2mat(string):
    integers = [ord(c) - ord('A') for c in string]
    length = len(integers)
    arr = np.zeros((2, length // 2), dtype=np.int32)
    i = 0
    for column in range(length // 2):
        for row in range(2):
            arr[row][column] = integers[i]
            i += 1
    return arr

def encipher_hill(s, key):
  c = ''
  s = s.upper()
  a = [(s[i:i+4]) for i in range(0, len(s), 4)]
  for b in a: 
    while not len(b) % 2 == 0:
      b += 'Z'
    p = str2mat(b)
    l = len(b) // 2
    for i in range(l):
      c += chr((key[0][0] * p[0][i] + key[0][1] * p[1][i]) % 26 + ord('A'))
      c += chr((key[1][0] * p[0][i] + key[1][1] * p[1][i]) % 26 + ord('A'))
  return c

def decipher_hill(s, key):
  c = ''
  s = s.upper()
  key = invert(key)
  a = [(s[i:i+4]) for i in range(0, len(s), 4)]
  for b in a: 
    while not len(b) % 2 == 0:
      b += 'Z'
    p = str2mat(b)
    l = len(b) // 2
    for i in range(l):
      c += chr((key[0][0] * p[0][i] + key[0][1] * p[1][i]) % 26 + ord('A'))
      c += chr((key[1][0] * p[0][i] + key[1][1] * p[1][i]) % 26 + ord('A'))
  return c

s = input('Enter Plaintext: ')
key = [[6, 15], [13, 4]]
print("Key:", key)
print("Plain Text:", s)
print("Cipher Text:", encipher_hill(s, key))
print("Deciphered Text:", decipher_hill(encipher_hill(s, key), key))
