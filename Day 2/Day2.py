a = [eval(input("pierwsza wartość")), eval(input("druga wartość")), eval(input("trzecia wartość")), eval(input("czwarta wartośc")), eval(input("piąta wartość"))]

list = []
for elem in a:
    if type(elem) is str:
        list.append(elem)
print(list)