#co jeśli we wtorek i 7dni naprawa itd..

class szewc():
    def policz(self):
        zm_1 = input("Proszę, podaj w który dzień tygodnia oddałeś buty do naprawy ?")
        zm_2 = int(input("Proszę podaj, ile chcesz, żeby trwała naprawa ?"))

        Poniedziałek = 1
        Wtorek = 2
        Sroda = 3
        Czwartek = 4
        Piatek = 5
        Sobota = 6
        Niedziela = 7

        dzien = 0


        if zm_1 == "Poniedziałek":
            dzien = Poniedziałek + zm_2
        elif zm_1 == "Wtorek":
            dzien = Wtorek + zm_2
        elif zm_1 == "Środa":
            dzien = Sroda + zm_2
        elif zm_1 == "Czwartek":
            dzien = Czwartek + zm_2
        elif zm_1 == "Piątek":
            dzien = Piatek + zm_2
        elif zm_1 == "Sobota":
            dzien = Sobota + zm_2
        elif zm_1 == "Niedziela":
            dzien = Niedziela + zm_2
        else:
            print("Nieprwidłowy dzień tygodnia")


        if dzien == 1:
            d_1 = "w Poniedziałek"
        elif dzien == 2:
            d_1 = "we Wtorek"
        elif dzien == 3:
            d_1 = "w Środę"
        elif dzien == 4:
            d_1 = "w Czwartek"
        elif dzien == 5:
            d_1 = "w Piatek"
        elif dzien == 6:
            d_1 = "w Sobotę"
        elif dzien == 7:
            d_1 = "w niedzielę"
        else:
            print("Wszystkie terminy zajęte")



        print(f"Buty będą gotowe do odbioru {d_1}")




szewc_1 = szewc()
szewc_1.policz()