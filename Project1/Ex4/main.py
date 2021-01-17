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


def czy_reszta_kwadratowa(b, p):
    c = p-1
    c = c//2
    num = power_bin(b, p, c)
    if num == 1:
        print("b jest resztą kwadratową")
    else:
        print("b nie jest resztą kwadratową")


b = int(input("Input value b: "))
p = int(input("Input value p: "))

czy_reszta_kwadratowa(b, p)

