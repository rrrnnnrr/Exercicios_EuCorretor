def firstUniqChar(s):
    contador_char = {}

    for i, char in enumerate(s):
        if char in contador_char:
            contador_char[char][0] += 1
        else:
            contador_char[char] = [1, i]

    for char, (count, index) in contador_char.items():
        if count == 1:
            return index

    return -1
