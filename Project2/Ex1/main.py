import random


def dec_to_bin(k):
    binary_string = bin(k).replace("0b", '')[::-1]
    return str(binary_string)


def power_bin(b, n, k):
    sum = 1
    k_to_binary_string = dec_to_bin(k)
    for i in range(0, len(k_to_binary_string)):
        if int(k_to_binary_string[i]) == 1:
            sum = (sum * b * int(k_to_binary_string[i])) % n
        b = (b * b) % n
    return sum


def generate_elliptic_curve(p):
    generated_A = random.randrange(0, p)
    generated_B = random.randrange(0, p)

    delta = (4 * power_bin(generated_A, p, 3) + 27 * power_bin(generated_B, p, 2)) % p

    if delta == 0:
        generate_elliptic_curve(p)

    else:
        print(generated_A)
        print(generated_B)


p = int(input("Podaj liczbę pierwszą: "))
generate_elliptic_curve(p)
