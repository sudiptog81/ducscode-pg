def encrypt_shift(s, key):
    s = ''.join(s.upper().split())
    return ''.join([chr(((ord(c) - 65 + key) % 26) + 65) for c in s])

def decrypt_shift(s, key):
    return encrypt_shift(s, -key)

if __name__ == "__main__":
    s = input("Enter Plaintext: ")
    key = int(input("Enter Key: "))
    print("Plain Text:", s)
    print("Cipher Text:", encrypt_shift(s, key))
    print("Deciphered Text:", decrypt_shift(encrypt_shift(s, key), key))
