a = [eval(input("pierwsza wartość")), eval(input("druga wartość")), eval(input("trzecia wartość")), eval(input("czwarta wartośc")), eval(input("piąta wartość"))]

list = []
for elem in a:
    if type(elem) is str:
        list.append(elem)
print(list)

slownik = {
    'jeden' : 1,
    'dwa' : 2,
    'trzy' : 3,
    'cztery' : 4,
    'pięć' : 5
}
print(slownik)

a = input("podaj wartośc")
print(slownik[a])
kod = input("podaj kod produtu")
ilosc = int(input("podaj ilosć produktu"))
produkty = {
    "k1": ("nazwak1", 10.0),
    "k2": ("nazwak2", 12.0),
    "k3": ("nazwak3", 155.0)
}

print("zamówienie", produkty[kod][1] * ilosc)

a = [1,2,3]
b =(4,5,6)

aSet = set(a)
bSet = set(b)
print(aSet | bSet)
print(aSet & bSet)
print(aSet - bSet)
print(aSet ^ bSet)

from random import randint
print(randint(1,49))
lotto =set()

while(len(lotto) < 6):
    lotto.add(randint(1,49))
print(lotto)

x = input("podaj wartosc")
mojSet = set()
while x != 'exit':
    mojSet.add(x)
    x = input("podaj wartosc")
print (len(mojSet))

x = input("podaj wartosc")
mojSet = set()
while x != 'exit':
    if x in mojSet:
        exit()
    mojSet.add(x)
    x = input("podaj wartosc")
print (len(mojSet))

if 1<2:
    print("1<2")
elif 1<3:
    print("1<3")
else:
    pass

a = 25
b = 30

print(b) if (a<b) else print(a)
test = list(range(0,5))
if bool(0):
    print(test[0])
if bool(1):
    print(test[1])
if bool(2):
    print(test[2])
if bool(3):
    print(test[3])
if bool(4):
    print(test[4])

test = str(list(range(1,10)))
print(test)

x = int(input("podaj wartość"))
if x in test:
    print("true")
else:
    print("out of range")

 elem = [3, 0, 3, 4, 4]
if (elem[0] >= 0 and elem[1] >= 0):
    print("++")
elif (elem[0] >= 0 and elem[1] < 0):
    print("+-")
elif (elem[0] < 0 and elem[1] >= 0):
    print("-+")
else:
    print("--")

dictionary = {
    0: "parzysta",
    1: "nieparzysta"
}
number = int(input("podajLiczbe") % 2)
print (dictionary[number])

# user : user
# admin : admin

acces_dictionary = {

    "user" : "user",
    "admin" : "admin"
}
login = input("podaj login")
password = input("podaj hasło")

if login in acces_dictionary and password == acces_dictionary[login]:
    print('zalogowany')
    if login == "admin":
        print("panel admina")
    else:
        print("panel użytkownika")
else:
    print("nieprawidłowe dane")

    lst = range(1, 5)

    for elem in lst:
        if elem == 3:
            continue
        print(elem)
    # continue przeskakuje wskazany element
a = [1,2,3,4,5]
for index, value in enumerate(a) :
    print (index,value)

zmienna = enumerate(a)
print(list(zmienna))

Slownik = {"key1": "var1", "key2": "var2", "key3":"var3"}
for key in Slownik:
 print(key, Slownik[key])

 for x in range(5, 100, 10):
     print("%4i%6i%8i" % (x, x ** 2, x ** 3))

 for x in range(5, 100, 10):
     print("pierwiastkiem liczby %2i jest %5.3f" % (x, x ** 0.5))

 for x in range(5, 100, 10):
     print("%-03i%#-6o%#-5x" % (x, x, x))

 for x in range(5, 100, 10):
     print("%-03i %#044o %#04x" % (x, x, x))

 a = 24
 b = "sample"
 c = 27
 d = "text"

 print(str(a) + b + str(c) + d)
 print("%1i %s %i %s" % (a, b, c, d))

 liczby = eval(input("Podaj liczbe:")), eval(input("Podaj liczbe:")), eval(input("Podaj liczbe:"))
 szukana = eval(input("Podaj liczbę do znalezienia:"))
 for p, x in enumerate(liczby):
     if x != szukana:
         continue
     print("Znaleziono liczbę %i na pozycji %i" % (x, p + 1))
     break
 else:
     print("Liczby %i nie ma na liście" % szukana)

cyfry = {
    0: "zero",
    1: "jeden",
    2: "dwa",
    3: "trzy",
    4: "cztery",
    5: "pięć",
    6: "sześć",
    7: "siedem",
    8: "osiem",
    9: "dziewięć"
}
x = input("wprowadź cyfry")
    result = ""
    for elem in x:
        if (elem.isdigit()):
            result += cyfry[int(elem)]
            result += " "
        else:
            result += ""
    print(result)

    numbers = [5, 2, 1, 10]
    print(numbers.index(int(input("podaj number"))))
     # x = int(input("Podaj C"))
     # fahrenheit = (celsius*1.8) - 32
     # print((x*1.8) + 32)

lst = range(40, -21, -5)
for x in lst:
    y = 32 + x * 1.8
        print(x, y)

# P43
    X = list(range(0, 21, 2))
    Y = list(range(0, 11, 1))
XY = (X, Y)
print(XY[0][0], XY[1][0])
print(XY[0][1], XY[1][1])

lista = []
count = 0
while count < 11:
    a = (count * 2, count)
        lista.append(a)
        count = count + 1
    print(lista)

