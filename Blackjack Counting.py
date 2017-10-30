# codeabbey
#codeabbey_my_attempts
#The game of Blackjack has very simple rules: players should take cards one by one trying to collect more points than opponents, but not exceeding 21 (refer Wikipedia for complete rules).

#The deck contains all cards from 2 to 10 inclusive, which are counted according to their value, also Kings, Queens and Jacks which cost 10 points each and also Aces, which could be counted as 1 or 11 points, whatever is better.

#Let us learn the programming of scoring algorithm for such game.

#Input data will contain the number of test-cases in the first line.
#Then test-cases will follow on separate lines. Each test-case consists of several cards expressed with symbols:
#2, 3, 4, 5, 6, 7, 8, 9,
#T, J, Q, K - for 10, Jack, Queen, King,
#A - for Ace.
#Answer should contain the number of points in each test-case, not exceeding 21 - or the word Bust if the total is greater than 21 (i.e. player immediately loss).
  cards = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9,
  "T" : 10, "J" : 10, "K" : 10, "Q" : 10, "A" : [1, 11]}
  otv = []
  for i in range(int(input())):
      slov = input().split()
     hranilishe = []
     tuzi = []
     for i in slov:
         if i != "A":
              hranilishe.append(cards[i])
         else:
              tuzi.append(cards[i])

      dl_tuz = len(tuzi)
      maxim, minim = 0, 0
      if dl_tuz >= 1:
          maxim = 11 + len(tuzi) - 1
         minim = len(tuzi)

     summa = sum(hranilishe)
     a = 0
     if summa + maxim <= 21:
         a = summa + maxim
     else:
          a = summa + minim

     if a > 21:
         a = "Bust"

     otv.append(str(a))
  print(" ".join(otv))
