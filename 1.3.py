#coś źle oblicza bmi

class Bmi:
    def policz(self):
        metry = float(input("Proszę podaj swój wzrost w (m) : "))
        wg_1 = float(input("Proszę podaj swoją wagę w (Kg) : "))


        bmi = wg_1 / metry / 2
        #print(bmi)

        wyglodzenie = 16.0
        wychudzenie = 16.99
        niedowaga = 18.49
        pozadana_masa = 24.99
        nadwaga = 29.99
        otyłosc_I_stopnia = 34.99
        otylosc_II_stopnia = 39.99
        otylosc_III_stopnia  = 40.0

        if bmi < wyglodzenie:
            print(f"Twoje BMI wynosi {bmi}. Niestety masz niedowagę. "
                  f"Jesteś wygłodzony!!!\n"
                  f"Ryzyko chorób towarzyszących otyłości jest minimalne, ale\n"
                  f"istnieje zwiększony poziom wystapienia innych problemów"
                  f"zdrowotnych")
        elif bmi > wyglodzenie and bmi < wychudzenie:
            print(f"Twoje BMI wynosi {bmi}. Niestety masz niedowagę. "
                  f"Jesteś wychudzony!!"
                  f"Ryzyko chorób towarzyszących otyłości jest minimalne. ")

        elif bmi > wychudzenie and bmi < niedowaga:
            print(f"Twoje BMI wynosi {bmi}. Niestety masz niedowagę. "
                  f"Ryzyko chorób towarzyszących otyłości jest minimalne. ")

        elif bmi > niedowaga and bmi < pozadana_masa:
            print(f"Twoje BMI wynosi {bmi}. Masz pożądaną masę ciała. "
                  f"Ryzyko chorób towarzyszących otyłości jest minimalne. ")

        elif bmi > pozadana_masa and bmi < nadwaga:
            print(f"Twoje BMI wynosi {bmi}. Niestety masz nadwagę. "
                  f"Ryzyko chorób towarzyszących otyłości jest minimalne. ")

        elif bmi > nadwaga and bmi < otyłosc_I_stopnia:
            print(f"Twoje BMI wynosi {bmi}. Niestety masz nadwagę. "
                  f"Ryzyko chorób towarzyszących otyłości jest średnie. ")

        elif bmi > otyłosc_I_stopnia and bmi < otylosc_II_stopnia:
            print(f"Twoje BMI wynosi {bmi}. To już otyłość. "
                  f"Ryzyko chorób towarzyszących otyłości jest bardzo,"
                  f"wysokie. ")
        elif bmi > otylosc_III_stopnia:
            print(f"Twoje BMI wynosi {bmi}. To już otyłość. "
                  f"Ryzyko chorób towarzyszących otyłości ma postać ,"
                  f"eksremalnego poziomu ryzyka. ")
        else:
            print("coś nie tak poszło, ups..")


bmi_1 = Bmi()
bmi_1.policz()














