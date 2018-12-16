from random import randint

class lotto:

    def __init__(self):
        self.wynik =set()
        self.__losuj()

    def __losuj(self):
        while(len(self.wynik)<6):
            self.wynik.add(randint(1,49))

    def pokaz(self):
        return self.wynik

los1 = lotto()
print(los1.pokaz())