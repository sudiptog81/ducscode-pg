import numpy as np

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_playfair_matrix(key):
  mapping= {}
  key = key.upper()
  mat = np.zeros((5, 5), dtype=str)
  
  for c in alphabet:
    if c not in key:
      if c == 'I' and 'J' in key:
        continue
      elif c == 'J' and 'I' in key:
        continue
      key += c

  i = j = 0
  for i, c in enumerate(key):
    if c not in mapping.keys():
      mat[j][i % 5] = c
      mapping[c] = (j, i % 5)
      i += 1
    if i % 5 == 0:
      j += 1
  
  return mapping, mat
  
def encipher_playfair(text, key):
  n = ''

  text = text.upper()
  mapping, mat = make_playfair_matrix(key)

  for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
      text = text[:i + 1] + 'X' + text[i + 1:]

  while len(text) % 2 != 0:
    text += 'Z'
  
  bigrams = [text[i:i + 2] for i in range(0, len(text), 2)]
  print('Bigrams:', bigrams)
  for b in bigrams:
    if (mapping[b[0]][0] == mapping[b[1]][0]):
      # same row
      n += (mat[mapping[b[0]][0]][(mapping[b[0]][1] + 1) % 5])
      n += (mat[mapping[b[1]][0]][(mapping[b[1]][1] + 1) % 5])
    elif (mapping[b[0]][1] == mapping[b[1]][1]):
      # same col
      n += (mat[(mapping[b[0]][0] + 1) % 5][mapping[b[0]][1]])
      n += (mat[(mapping[b[1]][0] + 1) % 5][mapping[b[1]][1]])
    else:
      # diff row, col
      n += (mat[mapping[b[0]][0]][mapping[b[1]][1]])
      n += (mat[mapping[b[1]][0]][mapping[b[0]][1]])
  return n

def decipher_playfair(text, key):
  n = ''

  text = text.upper()

  while len(text) % 2 != 0:
    text += 'Z'
  
  mapping, mat = make_playfair_matrix(key)
  
  bigrams = [text[i:i + 2] for i in range(0, len(text), 2)]
  for b in bigrams:
    if (mapping[b[0]][0] == mapping[b[1]][0]):
      # same row
      n += (mat[mapping[b[0]][0]][(mapping[b[0]][1] - 1) % 5])
      n += (mat[mapping[b[1]][0]][(mapping[b[1]][1] - 1) % 5])
    elif (mapping[b[0]][1] == mapping[b[1]][1]):
      # same col
      n += (mat[(mapping[b[0]][0] - 1) % 5][mapping[b[0]][1]])
      n += (mat[(mapping[b[1]][0] - 1) % 5][mapping[b[1]][1]])
    else:
      # diff row, col
      n += (mat[mapping[b[0]][0]][mapping[b[1]][1]])
      n += (mat[mapping[b[1]][0]][mapping[b[0]][1]])
  return n

s = input('Enter Plaintext: ')
key = input('Enter Key: ')
print('Key Matrix:')
print(make_playfair_matrix(key)[1])
print("Plain Text:", s)
print("Cipher Text:", encipher_playfair(s, key))
print("Deciphered Text:", decipher_playfair(encipher_playfair(s, key), key))
