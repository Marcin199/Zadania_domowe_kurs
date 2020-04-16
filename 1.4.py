class hotel:
    def policz(self):
        wiek_1 = int(input("Witaj, proszę podaj swój wiek : "))
        ile_n = int(input("Ile nocy zamierzasz spędzić w hotelu ?"))

        if wiek_1 <= 18:
            op_noc = 100
        elif wiek_1 > 18 and wiek_1 < 65:
            if ile_n == 1:
                op_noc = 200
            elif ile_n > 2 and ile_n < 5:
                op_noc = 180
            else:
                op_noc = 150
        else:
            if ile_n == 1:
                op_noc = 180
            elif ile_n > 2 and ile_n < 5:
                op_noc = 162
            else:
                op_noc = 140
        op_noc_1 = ile_n* op_noc

        print(f"Do zapłaty za cały pobyt w hotelu jest {op_noc_1} zł. ")

hotel_1 = hotel()
hotel_1.policz()





