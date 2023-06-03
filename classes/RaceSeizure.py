import random
from classes.RaceTraits import RaceTraits

class RaceSeizure:
    tabela_ras = {
    1: "Leśny elf", 2: "Wysoki elf", 3: "Krasnolud", 4: "Niziołek", 5: "Człowiek"
    }
    rasy_str = ""
    def formatowanie_wyswietlania_tablicy_ras(self, tabela_ras):
        global rasy_str
        rasy_str = ""
        a = 1
        for key, value in tabela_ras.items():
            b = ""
            c = len(value)
            d = 30 - len(value) - len(str(key))

            while d > 0:
                b = b + " "
                d = d - 1

            if a % 4 != 0:
                rasy_str = rasy_str + str(key) + " - " + value + b

            if a % 4 == 0:
                rasy_str = rasy_str + str(key) + " - " + value + "\n"
            a = a + 1

        self.rasy_str=rasy_str
        
    # input rasy przez uzytkownika
    def ask_for_race(self):
        self.formatowanie_wyswietlania_tablicy_ras(self.tabela_ras)

        while True:
            zasieg = ["1", "2", "3", "4", "5"]
            input_rasa = input(f"{self.rasy_str} \nJaką rasę chcesz wybrać:(1-5) \nZostaw puste, jeśli rasa ma być losowa  ")
            if input_rasa in zasieg:

                self.input_rasa = input_rasa
                break
            
            if input_rasa == "":
                self.input_rasa = None
                break

    # Dodanie wybranej rasy, lub losowej w postaci obiektu RaceTraits
    def give_race(self, character):
        if self.input_rasa != None:
            character.race  = self.tabela_ras[int(self.input_rasa)]

        if self.input_rasa == None:
            K100 = random.randint(1,100)
            lesny = [100]
            wysoki = [99]
            kras = [98, 97, 96, 95]
            hobbit = [94, 93, 92, 91]
            if K100 in wysoki:
                character.race = "Wysoki elf"
            if K100 in lesny:
                character.race = "Leśny elf"
            if K100 in kras:
                character.race = "Krasnolud"
            if K100 in hobbit:
                character.race = "Niziołek"
            if K100 < 91:
                character.race = "Człowiek"
        
        if character.race == "Wysoki elf":
            from rasy.wysoki_elf import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = character.race
        if character.race == "Leśny elf":
            from rasy.lesny_elf import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = character.race
        if character.race == "Krasnolud":
            from rasy.khazad import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = character.race
        if character.race == "Niziołek":
            from rasy.hobbit import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = character.race
        if character.race == "Człowiek":
            from rasy.czlowiek import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
            nazwa = character.race
            
        
    
    
        character.race = RaceTraits(nazwa = nazwa, cechy = cechy, sz = szybkosc, pb = punkty_bohatera0, pp = punkty_przeznaczenia0, p0 = punkty_wolne, profesje = profesje, umiejki = umiejki, talenty=talentyx, wzrost=wzrost, imiex_m=imiex_m, imiex_z=imiex_z, wlosy = wlosy, oczy=oczy )