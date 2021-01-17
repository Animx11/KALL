
def rozszerzony_algorytm_euklidesa(b, n):

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
            print(mat[0])
            print(mat[1])

        elif mat[0][0] < mat[1][0]:

            if mat[1][0] % mat[0][0] == 0:
                con = True
                break

            a = mat[1][0] // mat[0][0]
            mat[1][1] = mat[1][1] - (a * mat[0][1])
            mat[1][2] = mat[1][2] - (a * mat[0][2])
            mat[1][0] = mat[1][0] % mat[0][0]
            print(mat[0])
            print(mat[1])

    if mat[0][0] != 0:
        return mat[1][2]
    else:
        return mat[0][2]


b = int(input("Input value b: "))
n = int(input("Input value n: "))
print(rozszerzony_algorytm_euklidesa(b, n))