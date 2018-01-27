#Cards Shuffling

class Making(object):
    def __init__(self, task):
        self.ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
        self.suits = ["C", "D", "H", "S"]
        self.task = task

    def pack_maker(self):
        pack = []
        for j in self.suits:
            for i in self.ranks:        
                pack.append(j+i)      
        self.mass = pack

    def raschet(self):
        init = Making.pack_maker(self)
        for i in range(52):
            a = self.mass[i]
            self.mass[i] = self.mass[self.task[i]]
            self.mass[self.task[i]] = a
                 
    def __str__(self):
        init  = Making.raschet(self)
        otv = " ".join(self.mass)
        return otv
        
        
task = [(int(i)%52) for i in input().split()]
new = Making(task)
print(new)
