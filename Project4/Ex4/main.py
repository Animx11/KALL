def hex_to_bin(hex):
    return bin(int(hex, 16))[2:].zfill(8)


def bin_to_hex(bin):
    if bin == 'undefined':
        return 'undefined'
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


def dec_to_bin(k):
    binary_string = bin(k).replace("0b", '')[::-1]
    return str(binary_string)




def power_bin(b, k):
    if b == '00000000':
        return str('undefined')
    s = '00000001'
    k_to_binary_string = dec_to_bin(k)
    for i in range(0, len(k_to_binary_string)):
        if k_to_binary_string[i] == '1':
            s = mul(s, b)
        b = mul(b, b)
    return s


a = input("Podaj liczbę a: ")
a = hex_to_bin(a)
print(bin_to_hex(power_bin(a, 254)))
