"""Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena. Wyświetl odpowiedni komunikat.
​
Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10
​
Za ziemniaki, który chcesz kupić, zapłacisz 50 zł
"""
class Zakupy:
    def policz(self):
        zm_1 = input("Dzień dobry, co chcesz kupić ? ")
        zm_2 = float(input("Podaj cenę towaru : "))
        zm_3 = float(input("Podaj ilość towaru :"))

        if zm_1 == "ziemniaki" or zm_1 == "Ziemniaki":
            suma = zm_2 * zm_3
            print(f"Za ziemniaki, które chcesz kupić , zapłacisz {suma} zł.")
        else:
            print("W bazie nie ma takiego towaru. Poproś sprzedawcę o pomoc.")


Zakupy_1 = Zakupy()
Zakupy_1.policz()



