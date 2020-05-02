"""Założenia:
	- 0-6   - wiek przedszkolny - cena biletu: 0
	- 7-17  - wiek szkolny      - cena biletu: 2.28
	- 18-64 - wiek dorosły      - cena biletu: 3.80
	- +65   - wiek emerytalny   - cena biletu: 1.90
​
Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
​
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety,
które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.
"""

class Bilety:
    def policz(self):
        wiek = int(input("Proszę, podaj swój wiek : "))
        ilosc = int(input("Teraz podaj ile biletów chcesz kupić : "))

        if wiek < 6:
            cena_1 = 0
        elif wiek >= 7 and wiek <= 17:
            cena_1 = 2.28
        elif wiek >= 18 and wiek <= 64:
            cena_1 = 3.80
        else:
            cena_1 = 1.90

        suma_1 = cena_1 * ilosc

        print(f"Do zapłaty za bilety jest {suma_1} zł.")

Bilety_1 = Bilety()
Bilety_1.policz()



