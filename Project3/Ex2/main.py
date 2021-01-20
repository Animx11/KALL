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
        lam = ((3 * power_bin(point1[0], p, 2) + a) * extended_euclidean_algorithm((2 * point1[1] % p), p)) % p
        x3 = (power_bin(lam, p, 2) - point1[0] - point2[0]) % p
        y3 = (lam * (point1[0] - x3) - point1[1]) % p
        return [x3, y3]

    elif point1[0] != point2[0]:
        lam = ((point2[1] - point1[1]) * extended_euclidean_algorithm(((point2[0]-point1[0]) % p), p)) % p
        x = (power_bin(lam, p, 2) - point1[0] - point2[0]) % p
        y = (lam * (point1[0] - x) - point1[1]) % p
        return [x, y]


# def calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return point
#     elif n % 2 == 0:
#         return calculate_sum_of_elliptic_curve_points(p, A, B, calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n//2), calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n//2))
#     elif n % 2 == 1:
#         mul = calculate_sum_of_elliptic_curve_points(p, A, B, calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n//2), calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n//2))
#         return calculate_sum_of_elliptic_curve_points(p, A, B, point, mul)


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
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
n = int(input("Enter the value of n: "))


point = [x, y]

exp_xn = 10
exp_yn = 1
print(calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n))

