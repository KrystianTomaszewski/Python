A=11
B=5
C=1

Z_towar = []
Cena = 0
Paragon = []
while 1==1:
    zamowienie = input("zamówienie")
    if zamowienie == "":
        Paragon.append(Z_towar)
        Paragon.append(str(Cena))
        break
    else:
        try:
            ilosc = input("podaj ilosc")
            if float(zamowienie) == 1:
                if float(A) - float(ilosc) >= 0:
                    Z_towar.append("A")
                    Cena = Cena + (float(ilosc) * float(3.5))
                else:
                    print("Brak towaru A")
            elif float(zamowienie) == 2:
                if float(B) - float(ilosc) >= 0:
                    Z_towar.append("B")
                    Cena = Cena + (float(ilosc) * float(2.99))
                else:
                    print("Brak towaru B")
            elif float(zamowienie) == 3:
                if float(C) - float(ilosc) >= 0:
                    Z_towar.append("C")
                    Cena = Cena + (float(ilosc) * float(9.99))
                else:
                    print("Brak towaru C")
            print(Z_towar)
            print(Cena)
        except:
            print("Błędna wartość")
print("Paragon")
print(Paragon)
