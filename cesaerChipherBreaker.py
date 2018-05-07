5
#JXU VEEB JXUHU MQI QDT XU CQTU XYI FHQOUH YJ SQD RU SQKWXJ RKJ DEJ JXHEMD
#EAYQ AR TUY XUHQP NGF FTQ YAEF AR TUY PUQP FGDZE MXX MDAGZP NGF PAQE ZAF YAHQ
#VGDM LX FTHSZQ FDMSKX VDDOR SGD RDBQDS NE GDZSGDQ ZKD GDQD CHDR HM LX ANRRNL
#QOFHVOUS AIGH PS RSGHFCMSR WH WG PZOQY OBR KVWHS OBR FSR OZZ CJSF
#UVQPG YCNNU FQ PQV C RTKUQP OCMG KP CPEKGPV RGTUKC VJGTG YCU C MKPI


import string

class CesarChiferBreaker(object):
    def __init__(self, strCipher : str):
        self.strCipher = strCipher
        self.ideal = {key : value for (key, value) in
                      zip(string.ascii_uppercase,[8.1, 1.5, 2.8, 4.3, 13.0, 2.2,
                          2.0, 6.1, 7.0, 0.15, 0.77, 7.0, 2.4, 6.8, 7.5, 1.9, 0.095,
                          6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074])}

    def magicMmaker(self, resultingOutput : str, newDict : dict, key : int, koef):
        counter = 0
        istinDlin = 0
        self.zeroHolder = {key : value for (key, value) in
                           zip(string.ascii_uppercase, [0 for i in range(len(string.ascii_uppercase))])}
        for i in  resultingOutput:
            if i != ' ':
                istinDlin += 1
        for i in resultingOutput:
            if i != ' ':
                self.zeroHolder[i] += round(((1 / istinDlin) * 100), 2)
        for i in self.ideal:
            if self.zeroHolder[i] != 0 and \
                abs(self.ideal[i] - self.zeroHolder[i]) <= round(koef, 1):
                counter += 1
        return [counter, resultingOutput]

    def createMove(self, key, koef):
        newDict = {key : value for (key, value) in
                 zip(string.ascii_uppercase[key : 27] +
                    string.ascii_uppercase[0 : key], string.ascii_uppercase)}
        resultingOutput = ""
        for i in self.strCipher:
            if i not in string.ascii_uppercase:
                resultingOutput += i
            else:
                resultingOutput += (newDict[i])
        return self.magicMmaker(resultingOutput, newDict, key, koef)
             
holder = []
for i in range(int(input())):
    ranger = [i for i in range(1, 27)]  
    cipher = CesarChiferBreaker(input())
    koef = 5.0
    maxima = 0
    cipherer = 0
    while len(ranger) > 1:
        item = []
        for key in ranger:
            cipherer = cipher.createMove(key, koef)[0]
            item.append([key, cipherer])
            if cipherer >= maxima:
                maxima = cipherer
        ranger = []
        for i in item:
            if i[1] == maxima:
                ranger.append(i[0])
        koef -= 0.1
    strinn = cipher.createMove(ranger[0], koef + 0.1 )[1]
    strinn = strinn.split()[0 : 3]
    holder.append("{0} {1}".format(' '.join(strinn), ranger[0]))
print(* holder)
