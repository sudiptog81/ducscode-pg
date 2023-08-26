def make_matrix(s, n):
  m = []
  for i in range(n):
    m.append([])
  i = 0
  while len(s) % n != 0:
    s += 'Z'
  for c in s:
    m[i].append(c)
    i = (i + 1) % n
  
  return m

def encipher_transposition(s, k):
  c = ''
  s = s.upper()
  m = make_matrix(s, len(k))
  for r in m:
    print(r)
  for i in k:
    c += ''.join(m[i - 1])
  return c

def decipher_transposition(c, k):
  m = [list(c[i:i+len(c)//len(k)]) for i in range(0, len(c), len(c)//len(k))]
  _m = {}
  for i in range(len(k)):
    _m[k[i]] = m[i]
  s = ''
  for i in range(len(c)//len(k)):
    for j in range(len(k)):
      s += _m[j + 1][i]
  return s

s = input("Enter Plaintext: ")
k = [int(i) for i in input("Enter Key: ").split()]
print("Plain Text:", s)
print("Cipher Text:", encipher_transposition(s, k))
print("Deciphered Text:", decipher_transposition(encipher_transposition(s, k), k))
