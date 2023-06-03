import random
from classes.ProfessionTraits import ProfessionTraits
import importlib
import unicodedata

class ProfessionSeizure:

    tabela_wszystkich_profesji = {
    0: 'Agitator', 1: 'Aptekarz', 2: 'Artysta', 3: 'Banita', 4: 'Biczownik', 5: 'Chłop', 6: 'Czarodziej',
    7: 'Czarownica', 8: 'Doker', 9: 'Domokrążca', 10: 'Doradca', 11: 'Flisak', 12: 'Gladiator', 13: 'Guślarz',
    14: 'Górnik', 15: 'Hiena Cmentarna', 16: 'Inżynier', 17: 'Kapłan', 18: 'Kapłan Bitewny', 19: 'Kawalerzysta',
    20: 'Kuglarz', 21: 'Kupiec', 22: 'Medyk', 23: 'Mieszczanin', 24: 'Mistyk', 25: 'Mnich', 26: 'Namiestnik',
    27: 'Ochroniarz', 28: 'Oprych', 29: 'Paser', 30: 'Pilot Rzeczny', 31: 'Pirat Rzeczny', 32: 'Poseł',
    33: 'Posłaniec', 34: 'Prawnik', 35: 'Przemytnik', 36: 'Przewoźnik', 37: 'Rajfur', 38: 'Rekietier',
    39: 'Rycerz', 40: 'Rzemieślnik', 41: 'Strażnik', 42: 'Strażnik Dróg', 43: 'Strażnik Rzeczny', 44: 'Szarlatan',
    45: 'Szczurołap', 46: 'Szlachcic', 47: 'Szpieg', 48: 'Służący', 49: 'Uczony', 50: 'Woźnica', 51: 'Zabójca',
    52: 'Zarządca', 53: 'Zielarz', 54: 'Zwadźca', 55: 'Zwiadowca', 56: 'Złodziej', 57: 'Łowca',
    58: 'Łowca Czarownic', 59: 'Łowca Nagród', 60: 'Śledczy', 61: 'Żebrak', 62: 'Żeglarz', 63: 'Żołnierz'}

    prof_str = ""
    a = 1
    ########format wyswietlania profesji
    for key, value in tabela_wszystkich_profesji.items():
        b = ""
        c = len(value)
        d = 20 - len(value) - len(str(key))

        while d > 0:
            b = b + " "
            d = d - 1

        if a % 5 != 0:
            prof_str = prof_str + str(key) + " - " + value + b
            # print(prof_str)

        if a % 5 == 0:
            prof_str = prof_str + str(key) + " - " + value + "\n"
            # print(prof_str)

        a = a + 1
    
    def ask_for_profession(self):
        zasieg = range(0,64)
        zasieg_str = []
        for el in zasieg:
            zasieg_str.append(str(el))
        while True:
            wybor = input(f"{self.prof_str}\nJaką profesją chcesz grać? (0-63)\nZostaw puste jeśli chcesz losową profesję ")
            if wybor in zasieg_str:
                self.wybor_prof = wybor
                break
            
            if wybor == "":
                self.wybor_prof = None
                break
    
    def give_profession_name_from_input_or_random(self, character):
        # if character.race.nazwa == "Leśny elf":
        #     tabela_profesji = character.race.tabela_losowania_profesji_slownik
        # if character.race.nazwa == "Wysoki elf":
        #     tabela_profesji = character.race.tabela_losowania_profesji_slownik
        # if character.race.nazwa == "Krasnolud":
        #     tabela_profesji = character.race.tabela_losowania_profesji_slownik
        # if character.race.nazwa == "Leśny elf":
        #     tabela_profesji = character.race.tabela_losowania_profesji_slownik
        # if character.race.nazwa == "Leśny elf":
        #     tabela_profesji = character.race.tabela_losowania_profesji_slownik
        tabela_profesji = character.race.tabela_losowania_profesji_slownik
        if self.wybor_prof == None:
            
            rzut_K100_na_profesje = random.randint(1,100)
            self.nazwa_profesji = tabela_profesji[rzut_K100_na_profesje]

        if self.wybor_prof != None:
            self.nazwa_profesji = self.tabela_wszystkich_profesji[int(self.wybor_prof)]
            if self.nazwa_profesji not in tabela_profesji.values():
                print(f"hmmm {character.race.nazwa} {self.nazwa_profesji}! A little bit weird, ale kim jestem by Ci tego zabraniać")
    def create_ProfessionTraits_object_and_add_to_character(self,character):
        folder = 'profesje'
        file = self.nazwa_profesji.lower()
        #pozbywam się polskich znaków :/ moduł robiący to automatycznie, jest zjebane dla języka polskiego i usuwa ł, zamiast zamienić na l
        file = file.replace("ł", "l")
        file = file.replace(" ", "_")
        normalized = unicodedata.normalize("NFKD", file)
        file = normalized.encode("ASCII", "ignore").decode("utf-8")
        module_name = f'{folder}.{file}'
        profesja_variables = importlib.import_module(module_name)
        character.profession = ProfessionTraits(klasa= profesja_variables.klasa ,nazwa_profesji=profesja_variables.nazwa_profesji, status=profesja_variables.status , rozwiniecia_cech=profesja_variables.rozwiniecia_cech ,slownik_umiejetnosci_oraz_levelu=profesja_variables.slownik_umiejetnosci_oraz_levelu, talenty=profesja_variables.talenty, wyp=profesja_variables.wyp, waga=profesja_variables.waga)
        

# prof = Profession()
# prof.ask_for_profession()