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
    return int(sum)

def power_bin_notmod(b, k):
    sum = 1
    k_to_binary_string = dec_to_bin(k)
    for i in range(0, len(k_to_binary_string)):
        if int(k_to_binary_string[i]) == 1:
            sum = (sum * b * int(k_to_binary_string[i]))
        b = (b * b)
    return int(sum)


def is_first_fermat(n, k):
    i = 0
    while i < k:
        a = random.randint(1, n - 1)
        if power_bin(a, n, (n-1)) == 1:
            i = i + 1
        else:
            return False
    return True


def generate_elliptic_curve(p):
    generated_A = random.randrange(0, p)
    generated_B = random.randrange(0, p)

    delta = (4 * power_bin(generated_A, p, 3) + 27 * power_bin(generated_B, p, 2)) % p

    if delta == 0:
        generate_elliptic_curve(p)

    else:
        return [generated_A, generated_B]


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
        test = (power_bin_notmod(generated_x, 3) + (A * generated_x) + B)
        x = czy_reszta_kwadratowa(test, p)

    generated_y = pierwiastek(test, p)

    return [generated_x, generated_y]


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


def calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n):
    if n == 0:
        return 0
    elif n == 1:
        return point
    elif n % 2 == 1:
        return calculate_sum_of_elliptic_curve_points(p, A, B, point, calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, point, n - 1))
    elif n % 2 == 0:
        return calculate_multiplication_of_elliptic_curve_point_by_n(p, A, B, calculate_sum_of_elliptic_curve_points(p, A, B, point, point), n/2)


def generate_elgamal_keypair_by_elliptic_curve(k):
    p = 0
    is_prime = False
    while not is_prime:
        p = random.randrange(power_bin_notmod(2, k-1), power_bin_notmod(2, k))
        if p % 4 == 3:
            if is_first_fermat(p, k):
                is_prime = True

    ab_value = generate_elliptic_curve(p)
    point_q = generate_points(ab_value[0], ab_value[1], p)
    n = random.randint(1, p)

    point_p = calculate_multiplication_of_elliptic_curve_point_by_n(p, ab_value[0], ab_value[1], point_q, n)

    public_key = [point_q, point_p, p, ab_value[0], ab_value[1]]
    private_key = [point_q, n, p, ab_value[0], ab_value[1]]

    return [public_key, private_key]


k = int(input("How many bits for prime number: "))
key_pair = generate_elgamal_keypair_by_elliptic_curve(k)


print("\nKlucz publiczny:\n")
print("p = " + str(key_pair[0][2]))
print("A = " + str(key_pair[0][3]))
print("B = " + str(key_pair[0][4]))
print("a1 = " + str(key_pair[0][0][0]))
print("a2 = " + str(key_pair[0][0][1]))
print("a1 = " + str(key_pair[0][1][0]))
print("a2 = " + str(key_pair[0][1][1]))

print("\nKlucz prywatny:\n")
print("p = " + str(key_pair[1][2]))
print("A = " + str(key_pair[1][3]))
print("B = " + str(key_pair[1][4]))
print("a1 = " + str(key_pair[1][0][0]))
print("a2 = " + str(key_pair[1][0][1]))
print("n = " + str(key_pair[1][1]))

