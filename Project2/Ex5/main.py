
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


def extended_euclidean_algorithm(b, n):

    if b < n:
        b, n = n, b
    mat = ([int(b), int(1), int(0)], [int(n), int(0), int(1)])

    con = False
    while not con:
        if mat[0][0] > mat[1][0]:

            if mat[0][0] % mat[1][0] == 0:
                con = True
                break

            a = mat[0][0] // mat[1][0]
            mat[0][1] = int(mat[0][1]) - (a * mat[1][1])
            mat[0][2] = mat[0][2] - (a * mat[1][2])
            mat[0][0] = mat[0][0] % mat[1][0]

        elif mat[0][0] < mat[1][0]:

            if mat[1][0] % mat[0][0] == 0:
                con = True
                break

            a = mat[1][0] // mat[0][0]
            mat[1][1] = mat[1][1] - (a * mat[0][1])
            mat[1][2] = mat[1][2] - (a * mat[0][2])
            mat[1][0] = mat[1][0] % mat[0][0]

    if mat[0][0] != 0:
        return mat[1][2]
    else:
        return mat[0][2]


def calculate_sum_of_elliptic_curve_points(p, a, b, x1, y1, x2, y2):
    if x2 == "infty" or y2 == "infty":
        print(x1)
        print(y1)
        return 0
    x2 = int(x2)
    y2 = int(y2)

    if x1 == x2 and y1 == (-y2 + p):
        print("infty")
        print("infty")

    elif x1 == x2 and y1 == y2 == 0:
        print("infty")
        print("infty")

    elif x1 == x2 and y1 == y2:
        lam = ((3 * power_bin(x1, p, 2) + a) * extended_euclidean_algorithm((2 * y1 % p), p)) % p
        x3 = (power_bin(lam, p, 2) - x1 - x2) % p
        y3 = (lam * (x1 - x3) - y1) % p
        print(x3)
        print(y3)

    elif x1 != x2:
        lam = ((y2 - y1) * extended_euclidean_algorithm(((x2-x1) % p), p)) % p
        x3 = (power_bin(lam, p, 2) - x1 - x2) % p
        y3 = (lam * (x1 - x3) - y1) % p
        print(x3)
        print(y3)


p = int(input("Podaj wartość p: "))
a = int(input("Podaj wartość A: "))
b = int(input("Podaj wartość B: "))
x1 = int(input("Podaj wartość x1: "))
y1 = int(input("Podaj wartość y1: "))
x2 = input("Podaj wartość x2: ")
y2 = input("Podaj wartość y2: ")

calculate_sum_of_elliptic_curve_points(p, a, b, x1, y1, x2, y2)

