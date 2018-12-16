
oceny       ={2,3,3.5,4,4.5,5}
wprowadzone =[]
suma        =0
while 1==1:

    ocena = input("wprowadź ocenę")

    if ocena == "":
        for ocena in wprowadzone:
            suma = suma + ocena
        break
    else:
        try:
            ocena = float(ocena)
            if ocena in oceny:
                wprowadzone.append(ocena)
            else:
                print("nie ma takiej oceny")
        except:
            print ("błędna wartość")

print("srednia ocen: %4.1f" % (suma/len(wprowadzone)))





def calculate_square(x):
    return x **2

print(calculate_square(3))

def calculate_even(x):
    if x % 2 == 0:
        return "parzysta"
    else:
        return "nieparzysta"
print (calculate_even(5))

def fun(*args):
    print (type(args))
    suma = 0
    for x in args:
        suma+=x
    return suma

print (fun(1,2,3,4,5))

def silnia(n):

    wynik = 1
    while(n>1):
        wynik *= n
        n -= 1
    return wynik
print(silnia(5))

def fib(n):
    L = [1,1]
    i = 2
    while(i <= n):
        L.append(L[i-2]+L[i-1])
        i+=1
    return sum(L)
print(fib(5))

from random import randint
def losowe_zdanie(n=5):

    wyrazy= ["ala","ma","kota","a","kot","ma","ale"]

    i = 0
    zdanie = ""

    while i<n:
        index_los=randint(0, len(wyrazy)-1)
        zdanie += wyrazy[index_los]
        i +=1
    return zdanie
print(losowe_zdanie(3))

def dist(p1,p2):
    return((p1[0]-p1[0])**2+ (p2[1] - p2[1])**2)**0.5
p1_x = int(input("p1_x"))
p1_y = int(input("p1_y"))
p2_x = int(input("p2_x"))
p2_y = int(input("p2_y"))
print(dist( (p1_x,p1_y),(p2_x,p2_y)))

def srednia(*arg):
    ilosc = len(arg)
    suma = 0
    if ilosc == 0:
        return 0
    else:
        for x in arg:
            suma += x
        return suma/ilosc

print(srednia(1,2,3,4,5))

def myHTML(color = 'black', size = 16, text='Lorem Ipsum'):
    return '<span style="color %s; font-size: %s; ">%s</span>' % (color, size, text)
print(myHTML())

#p64
color = 'white'
def color_change():
    global color
    if color == "white":
        color = "black"
    else:
        color = "white"
    return color

print(color_change())
print(color_change())
print(color_change())
print(color_change())
print(color_change())
print(color_change())

from random import randint
def fun(min,ilosc):
    lst = []
    for elem in range(0, ilosc):
        lst.append(randint(-1000,1000))
    print(lst, "wylosowane liczby")
    lst_upper_than_min =[]
    suma = 0
    for elem in lst:
        if elem > min:
            lst_upper_than_min.append(elem)
            suma += elem
    return (lst_upper_than_min, "wylosowane liczby"),suma

print(fun(10,5))

def fun(**args):
    return args

print (fun(a=1, b=2,c=3))
print (fun(a=1, b=2))
print (fun(a=1))

def fun(text):
    return text.replace(" ","") == text[::-1].replace(" ","")

print(fun("kajak"))
print(fun("palindrom"))
