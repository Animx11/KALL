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


def is_first_fermat(n, k):
    i = 0
    while i < k:
        a = random.randint(1, n - 1)
        if power_bin(a, n, (n-1)) == 1:
            i = i + 1
        else:
            return False
    return True


n = int(input("Input value n: "))
is_first = is_first_fermat(n, 2048)

if is_first:
    print("n jest prawdopodobnie liczbą pierwszą")
else:
    print("n jest liczbą złożoną")