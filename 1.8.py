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

        imie = input("Proszę, podaj imię psa : ")
        wiek = int(input("Teraz podaj wiek psa : "))
        lata = wiek*5

        print(f"Gdyby {imie} był człowiekiem, miałby {lata} lat. ")

WiekPsa_1 = WiekPsa()
WiekPsa_1.policz()