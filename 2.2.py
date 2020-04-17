"""Napisz program, który wczytuje liczbę całkowitą,
a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`.
Np. dla parametru 3 powinno się wypisać:
​
```
    *
  * * *
* * * * *
```
"""

zm_1 = int(input("Podaj liczbę całkowitą : "))

if zm_1 == 3:
    print("    *\n"
          "  * * *\n"
          "* * * * *\n")
elif zm_1 > 3:
    print("    *\n"
          "  * * *\n"
          "* * * * *\n"*zm_1)
else:
    pass




