

def dec_to_bin(k):
    binary_string = bin(k).replace("0b", '')[::-1]
    return str(binary_string)


def power_bin_notmod(b, k):
    sum = 1
    k_to_binary_string = dec_to_bin(k)
    for i in range(0, len(k_to_binary_string)):
        if int(k_to_binary_string[i]) == 1:
            sum = (sum * b * int(k_to_binary_string[i]))
        b = (b * b)
    return int(sum)


def power_bin(b, n, k):
    sum = 1
    k_to_binary_string = dec_to_bin(k)
    for i in range(0, len(k_to_binary_string)):
        if int(k_to_binary_string[i]) == 1:
            sum = (sum * b * int(k_to_binary_string[i])) % n
        b = (b * b) % n
    return sum


def encode_message_to_number(message):
    i = len(message)
    encoded_message = 0
    for letter in message:
        encoded_message = encoded_message + ord(letter) * power_bin_notmod(200, i-1)
        i = i-1
    return encoded_message


def square_root_on_field_fp(b, p):

    k = p - 3
    k = k // 4
    z = p - 1 - k
    return int(power_bin(b, p, z))


def is_quadratic_residue(b, p):
    c = p-1
    c = c//2
    num = power_bin(b, p, c)
    if num == 1:
        return True
    else:
        return False


def generate_points(A, B, encoded_message, p):
    x = False
    k = 20
    message_x = k * encoded_message
    while not x:
        test = (power_bin_notmod(message_x, 3) + (A * message_x) + B)
        x = is_quadratic_residue(test, p)
        if not x:
            message_x = message_x + 1

    message_y = square_root_on_field_fp(test, p)

    return [message_x, message_y]


m = input("Enter message: ")
p = int(input("Enter the value of p: "))
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))

encoded_message = encode_message_to_number(m)
point = generate_points(A, B, encoded_message, p)
print(point)

