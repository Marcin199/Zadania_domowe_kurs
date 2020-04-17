"""Napisz program, który odczytuje od użytkownika wiele liczb.
​
Program powinien wyliczyć i na końcu wypisać następujące statystyki:
​
- liczba podanych liczb (ile sztuk)
- suma
- średnia
- minimum
- maksimum
​
NIE używaj funkcji wbudowanych!
"""




zm_3 = 0
suma = 0
licz = 0
minimum = None
maximum = None

while licz < 5:
    zm_1 = int(input("Podaj liczbę: "))
    zm_3 += 1
    suma += zm_1
    liczba = zm_1

    if minimum is None or liczba < minimum:
        minimum = liczba
    if maximum is None or liczba > maximum:
        maximum = liczba

    if zm_3 >= 5:
        srednia = suma / zm_3
        print(f"Liczba podanych liczb: {zm_3}\n"
              f"Suma wszystkich liczb : {suma}\n"
              f"Średnia ze wszystkich liczb: {srednia}\n"
              f"Minimalna liczba to {minimum}\n"
              f"Maksymalna liczba to {maximum}")
        break





