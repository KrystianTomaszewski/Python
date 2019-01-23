import pymysql


"""
Obiekt kursora:
Aby móc wykonywać operacje na bazie,potrzebujemy obiekt tzw.kursora służy do pobierania 
oraz modyfikacji danych w bazie danych
"""

class DBConnect:

    def __init__(self):
        try:
            self.conn = pymysql.connect(host = "localhost", user="root", password="zaq12wsx", db="Python", port=3307,
                                        charset='utf8')
            print("polaczenie ustanowione")

            self.logowanie()

        except:
            print("bledne dane")

    def logowanie(self):
        login = input("podaj login")
        passw = input("podaj haslo")

        self.cursor = self.conn.cursor()
        self.cursor.execute("Select * from logowanie WHERE login=%s and passwd=%s", (login,passw))
        resultsLogs = self.cursor.fetchall()

        if(len(resultsLogs) == 1):
            print("zalogowano w systemie")
            self.menu()
        else:
            print("niepoprawny login lub haslo")
            self.logowanie()

    def menu(self):
        while(True):
            dec = input("S-show, I-insert, D-delete,U-Update, T-Test, Q-exit").upper()

            if(dec=="S"):
                self.select()
            elif (dec=="I" ):
                self.insert()
            elif(dec=="D"):
                self.delete()
            elif(dec=="U"):
                self.update()
            elif(dec=="T"):
                self.tajemnica()
            elif(dec=="Q"):
                self.exit()
    def exit(self):
        exit()
    def tajemnica(self):
        self.cursor.execute("select * from `pracownicy`")
        a = int(input("druga wartość"))
        b = int(input("druga wartość"))
        pracownicy = self.cursor.fetchall()[a][b]
        print(pracownicy)
    def update(self):
        self.select()
        decp = input("Co chcesz uaktulnić I - Imie, N-Nazwisko, P-pesel, D-data urodzenia").upper()
        if(decp=="I"):
            DP = input("podaj Pesel")
            NW = input("podaj nowe imie")
            self.cursor.execute("UPDATE pracownicy SET imie = %s WHERE pesel = %s", (NW,DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if(dec=="T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "N"):
            DP = input("podaj Pesel")
            NW = input("podaj nowe nazwisko")
            self.cursor.execute("UPDATE pracownicy SET nazwisko = %s WHERE pesel = %s", (NW, DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "P"):
            DP = input("podaj Pesel")
            NW = input("podaj nowy Pesel")
            self.cursor.execute("UPDATE pracownicy SET pesel = %s WHERE pesel = %s", (NW, DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "D"):
            DP = input("podaj Pesel")
            NW = input("podaj nową datę(YYYY-MM-DD)")
            self.cursor.execute("UPDATE pracownicy SET data_ur = %s WHERE pesel = %s", (NW, DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        else:
            self.conn.rollback()
            print("podano błedna wartość")
    def delete(self):
        self.select()
        pesel = input("pesel")
        self.cursor.execute("DELETE FROM pracownicy WHERE pesel = %s", pesel)
        dec = input("Czy na pewno chcesz usunąc rekord T/N").upper()
        if(dec=="T"):
            self.conn.commit()
            print("usunięto rekord")
        else:
            self.conn.rollback()
            print("Come to MENU")

    def insert(self):
        imie     = input("imie")
        nazwisko = input("nazwisko")
        pesel    = input("pesel")
        data     = input("data")

        self.cursor.execute("INSERT INTO pracownicy(imie,nazwisko,pesel,data_ur) values (%s,%s,%s,%s)", (imie,nazwisko,pesel,data))
        self.conn.commit()



    def select(self):
        self.cursor.execute("select * from `pracownicy`")
        pracownicy = self.cursor.fetchall()

        for row in pracownicy:
            Name           = 1
            Surname        = 2
            PESEL          = 3
            Data_urodzenia = 4
            print(row[Name],row[Surname],row[PESEL],row[Data_urodzenia])


DBConnect = DBConnect()