
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


def extended_euclidean_algorithm(a, b):
    mod = b
    s = 1
    t = 0
    u = 0
    v = 1
    while 0 < b:
        q = (a//b)

        a, b, s, t, u, v = b, (a%b), u, v, (s-u*q), (t-v*q)


    if s < 0:
        s = s + mod
    return [a, s, t]



def calculate_sum_of_elliptic_curve_points(p, a, b, point1, point2):
    if point2[0] == "infty" or point2[1] == "infty":
        return point1
    point2[0] = int(point2[0])
    point2[1] = int(point2[1])

    if point1[0] == point2[0] and point1[1] == (-point2[1] + p):
        return ["infty", "infty"]

    elif point1[0] == point2[0] and point1[1] == point2[1] == 0:
        return ["infty", "infty"]

    elif point1[0] == point2[0] and point1[1] == point2[1]:
        lam = ((3 * power_bin(point1[0], p, 2) + a) * extended_euclidean_algorithm((2 * point1[1] % p), p)[1]) % p
        x3 = (power_bin(lam, p, 2) - point1[0] - point2[0]) % p
        y3 = (lam * (point1[0] - x3) - point1[1]) % p
        return [x3, y3]

    elif point1[0] != point2[0]:
        lam = ((point2[1] - point1[1]) * extended_euclidean_algorithm(((point2[0]-point1[0]) % p), p)[1]) % p
        x = (power_bin(lam, p, 2) - point1[0] - point2[0]) % p
        y = (lam * (point1[0] - x) - point1[1]) % p
        return [x, y]



p = int(input("Podaj wartość p: "))
a = int(input("Podaj wartość A: "))
b = int(input("Podaj wartość B: "))
x1 = int(input("Podaj wartość x1: "))
y1 = int(input("Podaj wartość y1: "))
x2 = input("Podaj wartość x2: ")
y2 = input("Podaj wartość y2: ")

point1 = [x1, y1]
point2 = [x2, y2]

print(calculate_sum_of_elliptic_curve_points(p, a, b, point1, point2))

