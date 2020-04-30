class IleKosztuje:
    def policz(self):
        ziemniaki = float (input("Dzień Dobry, prosze podaj cenę, ile kosztuje 1 kilogram ziemniaków : "))
        cena = ziemniaki * 5
        print(f"Za pięć kilogramów ziemniaków trzeba będzie zapłacić {cena} zł. ")

Ile_Kosztuje = IleKosztuje()
Ile_Kosztuje.policz()

class IleKosztuje_IleKupuje:
    def policz(self):
        ziemniaki = float(input("Dzień dobry, proszę podaj cenę, ile kosztuje 1 kilogram ziemniaków : "))
        kilogramy = float(input("Teraz, proszę podaj ile kilogramów ziemniaków chcesz kupić ? : "))
        suma = ziemniaki * kilogramy
        print(f"Drogi kliencie, za te ziemniaki trzeba będzie zapłacić {suma} zł. ")

IleKosztuje_IleKupuje_1 = IleKosztuje_IleKupuje()
IleKosztuje_IleKupuje_1.policz()

class Ziemniki_Banany:
    def policz(self):
        ziemniaki = float(input("Dzień dobry, proszę podaj cenę, ile kosztuje 1 kilogram ziemniaków : "))
        kilo_ziemniaki = float(input("Teraz, proszę podaj ile kilogramów ziemniaków chcesz kupić ? : "))
        banany = float(input("Dzień dobry, proszę podaj cenę, ile kosztuje 1 kilogram bananów : "))
        kilo_banany = float(input("Teraz, proszę podaj ile kilogramów bananów chcesz kupić ? : "))

        zm_ziem = ziemniaki*kilo_ziemniaki
        zm_banan = banany*kilo_banany
        suma_zakupy = zm_ziem + zm_banan

        if zm_ziem > zm_banan:
            produkt = "Ziemniaki"
        else:
            produkt = "Banany"
        #zcw = max(zm_ziem, zm_banan)
        print(f"Drogi kliencie, razem za banany oraz ziemniaki trzeba będzie zapłacić {suma_zakupy} zł. ")
        print(f"Więcej trzeba bedzie zapłacić za {produkt}.")

Ziemniki_Banany_1 = Ziemniki_Banany()
Ziemniki_Banany_1.policz()










