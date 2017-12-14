"""
Anna lives at Algol and Bob lives at Betelgeuse. Long distance separates them since these stars are in different constellations - Perseus and Orion.

They found a way to communicate via e-mail. However, due to big distance, some letters could be changed during transmission. Simple form of error-checking is proposed by Anna:

All letters are transmitted in usual ASCII code, one byte per symbol. Each byte consists of 8 bits, but the highest bit is not used for English language - it is normally always 0.

Let us set this bit to either 0 or 1 in order that sum of bits in the whole byte is always even (2, 4, 6 or 8). That is how some letters are encoded:

symbol     ascii-code     binary     num-of-bits    encoded-binary   encoded-dec

 'A'           65        01000001         2            01000001           65
 'B'           66        01000010         2            01000010           66
 'C'           67        01000011         3            11000011          195
 '.'           46        00101110         4            00101110           46
 ' '           32        00100000         1            10100000          160
It is supposed that communication line could not change more than one bit in each of the transmitted bytes. So the bytes which have odd amount of bits are considered corrupted.

We are given the message in this protected encoding. Our task is to check each letter and remove those which are corrupted. Others should be converted to normal ASCII and printed as characters.

Input data will contain bytes of the message transmitted (represented by the sequence of decimal values, separated with spaces).
Original message consists only of latin letters (small and capital), digits and spaces.
The end of message is signalled by dot character '.' - you can assume this will never be corrupted.
Answer should contain message with corrupted bytes removed, highest bits cleared - and represented as characters rather than numbers.

Example:

input data:
65 238 236 225 46

answer:
Ana.
"""


line =["{0:b}".format(int(i)) for i in input().split()]

def iteration(x, b, i = 0):
    if i < b:
        if (x[i].count("1") % 2) != 0:
            x.pop(i)
            return iteration(x, b - 1, i)
        else:
            return iteration(x, b, i + 1)
    else:
        for i in range(len(x)):
            if (len(x[i]) == 8) and (x[i][0] == '1'):
                x[i] = list(x[i])
                x[i][0] = '0'
                x[i] = ''.join(x[i])
        return x

class Iterator(object):
    def __init__(self, line):
        self.line = line
        self.dlinn = len(line)
    def iteration(self):
        func = iteration(self.line, self.dlinn)
        new_line = [chr(int(i, 2)) for i in func]
        return print(''.join(new_line))

chto = Iterator(line)


chto.iteration()
