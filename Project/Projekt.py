import pymysql

class Connect:

    def __init__(self):
        try:
            self.conn = pymysql.connect(host = "localhost", user="root", password="zaq12wsx", db="Restauracja", port=3307,
                                        charset='utf8')
            print("polaczenie ustanowione")
            self.wybor()
        except:
            print("bledne dane")

    def wybor(self):
        dec = input("1.Gość 2.Logowanie")
        if dec =="1":
            self.menu()
        elif dec=="2":
            self.logowanie()
        else:
            print("Błędna wartość")
            self.wybor()

    def logowanie(self):
        login = input("podaj login")
        passw = input("podaj haslo")

        self.cursor = self.conn.cursor()
        self.cursor.execute("Select * from logowanie WHERE login=%s and passwd=%s", (login,passw))
        resultsLogs = self.cursor.fetchall()

        if(len(resultsLogs) == 1):
            print("zalogowano w systemie")
            self.admenu()
        else:
            print("niepoprawny login lub haslo")
            self.logowanie()

    def menu(self):
        while(True):
            dec = input("P-Pizza, Z-Zupy, D-Dania, K-Kontakt, Q-Wyjdź").upper()

            if(dec=="P"):
                self.Pizza()
            elif (dec=="Z" ):
                self.Zupy()
            elif(dec=="D"):
                self.Dania()
            elif(dec=="K"):
                self.Kontakt()
            elif(dec=="Q"):
                print("Koniec")
                break

    def Pizza(self):
        self.cursor.execute("select * from pizza")
        pizza = self.cursor.fetchall()
        for row in pizza:
            nazwa          = 1
            skladniki      = 2
            Cena           = 3
            print(row[nazwa], row[skladniki], row[Cena])
    def Zupy(self):
        self.cursor.execute("select * from pizza")
        pizza = self.cursor.fetchall()

        for row in pizza:
            nazwa          = 1
            skladniki      = 2
            Cena           = 3
            print(row[nazwa], row[skladniki], row[Cena])

    def Dania(self):
        self.cursor.execute("select * from pizza")
        pizza = self.cursor.fetchall()

        for row in pizza:
            nazwa          = 1
            skladniki      = 2
            Cena           = 3
            print(row[nazwa], row[skladniki], row[Cena])

    def Kontakt(self):
        self.cursor.execute("select * from pizza")
        pizza = self.cursor.fetchall()

        for row in pizza:
            nazwa = 1
            skladniki = 2
            Cena = 3
            print(row[nazwa], row[skladniki], row[Cena])

    def admenu(self):
        while(True):
            dec = input("A-Aktulizacja, U-Usuwanie, D-Dodawanie, Q-Wyjdź").upper()

            if(dec=="A"):
                self.AktualizujMenu()
            elif (dec=="U" ):
                self.UsunMenu()
            elif(dec=="D"):
                self.DodajMenu()
            elif(dec=="Q"):
                print("Koniec")
                break
    def APizza(self):
        self.cursor.execute("select * from pizza")
        pizza = self.cursor.fetchall()
        for row in pizza:
            id             = 1
            nazwa          = 2
            skladniki      = 3
            Cena           = 4
            print(row[id] ,row[nazwa], row[skladniki], row[Cena])

    def AktualizujMenu(self):
        while(True):
            dec = input("P-Pizza, Z-Zupy, D-Dania, W-Wróć").upper()

            if(dec=="P"):
                self.AktualizujPizza()
            elif (dec=="Z" ):
                self.AktulizujZupy()
            elif(dec=="D"):
                self.AktualzujDania()
            elif(dec=="Q"):
                self.admenu()

    def UsunMenu(self):
        while(True):
            dec = input("P-Pizza, Z-Zupy, D-Dania, W-Wróć").upper()

            if(dec=="P"):
                self.UsunPizza()
            elif (dec=="Z" ):
                self.UsunZupy()
            elif(dec=="D"):
                self.UsunDania()
            elif(dec=="Q"):
                self.admenu()

    def DodajMenu(self)        :
        while(True):
            dec = input("P-Pizza, Z-Zupy, D-Dania, W-Wróć").upper()

            if(dec=="P"):
                self.DodaPizza()
            elif (dec=="Z" ):
                self.DodajZupy()
            elif(dec=="D"):
                self.DodajDania()
            elif(dec=="Q"):
                self.admenu()

    def AktualizujPizza(self):
        self.APizza()
        decp = input("Co chcesz uaktulnić N - Nazwe, S-Składniki, C-Cene").upper()
        if(decp=="N"):
            DP = input("podaj id")
            NW = input("podaj nową nazwe")
            self.cursor.execute("UPDATE pizza SET nazwa = %s WHERE id = %s", (NW,DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if(dec=="T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "S"):
            DP = input("podaj id")
            NW = input("podaj nowe składniki")
            self.cursor.execute("UPDATE pizza SET skladniki = %s WHERE id = %s", (NW, DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "C"):
            DP = input("podaj id")
            NW = input("podaj nową cene")
            self.cursor.execute("UPDATE pizza SET Cena = %s WHERE id = %s", (NW, DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")


Connect = Connect()