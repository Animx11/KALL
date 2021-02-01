def hex_to_bin(hex):
    return bin(int(hex, 16))[2:].zfill(8)


def bin_to_hex(bin):
    return hex(int(bin, 2))[2:].zfill(2)


def sum(a, b):
    c = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        c[i] = bin(int(a[i], 2) ^ int(b[i], 2))[2:]
    return ''.join(c)


def xtime(x):
    if x[0] == '0':
        s = bin(int(x, 2) << 1)[2:].zfill(8)
        return s
    else:
        s = bin(int(x, 2) << 1)[3:].zfill(8)
        s = sum(s, '00011011')
        return s


a = input("Podaj liczbę a: ")

s = xtime(hex_to_bin(a))
print(bin_to_hex(s))
