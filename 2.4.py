"""Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
​
Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją i pełni w informatyce bardzo ważną rolę.
Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024).

Zgadnij liczbę, którą wylosowałem: 50
Twoja liczba jest za mała.
Zgadnij liczbę, którą wylosowałem: 100
Twoja liczba jest za mała.
Zgadnij liczbę, którą wylosowałem: 400
Twoja liczba jest za duża.
Zgadnij liczbę, którą wylosowałem: 300
Twoja liczba jest za duża.
Zgadnij liczbę, którą wylosowałem: 200
Twoja liczba jest za mała.
Zgadnij liczbę, którą wylosowałem: 250
Twoja liczba jest za duża.
Zgadnij liczbę, którą wylosowałem: 230
Twoja liczba jest za duża.
Zgadnij liczbę, którą wylosowałem: 220
Brawo zgadłeś liczbę :)

"""

from random import*

podejscia = 0
zm_1 = randint(0,999)
#print(zm_1)
while podejscia < 10:
    podejscia +=1
    zgadnij_liczbe = int(input("Zgadnij liczbę, którą wylosowałem: "))
    if zm_1 < zgadnij_liczbe:
        print('Twoja liczba jest za duża.')
    if zm_1 > zgadnij_liczbe:
        print('Twoja liczba jest za mała.')

    if zm_1 == zgadnij_liczbe:
        break

if zm_1 == zgadnij_liczbe:
    print("Brawo zgadłeś liczbę :)")



