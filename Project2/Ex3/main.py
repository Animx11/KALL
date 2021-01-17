
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


def check_if_point_exist_on_ellipse_curve(p, a, b, x, y):
    left = (power_bin(y, p, 2)) % p
    right = (power_bin(x, p, 3) + (a * x) + b) % p
    if left == right:
        return True
    else:
        return False


p = int(input("Podaj wartość p: "))
a = int(input("Podaj wartość A: "))
b = int(input("Podaj wartość B: "))
x = int(input("Podaj wartość x: "))
y = int(input("Podaj wartość y: "))

print(check_if_point_exist_on_ellipse_curve(p, a, b, x, y))


