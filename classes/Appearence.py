import random

class Appearence:
    def __init__(self):
        self.eager = None
        self.hair = None
        self.eyes = None
        self.height = None
    
    def ask_about_app(self):
        while True:
            eager = input("Czy chcesz wpisać cechy wyglądu?(t/n): ")
            if eager == "t":
                self.eager = True
                break
            if eager == "n" or eager == "":
                self.eager = False
                break
    
    def get_hair(self,character):
        if self.eager == True:
            slownik_do_wybierania_wlosow = {}
            a = 1
            zasieg =["1"]
            for key, value in character.race.slownik_do_losowania_wlosow.items():
                if value not in slownik_do_wybierania_wlosow.values():
                    slownik_do_wybierania_wlosow[a] = value
                    a += 1
                    zasieg.append(str(a))
            while True:         
                hair = input(f"{slownik_do_wybierania_wlosow} \n Podaj kolor włosów(nr): ")
                if hair in zasieg:
                    self.hair = slownik_do_wybierania_wlosow[int(hair)]
                    break

        if self.eager == False:
            los = random.randint(1,19)
            self.hair = character.race.slownik_do_losowania_wlosow[los]

    def get_eyes(self,character):
        if self.eager == True:
            slownik_do_wybierania_oczu = {}
            zasieg =["1"]
            a = 1
            for key, value in character.race.slownik_do_losowania_oczu.items():
                if value not in slownik_do_wybierania_oczu.values():
                    slownik_do_wybierania_oczu[a] = value
                    a += 1
                    zasieg.append(str(a))

            while True:
                eyes = input(f"{slownik_do_wybierania_oczu} \n Podaj kolor oczu(nr): ")
                if eyes in zasieg:
                    self.eyes = slownik_do_wybierania_oczu[int(eyes)]
                    break
        if self.eager == False:
            los = random.randint(1,19)
            self.eyes = character.race.slownik_do_losowania_oczu[los]

    def get_height(self,character):
        wzrost = character.race.wzrost_bazowe_i_liczba_K10
        if self.eager == True:
            max_wzrost = wzrost[0] + (wzrost[1]*10)
            min_wzrost = wzrost[0] + (wzrost[1])
            zasieg = range(min_wzrost,(max_wzrost+1))
            while True:     
                input_wzrost = int(input(f"Podaj wzrost({min_wzrost}-{max_wzrost}): "))
                if input_wzrost in zasieg:
                    self.height = input_wzrost
                    break

        if self.eager == False:
            a = wzrost[1]
            random_wzrost = wzrost[0]
            while a > 0:
                random_wzrost += random.randint(1,10)
                a -= 1
            
            self.height = random_wzrost

