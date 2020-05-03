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




ilosc = 0
suma = 0
licz = 0
minimum = None
maximum = None

while licz < 5:
    liczba_in = int(input("Podaj liczbę: "))
    ilosc += 1
    suma += liczba_in
    liczba = liczba_in

    if minimum is None or liczba < minimum:
        minimum = liczba
    if maximum is None or liczba > maximum:
        maximum = liczba

    if ilosc >= 5:
        srednia = suma / ilosc
        print(f"Liczba podanych liczb: {ilosc}\n"
              f"Suma wszystkich liczb : {suma}\n"
              f"Średnia ze wszystkich liczb: {srednia}\n"
              f"Minimalna liczba to {minimum}\n"
              f"Maksymalna liczba to {maximum}")
        break





