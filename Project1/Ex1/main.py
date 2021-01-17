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


n = int(input("Input value n: "))
k = int(input("Input value k: "))


'# Dałem tutaj do k, -1, gdyż otrzymywałem liczby o 1 bit za dużo.'
'# Przy pierwszym przykładzie dostawałem liczby pokroju 1342, gdzie maksymalnie powinny być 1023 przy braniu 10 bitów.'
random_number = random.randrange(power_bin(2, n, k-1), power_bin(2, n, k))

print(random_number)

