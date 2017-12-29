from math import *


def schitatel(A, B, C, D, staroe, n = 1, x = 1):
    uravnenie = A * x + B * sqrt(pow(x, 3)) - C * exp(-x/50) - D

    if uravnenie > 0 and uravnenie < 0.000000001:
        #print("1 x=", x, " n=", n, " staroe=", staroe, " uravnenie=", uravnenie)
        return x

    elif uravnenie < 0 and staroe < 0:
        staroe = uravnenie
        #print("2 x=", x, " n=", n, " staroe=", staroe, " uravnenie=", uravnenie)
        return schitatel(A, B, C, D, staroe, n, x * 10)

    elif uravnenie > 0 and staroe < 0:
        n = x / 10
        x -= n
        staroe = uravnenie
        #print("3 x=", x, " n=", n, " staroe=", staroe, " uravnenie=", uravnenie)
        return schitatel(A, B, C, D, staroe, n, x)

    elif staroe > uravnenie and uravnenie > 0:
        x -= n
        staroe = uravnenie
        #print("4 x=", x, " n=", n, " staroe=", staroe, " uravnenie=", uravnenie)
        return schitatel(A, B, C, D, staroe, n, x)

    elif uravnenie < 0 and staroe > 0:
        x += n
        n = n / 10
        x -= n
        #print("5 x=", x, " n=", n, " staroe=", staroe, " uravnenie=", uravnenie)
        return schitatel(A, B, C, D, staroe, n, x)
    print("Promazal")

#x = 0
#uravnenie = A * x + B * sqrt(pow(x, 3)) - C * exp(-x/50) - D

n = int(input())
bolsh = []
for i in range(n):
    x = 0
    mass = [float(mass) for mass in input().split()]
    A = mass[0]
    B = mass[1]
    C = mass[2]
    D = mass[3]
    staroe = A * x + B * sqrt(pow(x, 3)) - C * exp(-x/50) - D
    bolsh.append(str(schitatel(A, B, C, D, staroe, n = 1, x = 1)))

print(" ".join(bolsh))
