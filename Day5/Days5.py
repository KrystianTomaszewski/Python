class ksiazka:
    def __init__(self, autor, tytul):
        self.autor = autor
        self.tytul = tytul

    def __str__(self):
        return self.tytul + " " + self.autor.imie + " " + self.autor.nazwisko


class autor:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.lista_ksiazek = []

    def dodaj_ksiazke(self):
        self.lista_ksiazek.append(ksiazka)

    def wyswietl_ksiazki(self):
        for ksiazka in self.lista_ksiazek:
            print(ksiazka)


class demo:
    def __init__(self):
        tytul = input("podaj tytul")
        imie_autora = input("podaj imie autora")
        nazwisko_autora = input("podaj nazwisko")

        autor = autor(imie_autora, nazwisko_autora)
        ksiazka = ksiazka(tytul, autor)
        autor.dodaj_ksiazke(ksiazka)
        print(ksiazka)
        print(autor)


demo = demo()


import os
import time

class Pliki:
    def __init__(self):
        print("operacje na plikach")
    def zapis(self):
        self.file = open("myFile.txt", 'a')
        print(self.file.name, self.file.mode, self.file.closed)
        self.file.write("to jest zdanie 1 \n")
        self.file.write("to jest zdanie 2 \n")
        self.file.write("to jest zdanie 3 \n")
        self.file.close()
        print(self.file.name, self.file.mode, self.file.closed)
    def odczyt(self):
        self.file = open("myFile.txt", 'r')
        print(self.file.readlines())
        self.file.close()

    def odczytLiniapoLinii(self):
        self.file = open("myFile.txt", 'r')
        lines = self.file.tell()
        print(lines)
        print(self.file.tell())
        for linia in self.file.read().splitlines():
            print(linia, "log")
        for linia in self.file.read().splitlines():
            print(linia, "log2")

    def testSeek(self):
        self.file = open("myFile.txt", 'r')

        for linia in self.file.read().splitlines():
            print(linia,"log")
        self.file.seek(0)
        for linia in self.file.read().splitlines():
            print(linia,"log")


p = Pliki()
p.zapis()
p.odczyt()
p.odczytLiniapoLinii()
p.testSeek()

p = Pliki()
p.zapis()
p.odczyt()
p.odczytLiniapoLinii()

p = Pliki()
p.zapis()
p.odczytLiniapoLinii()

print("lokalizacja aktualnego katalogu", os.getcwd())
#zmiania aktualnego katalogu
os.chdir('.')
print("lokalizacja aktualnego katalogu", os.getcwd())
s = os.listdir('.')

for i in s:
    print("%20s %20s% 30s" % (i,os.path.getsize(i),time.ctime()))


#os.mkdir('test')
#print(os.path.isdir('test'))

#while(True):
 #   os.mkdir('test66')