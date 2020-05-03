"""Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena. Wyświetl odpowiedni komunikat.
​
Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10

Za ziemniaki, który chcesz kupić, zapłacisz 50 zł
"""
class Zakupy:
    def policz(self):
        zakupy = input("Dzień dobry, co chcesz kupić ? ")
        cena_towaru = float(input("Podaj cenę towaru : "))
        ilosc = float(input("Podaj ilość towaru :"))
        try:
            if zakupy == "ziemniaki" or zakupy == "Ziemniaki":
                suma = cena_towaru * ilosc
                print(f"Za ziemniaki, które chcesz kupić , zapłacisz {suma} zł.")
            else:
                print("W bazie nie ma takiego towaru. Poproś sprzedawcę o pomoc.")
        except:
            print("Brak towaru w bazie.Skontaktuj się z pracownikiem sklepu. ")


Zakupy_1 = Zakupy()
Zakupy_1.policz()



