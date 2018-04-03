from math import *

otvetprime = [] #array of prime numbers
massiveOfIntegers = [] #initialise the massive

"""fill the massive with integers"""
for i in range(int(input())): #amount of integer to factorize in the first line
    massiveOfIntegers.append(int(input()))




"""let's make primes numbers consecration"""
mMOIF = int(sqrt(max(massiveOfIntegers)))
primeNumbers = [i for i in range(2, mMOIF)]
lPN = len(primeNumbers)
start = 2 #start with 4 in massiveOfIntegers
shag  = 2 #step in consecration
for i in range(int(sqrt(mMOIF))):
    for j in range(start, lPN, shag):
        primeNumbers[j] = None
    start += 2
    shag += 1


for i in primeNumbers:
    if i != None:
        otvetprime.append(i)

status = True
otvetit_za_vseh = ""
otvetZaVseh = []
"""Using now massiveOfIntegers and otvetprime"""
for number in range(len(massiveOfIntegers)):
    prime = 0
    while status:
        if otvetprime[prime] >= massiveOfIntegers[number]:
            otvetit_za_vseh += str(massiveOfIntegers[number])
            break
        elif massiveOfIntegers[number] % otvetprime[prime] == 0:
            otvetit_za_vseh += str(otvetprime[prime]) + "*"
            massiveOfIntegers[number] = int(massiveOfIntegers[number]/otvetprime[prime])
        elif prime == len(otvetprime) - 1:
            otvetit_za_vseh += str(massiveOfIntegers[number])
            break
        else:
            prime += 1
    otvetZaVseh.append(otvetit_za_vseh)
    otvetit_za_vseh = ""

print(*otvetZaVseh)
