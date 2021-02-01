def hex_to_bin(hex):
    return bin(int(hex, 16))[2:].zfill(8)


def bin_to_hex(bin):
    return hex(int(bin, 2))[2:].zfill(2)


def sum(a, b):
    c = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        c[i] = bin(int(a[i], 2) ^ int(b[i], 2))[2:]
    return ''.join(c)


a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")

a = hex_to_bin(a)
b = hex_to_bin(b)
s = sum(a, b)
s_hex = bin_to_hex(s)


print(s_hex)
