def encipher_railfence(text, tracks):
    rail = [['\n' for i in range(len(text))] for j in range(tracks)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):
        if (row == 0) or (row == tracks - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(tracks):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ("" . join(result))

def decipher_railfence(cipher, tracks):
    rail = [['\n' for i in range(len(cipher))] for j in range(tracks)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == tracks - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(tracks):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == tracks - 1:
            dir_down = False
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return ("".join(result))


s = input("Enter Plaintext: ")
tracks = int(input("Enter No. of Tracks: "))
print("Plain Text:", s)
print("Cipher Text:", encipher_railfence(s, tracks))
print("Deciphered Text:", decipher_railfence(encipher_railfence(s, tracks), tracks))
