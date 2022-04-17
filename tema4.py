def cmmd(a, b):
    if a == 0:
        return b
    else:
        return cmmd(b % a, a)


class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'{self.numarator}/{self.numitor}'


    def __add__(self, numarator, numitor):
        if self.numitor != numitor:
            numi = self.numitor * numitor
            numa = self.numarator * numitor + numarator * self.numitor
        else:
            numi = self.numitor
            numa = self.numarator + numarator

        return Fractie(numa // cmmd(numa, numi), numi // cmmd(numa, numi))


    def __sub__(self, numarator, numitor):
        if self.numitor != numitor:
            numi = self.numitor * numitor
            numa = self.numarator * numitor - numarator * self.numitor
        else:
            numi = self.numitor
            numa = self.numarator - numarator

        return Fractie(numa // cmmd(numa, numi), numi // cmmd(numa, numi))


    def inverse(self):
        return f'{self.numitor}/{self.numarator}'


print(Fractie(2, 3))

print(Fractie(2, 3).__add__(2, 4))

print(Fractie(2, 3).__sub__(2, 4))

print(Fractie(2, 3).inverse())
