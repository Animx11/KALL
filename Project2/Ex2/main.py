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

def power_bin_wm(b, k):
    sum = 1
    k_to_binary_string = dec_to_bin(k)
    for i in range(0, len(k_to_binary_string)):
        if int(k_to_binary_string[i]) == 1:
            sum = (sum * b * int(k_to_binary_string[i]))
        b = (b * b)
    return sum


def pierwiastek(b, p):

    k = p - 3
    k = k // 4
    z = p - 1 - k
    return int(power_bin(b, p, z))


def czy_reszta_kwadratowa(b, p):
    c = p-1
    c = c//2
    num = power_bin(b, p, c)
    if num == 1:
        return True
    else:
        return False


def generate_points(A, B, p):
    x = False
    while not x:
        generated_x = random.randrange(0, p)
        test = (power_bin_wm(generated_x, 3) + (A * generated_x) + B)
        x = czy_reszta_kwadratowa(test, p)

    generated_y = pierwiastek(generated_x, p)

    print("X = " + str(generated_x))
    print("Y = " + str(generated_y))



A = int(input("Podaj liczbę A: "))
B = int(input("Podaj liczbę B: "))
p = int(input("Podaj liczbę pierwszą: "))

generate_points(A, B, p)
