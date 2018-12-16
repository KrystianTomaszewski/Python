
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