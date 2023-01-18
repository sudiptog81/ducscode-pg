def encipher_railfence(s, r):
    if r == 1:
        return s
    else:
        return ''.join([s[i::r] for i in range(r)])

def decipher_railfence(s, r):
    if r == 1:
        return s
    else:
        return ''.join([s[i::r] for i in range(r)])   

s = input("Enter Plaintext: ")
tracks = int(input("Enter No. of Tracks: "))
print("Plain Text:", s)
print("Cipher Text:", encipher_railfence(s, tracks))
print("Deciphered Text:", decipher_railfence(encipher_railfence(s, tracks), tracks))
