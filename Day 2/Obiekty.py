class Felga:

    def __init__(self, marka, rozmiar, szerokosc):
        self.marka      = marka
        self.rozmiar    = rozmiar
        self.szerokosc  = szerokosc

    def __str__(self):
        return self.marka + " " + str(self.rozmiar) + " " + str(self.szerokosc)

class Car:

    def __init__(self, color, moc, marka, felga):
        print ("init")
        self.color  = color
        self.moc    = moc
        self.marka  = marka
        self.bak    = 0
        self.felga  = felga
        self.spalanie= 6 #6litrów na 100
    def __str__(self):
        return self.color + " " + self.moc + " " +str(self.bak) + " " +self.felga.marka

    def go_speed(self):
        return "jedź szybko"

    def tankuj(self,ilosc_litrow):
        self.bak += ilosc_litrow

    def __calculate_petrol(self,distance):
        if self.bak <= 0:
            return "brak pusty"
        else:
            self.bak =self.bak - (distance/100) * self.spalanie

    def jedz(self, distance):
        self.__calculate_petrol(distance)


bbs = Felga("bbs", 18, 9)
oz = Felga("oz", 20, 10)

print (bbs)
print(oz)

polonez     = Car("green", "60KM", "polonez",bbs)
audi        = Car("black", "130KM", "polonez",oz)
ford        = Car("white", "105KM", "polonez",oz)

print(polonez.color)
print(audi.color)
print(ford.color)

print(polonez)

print(polonez.go_speed())
audi.tankuj(10)
audi.tankuj(15)
print(audi)

audi.jedz(100)
print(audi)

class Cat:

    def __init__(self,name):
        self.name = name

    def __add__(self, other_cat):
        print ("add invoke")
        return self.name + " " + other_cat.name

    def __sub__(self, other_cat):
        return self.name +" " + other_cat.name + " " + "Odejmowanie"

cat1 = Cat("mruczek")
cat2 = Cat("filemon")

print (cat1+cat2)

class Zawodnik:

    def __init__(self, wzrost, waga, imie):
        self.wzrost =wzrost
        self.waga   =waga
        self.imie   =imie

    def calculate_BMI(self):
        print(self.imie)
        return round(self.waga / (self.wzrost**2),2)

Janusz = Zawodnik(1.7, 90, "Janusz")

print(Janusz.calculate_BMI())