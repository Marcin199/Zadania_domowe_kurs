"""## 2. Pętle i struktury danych
​
### Zadanie 2.1 | Zagadka matematyczna
​
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
 """
from random import*
class Zagadka:
    def glowa(self):
        pierwsza_liczba = randint(0,100)
        druga_liczba = randint(0,100)
        wynik = pierwsza_liczba + druga_liczba


        print(f"Policz w głowie sumę tych dwóch liczb: {pierwsza_liczba} , {druga_liczba}")

        while True:
            try:
                wy_1 = int(input("Podaj obliczony przez Ciebie wynik : "))
                if wy_1 == wynik:
                    print("Brawo prawidłowo obliczyłeś sumę!")
                    break
            except:
                print("Nie podałeś liczby")


Zagadka_1 = Zagadka()
Zagadka_1.glowa()
