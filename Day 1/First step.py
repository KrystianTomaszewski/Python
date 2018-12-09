a = 1
print (type(a))

a = "sample text"
print (type(a))

a = 1.0
print (type(a))

pi = 3.14
print (type(pi))

myChar = 'a';
print (type(myChar))

imie= "Anna"
adres_zamieszkania = "Nieznana 20"
adreszamieszkania = "Nieznana 20"
drugie_imię = "Beata"
#3ulubionePotrawy = "x, y, z"
#and = 51
and_Dana = 1023
And = "hello"
#twoje zainteresowania = "nurkowanie"
twoje2samochody = "v, m"
śćółżęąćł = " :-) "
twojaSzczesliwaLiczbaKtoraWylosowanoSpecjalnieDlaCiebie= 5


"""
    W ten sposób ustala się długie komentarza
"""

a = 45
print(a)
b = "szkolenie"
print(b)
c = 23.5
print(c)
d = 'Test'
print(d)
e = '?'
print(e)
print(a,b,c,d,e)

##################################
# Syntax
##################################

##################################
# Tuple
##################################
# W pythonie liczymy od 0
a = (1,2,3)
print (type(a))

print (a[0])
print (a[1])
print (a[2])

a = (1,2,3,'s','a','m','p','l','e')
print (type(a))
print (a[4])
"""
#one element tuple
a = (1,)
print (type(a))
"""
#TUPLE są niemodyfikowalne
#a[0] = 4

a = 1,2,3,4,'s','a','m','p','l','e'
print (type(a))

a = tuple((1,2,3))
print (type(a))

##################################
# List
##################################

a = [1,2,3,4,5,'s','a','m','p','l','e']
print (type(a))

print (a[6])
#podmiana wartości pod indeksem
a[2] = 'nowa'
print (a)
#dodanie wartości na końcu
a.append('nowa2')
print (a)
#dodanie wartości n wybranej pozycji
a.insert(2,'nowa3')
print (a)
#usywanie elemnetów
del (a[0])

print (a)

print(len(a))

a_tuple = (tuple(a))
print (type(a_tuple))


a = 1
b = 2

c = a
a = b
b = c

print (a) #2
print (b) #1

a = 1
b = 2

a,b = b,a

print (a) #2
print (b) #1

a = (1,2,3,'s','a','m','p','l','e')
#Pętla for each
for elem in a:
    print (elem)
#elem to zmienna, można uzyć czego chcemy

a = list(range(1,6,1))
print (a)
mylist = (1,2,'log',4,5,'s','a','m','p','l','e')
counter = 0
for elem in a:
    print (mylist[counter])
    counter +=1 #counter = counter + 1

my_tuple = ('a','b','c')
for elem in my_tuple:
    print (elem)
a = list(range(1,3)) #< )
print (a)
qqq = 0
for ab in a:
    print (my_tuple[qqq])
    qqq +=1

a = ['a','b','c','d','e']

for elem in a:
    print (elem)
my_lst = list(range(7,10))
print (my_lst)
counter = 0
for elem in my_lst:
    print (a[counter])
    counter = counter + 1


a = [1,2,3,4,5]

for elem in a:
    print (elem * 2)

a = ['a', 'b', 'c']
for elem in a:
    print(elem * 2)


a = [1,2,3,4,5,6,7,8,9,10]
a = (list(range(1,11,1)))

new_list = []
new_list2 = []
for elem in a:
    if elem > 3:
        new_list.append(elem)
    elif elem <=3:
        new_list2.append(elem)
print(new_list)
print(new_list2)

a = [1,2,3,4,5,6,7,8,9,10]

new_list3 = []
for elem in a:
    if elem % 2 == 0:
        new_list3.append(elem)
print (new_list3)

a = "sample text"

for letter in a:
    print (letter)

#formuła dopóki
counter = 0
while counter<5:
    print (counter)
    counter +=1

counter = 0
while counter < 4:
    print (counter)
    counter +=1

while 1==1:
    counter = 4
    if counter > 0:
        break
    counter =- 1

if 1<2:
    pass

##################################
# SET
##################################

a = [1,1,1,2,3,4,5]
b = 'sample text'
c = (1,2,1,2,3)


a_set = set(a)
print (type(a_set))
b_set = set(b)
print (type(b_set))
c_set = set(a)
print (type(c_set))

print(a_set)
print(b_set)
print(c_set)

for elem in a_set:
    if elem ==1:
        print ("ok")
print (1 in a)

a = {1,1,1,1,2,2,3,4,3,}
print (a)
a.add(1)
a.add(4)
print(a)

a.remove(1)
print(a)
#frozen set , niemodyfikowalne
a = [1,2,3]
a_set = frozenset(a)


##################################
# Dictionary
##################################

numbers = {
    'a':2,
    'b':3,
    'c':4
}
print (numbers)
print (type(numbers))
print (numbers['b'])
print (numbers['c'])
print (numbers.keys())
print (numbers.values())
print (numbers.items())
items = numbers.items()
for item in items:
    print (item[0])
    print (item[1])

#slices
a = [1,2,3,4,5,6,7,8,9,10]
print (a[0:3:1])
print (a[0:7:2])
print (a[len(a) - 1])
#ostatni element
print (a[-1])
print (a[-1:-4:-1])
print (a[::])
print (a[::-1])

text = "sample text"
textList = text.split(" ")
print (textList)
print (" ".join(textList))

a = "Ciekawe"
b = "Programowanie"
c = "Jest"
d = "Wciągające"
e = "I"
f = " "

print (b +f + c + f + a + f + e + f + d)