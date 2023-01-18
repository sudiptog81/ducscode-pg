def encrypt(s, key):
    s = s.upper()
    return ''.join(key[c] for c in s)

def decipher(s, key):
    s = s.upper()
    return encrypt(s, {v: k for k, v in key.items()})

if __name__ == '__main__':
    key = { 'A': 'Q',
            'B': 'W',
            'C': 'E', 
            'D': 'R',
            'E': 'T',
            'F': 'Y',
            'G': 'U',
            'H': 'I',
            'I': 'O',
            'J': 'P',
            'K': 'A',
            'L': 'S',
            'M': 'D',
            'N': 'F',
            'O': 'G',
            'P': 'H',
            'Q': 'J',
            'R': 'K',
            'S': 'L',
            'T': 'Z',
            'U': 'X',
            'V': 'C',
            'W': 'V',
            'X': 'B',
            'Y': 'N',
            'Z': 'M' }
    s = input("Enter Plaintext: ")
    print("Plain Text:", s)
    print("Cipher Text:", encrypt(s, key))
    print("Deciphered Text:", decipher(encrypt(s, key), key))
