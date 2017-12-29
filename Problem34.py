from math import *



def schitatel(A, B, C, D, n = 1, x = 1, staroe = uravnenie):
    uravnenie = A * x + B * sqrt(pow(x, 3)) - C * exp(-x/50) - D

    if uravnenie > 0 and uravnenie < 0.00000001:
        return x

    elif uravnenie < 0 and staroe < 0:
        return schitatel(A, B, C, D, n, x * 10, staroe = uravnenie)

    elif uravnenie > 0 and staroe < 0:
        n = x / 10
        x -= n
        return schitatel(A, B, C, D, n, x, staroe = uravnenie)

    elif staroe > uravnenie and uravnenie > 0:
        x -= n
        return schitatel(A, B, C, D, n, x, staroe = uravnenie)

    elif uravnenie < 0 and staroe > 0:
        x += n
        n = n / 10
        x -= n
        return schitatel(A, B, C, D, n, x, staroe)


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
    uravnenie = A * x + B * sqrt(pow(x, 3)) - C * exp(-x/50) - D
    bolsh.append(str(schitatel(A, B, C, D, n = 1, x = 1, staroe = uravnenie)))

print(" ".join(bolsh))
