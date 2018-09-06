""" nput data will contai number of test-cases in the first line."""
"""Next lines will contain the sequence of steps (one sequence per line)
as a string of letters. Answer should contain the distances between
starting and ending point for each of sequences, separated by spaces and
with accuracy of 1e-7 at least."""
from math import *

class HexogridMover:
    def __init__(self, firstLine : str):
        self.firstLine = int(firstLine)

    def SecondLine(self):
        massOfStrings = []
        for i in range(self.firstLine):
            massOfStrings.append(input())
        return massOfStrings

    def Builder(self, string : str):
        param = {'A' : [1, 0], 'B' : [0.5, sqrt(3)/2],
                 'C' : [-0.5, sqrt(3)/2], 'D' : [-1, 0],
                 'E' : [-0.5, -sqrt(3)/2], 'F' : [0.5, -sqrt(3)/2]}
        x1, y1 = 0, 0
        for i in string:
            x1 += param[i][0]
            y1 += param[i][1]
        return [x1, y1]

    def Vector(self, arrayXY : list):
        return round(sqrt(arrayXY[0] ** 2 + arrayXY[1] ** 2), 8)

theHexogrid = HexogridMover(int(input()))
ans = []
for i in theHexogrid.SecondLine():
    ans.append(theHexogrid.Vector(theHexogrid.Builder(i)))

print(*ans)
