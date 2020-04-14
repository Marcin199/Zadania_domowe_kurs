class IleKosztuje:
    def policz(self):
        zm_1 = float (input("Dzień Dobry, prosze podaj cenę, ile kosztuje 1 kilogram ziemniaków : "))
        zm_2 = zm_1 * 5
        print(f"Za pięć kilogramów ziemniaków trzeba będzie zapłacić {zm_2} zł. ")

Ile_Kosztuje = IleKosztuje()
Ile_Kosztuje.policz()

class IleKosztuje_IleKupuje:
    def policz(self):
        zm_1 = float(input("Dzień dobry, proszę podaj cenę, ile kosztuje 1 kilogram ziemniaków : "))
        zm_2 = float(input("Teraz, proszę podaj ile kilogramów ziemniaków chcesz kupić ? : "))
        zm_3 = zm_1 * zm_2
        print(f"Drogi kliencie, za te ziemniaki trzeba będzie zapłacić {zm_3} zł. ")

IleKosztuje_IleKupuje_1 = IleKosztuje_IleKupuje()
IleKosztuje_IleKupuje_1.policz()

class Ziemniki_Banany:
    def policz(self):
        zm_1 = float(input("Dzień dobry, proszę podaj cenę, ile kosztuje 1 kilogram ziemniaków : "))
        zm_2 = float(input("Teraz, proszę podaj ile kilogramów ziemniaków chcesz kupić ? : "))
        zm_3 = float(input("Dzień dobry, proszę podaj cenę, ile kosztuje 1 kilogram bananów : "))
        zm_4 = float(input("Teraz, proszę podaj ile kilogramów bananów chcesz kupić ? : "))

        zm_ziem = zm_1*zm_2
        zm_banan = zm_3*zm_4
        zm_5 = zm_ziem + zm_banan

        if zm_ziem > zm_banan:
            zm_6 = "Ziemniaki"
        else:
            zm_6 = "Banany"
        #zcw = max(zm_ziem, zm_banan)
        print(f"Drogi kliencie, razem za banany oraz ziemniaki trzeba będzie zapłacić {zm_5} zł. ")
        print(f"Więcej trzeba bedzie zapłacić za {zm_6}.")

Ziemniki_Banany_1 = Ziemniki_Banany()
Ziemniki_Banany_1.policz()










