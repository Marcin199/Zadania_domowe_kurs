"""Zakładamy, że 1 ludzki rok, to 5 lat psich.
​
Za pomocą konsoli wczytaj imię i wiek psa.
​
Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.
​
Przykład:
Podaj imię psa - Burek
Podaj wiek psa - 3
​
Gdyby Burek był człowiekiem, miałby 15 lat.
"""

class WiekPsa:
    def policz(self):

        zm_1 = input("Proszę, podaj imię psa : ")
        zm_2 = int(input("Teraz podaj wiek psa : "))
        zm_3 = zm_2*5

        print(f"Gdyby {zm_1} był człowiekiem, miałby {zm_3} lat. ")

WiekPsa_1 = WiekPsa()
WiekPsa_1.policz()