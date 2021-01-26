
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


b = int(input("Input value b: "))
n = int(input("Input value n: "))
print(extended_euclidean_algorithm(b, n))