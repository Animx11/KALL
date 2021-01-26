p = int(input("Enter the value of p: "))
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
PM1 = int(input("Enter the value of PM1: "))
PM2 = int(input("Enter the value of PM2: "))


k = 20

encrypted_message = PM1 // k

tab = []

i = 0
while encrypted_message > 0:
    a = encrypted_message % 200
    tab.append(a)
    encrypted_message = (encrypted_message - a) // 200
tab.reverse()
str_tab = []
for t in tab:
    str_tab.append(chr(t))

print(''.join(str_tab))
