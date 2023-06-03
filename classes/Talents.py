import random

class Talents:
    tabela_losowych_talentów = {
    1: 'Atrakcyjny', 2: 'Atrakcyjny', 3: 'Atrakcyjny', 4: 'Bardzo Silny', 5: 'Bardzo Silny',
    6: 'Bardzo Silny', 7: 'Błękitna Krew', 8: 'Błękitna Krew', 9: 'Błyskotliwość', 10: 'Błyskotliwość',
    11: 'Błyskotliwość', 12: 'Charyzmatyczny', 13: 'Charyzmatyczny', 14: 'Charyzmatyczny',
    15: 'Chodu!', 16: 'Chodu!', 17: 'Chodu!', 18: 'Czujny', 19: 'Czujny', 20: 'Czujny',
    21: 'Czysta Dusza', 22: 'Czysta Dusza', 23: 'Czysta Dusza', 24: 'Czysta Dusza', 25: 'Czytanie/Pisanie',
    26: 'Czytanie/Pisanie', 27: 'Czytanie/Pisanie', 28: 'Geniusz Arytmetyczny', 29: 'Geniusz Arytmetyczny',
    30: 'Geniusz Arytmetyczny', 31: 'Geniusz Arytmetyczny', 32: 'Naśladowca', 33: 'Naśladowca',
    34: 'Naśladowca', 35: 'Niezwykle Odporny', 36: 'Niezwykle Odporny', 37: 'Niezwykle Odporny',
    38: 'Oburęczność', 39: 'Oburęczność', 40: 'Oburęczność', 41: 'Odporny na (Dowolne Zagrożenie)',
    42: 'Odporny na (Dowolne Zagrożenie)', 43: 'Odporny na (Dowolne Zagrożenie)', 44: 'Poliglota',
    45: 'Poliglota', 46: 'Poliglota', 47: 'Posłuch u Zwierząt', 48: 'Posłuch u Zwierząt',
    49: 'Posłuch u Zwierząt', 50: 'Silne Nogi', 51: 'Silne Nogi', 52: 'Silne Nogi', 53: 'Słuch Absolutny',
    54: 'Słuch Absolutny', 55: 'Słuch Absolutny', 56: 'Strzelec Wyborowy', 57: 'Strzelec Wyborowy',
    58: 'Strzelec Wyborowy', 59: 'Szczęście', 60: 'Szczęście', 61: 'Szczęście', 62: 'Szczęście',
    63: 'Szósty Zmysł', 64: 'Szósty Zmysł', 65: 'Szósty Zmysł', 66: 'Szósty Zmysł', 67: 'Szybki Refleks',
    68: 'Szybki Refleks', 69: 'Szybki Refleks', 70: 'Talent Artystyczny', 71: 'Talent Artystyczny',
    72: 'Talent Artystyczny', 73: 'Tragarz', 74: 'Tragarz', 75: 'Tragarz', 76: 'Twardziel',
    77: 'Twardziel', 78: 'Twardziel', 79: 'Twardziel', 80: 'Urodzony Wojownik', 81: 'Urodzony Wojownik',
    82: 'Urodzony Wojownik', 83: 'Widzenie w Ciemności', 84: 'Widzenie w Ciemności',
    85: 'Widzenie w Ciemności', 86: 'Wyczucie Kierunku', 87: 'Wyczucie Kierunku',
    88: 'Wyczucie Kierunku', 89: 'Wyczulony Zmysł (Dowolny)', 90: 'Wyczulony Zmysł (Dowolny)',
    91: 'Wyczulony Zmysł (Dowolny)', 92: 'Wytwórca (Dowolny)', 93: 'Wytwórca (Dowolny)',
    94: 'Wytwórca (Dowolny)', 95: 'Zimna Krew', 96: 'Zimna Krew', 97: 'Zimna Krew', 98: 'Zręczny',
    99: 'Zręczny', 100: 'Zręczny'
    }
    def __init__(self):
        self.talents = []

    # talenty losowe od rasy. ważne, funkcja usuwa liczbę losowalnych talentów z listy
    def draw_random_talents(self, character):
        if  isinstance(character.race.talenty_z_liczba_losowych_lista_list[-1] ,int):
            while True:
                self.talents = []
                liczba = character.race.talenty_z_liczba_losowych_lista_list[-1]
                los = random.sample(range(1,101), liczba)
                for i in los:
                    self.talents.append(Talents.tabela_losowych_talentów[i])
                if len(self.talents) == len(set(self.talents)):
                    character.race.talenty_z_liczba_losowych_lista_list.pop()
                    break
    
    # talenty wybieralne od rasy
    def choosable_talents_from_race(self, character):
        lista = character.race.talenty_z_liczba_losowych_lista_list
        for el in lista:
            if isinstance(el, str):
                self.talents.append(el)

            if isinstance(el, list):
                while True:
                    user_input = input(f"Wybierz talent rasowy 1 - {el[0]}, 2 - {el[1]} (1/2)  ")
                    if user_input == "1":
                        self.talents.append(el[0])
                        break

                    if user_input == "2":
                        self.talents.append(el[1])
                        break
                    if user_input == "":
                        self.talents.append(el[random.randint(0,1)])
                        break
    
    #talenty od profesji
    def talents_from_profession(self, character):
        for key, value in character.profession.talenty_i_level_dict.items():
            character.profession.talenty_i_level_dict[key] = value + character.level
        for key, value in character.profession.talenty_i_level_dict.items():
            if value > 0:
                self.talents.append(key)
    
    def add_talents_to_character(self, character):
        character.talents = self.talents

                



