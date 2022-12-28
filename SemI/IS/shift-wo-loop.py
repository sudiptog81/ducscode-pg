alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encipher_shift(p, key):
    p = p.upper()
    if len(p) == 0:
        return ""
    elif key == 0:
        return key
    elif p[0] == ' ':
        return ' ' + encipher_shift(p[1:], key)
    else:
        index = (alphabet.index(p[0]) + key) % len(alphabet)
        return alphabet[index] + encipher_shift(p[1:], key)

def decipher_shift(c, key):
    c = c.upper()
    if len(c) == 0:
        return ""
    elif key == 0:
        return key
    elif c[0] == ' ':
        return ' ' + decipher_shift(c[1:], key)
    else:
        index = (alphabet.index(c[0]) - key) % len(alphabet)
        return alphabet[index] + decipher_shift(c[1:], key)

if __name__ == "__main__":
    p = input("Enter Plaintext: ")
    key = int(input("Enter Key: "))
    print("Plain Text:", p)
    c = encipher_shift(p, key)
    print("Cipher Text:", c)
    print("Deciphered Text:", decipher_shift(c, key))
