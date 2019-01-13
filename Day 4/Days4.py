telefon = {
' ': '#',
'a': '2', 'b': '22', 'c': '222',
'd': '3', 'e': '33', 'f': '333',
'g': '4', 'h': '44', 'i': '444',
'j': '5', 'k': '55', 'l': '555',
'm': '6', 'n': '66', 'o': '666',
'p': '7', 'q': '77', 'r': '777', 's': '7777',
't': '8', 'u': '88', 'v': '888',
'w': '9', 'x': '99', 'y': '999', 'z': '9999'}

text = input("wpis text").lower()
for elem in text:
    print(telefon[elem])

#nie robic
class D:
    arg = 20

class C(D):
    arg = 30

class B(D):
    pass

class A(B, C):
    pass
a =A()
print (a.arg)

class A:
    def fun(self):
        return"funA Invoke"
class B(A):
    def __init__(self):
        self.con = [1,2,3,4,5]
        print(self.fun())
        print(super(B, self).fun())#dla wersji 2
        print(super().fun())# tylko dla wersji 3
        print (A.fun(self))# najbardziej czytelny
    def fun(self):
        return "funB invoke"
b = B()
print(b.fun())


# polimorfizm
class Kot:
    def glos(self):
        print("Miau")


class Pies:
    def glos(self):
        print("hau")


class Krowa:
    def glos(self):
        print(Muuu)

class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return"%s %5.2f zł" % (self.nazwa, self.cena)

class Oprogramowanie(Produkt):
    def __init__(self,nazwa, cena, jezyk, system):
        super().__init__(nazwa,cena)
        self.jezyk = jezyk
        self.system = system

    def rabat(self, procent):
        if(procent <= 10):
            self.cena = round(self.cena - self.cena * (procent/100),2)

    def __str__(self):
        return super().__str__() + ("%s %s" % (self.jezyk, self.system))

class Szkolenie(Oprogramowanie):

    def __init__(self,nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin
    def rabat(self, procent):
        super().rabat(procent)
        if (procent <= 15 and procent >10):
            self.cena = round(self.cena -self.cena * (procent/100),2)
    def __str__(self):
        return super().__str__() + ("%s" % (self.termin))

class Demo:
    def __init__(self):
        o1 = Oprogramowanie("python 3.0",2000,"Python", "win")
        o1.rabat(7)
        print(o1)
        s1 = Szkolenie("Python",1000, "Python", "win", "2019-01-01")
        s1.rabat(5)
        print(s1)
demo = Demo()

class RGB:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other):
        kolorek = RGB((self.r + other.r)/2, (self.g + other.g)/2, (self.b + other.b)/2)
        return kolorek
    def __str__(self):
        return 'RGB[%i, %i, %i]' % (self.r, self.g, self.g)
    pass

k1 =RGB(255,0,0)
print(k1)
k2 =RGB(153,255,51)
print(k2)
k3 = k1 + k2
print(k3)