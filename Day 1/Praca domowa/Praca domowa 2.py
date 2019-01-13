class DZIEKANAT:

    def __init__(self, nr_indeksu, imie, nazwisko):
        self.nr_indeksu = nr_indeksu
        self.imie       = imie
        self.nazwisko   = nazwisko

    def __str__(self):
        return self.nr_indeksu + " " + str(self.imie) + " " + str(self.nazwisko)

    def __add__(self, other):
        return self.nr_indeksu + other.nr_indeksu, self.imie + other.imie, + self.nazwisko + other.nazwisko

    def __del__(self):
        return input()

student1 = DZIEKANAT("123456", "Adam", "Nawałka")

