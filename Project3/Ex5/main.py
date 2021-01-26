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


def calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n):
    if n == 0:
        return 0
    elif n == 1:
        return point
    elif n % 2 == 1:
        return calculate_sum_of_elliptic_curve_points(p, A, B, point, calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n - 1))
    elif n % 2 == 0:
        return calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, calculate_sum_of_elliptic_curve_points(p, A, B, point, point), n/2)


p = int(input("Enter the value of p: "))
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
a1 = int(input("Enter the value of a1: "))
a2 = int(input("Enter the value of a2: "))
n = int(input("Enter the value of n: "))
C1x = int(input("Enter the value of C1x: "))
C1y = int(input("Enter the value of C1y: "))
C2x = int(input("Enter the value of C2x: "))
C2y = int(input("Enter the value of C2y: "))


C1 = [C1x, C1y]
C2 = [C2x, C2y]

nC1 = calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, C1, n)
nC1[1] = -nC1[1] + p
decrypted = calculate_sum_of_elliptic_curve_points(p, A, B, C2, nC1)
print(decrypted)