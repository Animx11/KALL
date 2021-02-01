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


def mul(a, b):

    b_prim = bin(int(b, 2) >> 1)[2:].zfill(8)
    if b_prim == '00000000':
        return a
    if b[7] == '0':
        return mul(xtime(a), b_prim)
    else:
        return sum(mul(xtime(a), b_prim), a)


a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")


print(bin_to_hex(mul(hex_to_bin(a), hex_to_bin(b))))
