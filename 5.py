# Napisz program wypisujący na konsolę tabliczkę mnożenia
# dla liczb od 0 do 9 w postaci tabelki.

# DO DOMU: przerobić ten program tak, żeby wyświetlał tabliczke mnozenia od 0 do 100

print(" "*4, end="") #3
for i in range(0, 11):  #10
    print(f"{i:4}", end="")  #3

print("\n")

for i in range(0, 11):  #10

    print(f"{i:<4}", end="")   #3

    for j in range(0, 11):  #10
        print(f"{i*j:4}", end="")  #3

    print()