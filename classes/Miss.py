import random

class Miss:
    #punkty bohatera, Punkty przeznaczenia, status
    def __init__(self):
        self.miss = {'PB': None, "PP": None, "Status": None, "Żyw": None, "SZ": None}

    def add_miss_to_character(self, character):
        character.miss = self
        
    def get_PP_and_PB(self, character):
        cab = character.race.punkty_do_rozdania
        zasieg =[]
        while cab >= 0:
            zasieg.append(str(cab))
            cab = cab - 1
        while True:
            input_pp = input(f"Twoja rasa startowo posiada początkowo {character.race.pb_poczatkowe} punków bohatera, oraz {character.race.pp_poczatkowe_int} punktów przeznaczenia, oraz {character.race.punkty_do_rozdania} punktów do rozdania. Ile z nich chciałbyś przeznaczyć na punkty przeznaczenia? (0-{character.race.punkty_do_rozdania}) \nZostaw puste, jeśli mają byc losowane " )
            if input_pp in zasieg:
                self.miss["PB"] = character.race.pb_poczatkowe + int(input_pp)
                character.race.punkty_do_rozdania = character.race.punkty_do_rozdania - int(input_pp)
                self.miss["PP"] = character.race.pp_poczatkowe_int + character.race.punkty_do_rozdania
                break

            if input_pp == "":
                a = random.randint(0, character.race.punkty_do_rozdania)
                self.miss["PB"] = character.race.pb_poczatkowe + a
                b = character.race.punkty_do_rozdania - a
                self.miss["PP"] = character.race.pp_poczatkowe_int + b
                break

    def get_status(self, character):
        self.miss["Status"] = character.profession.status_dict[character.level]

    def get_HP(self, character):

        s_b = int((character.characteristics[1]["S"]) / 10)
        wt_b = int((character.characteristics[1]["Wt"]) / 10)
        sw_b = int((character.characteristics[1]["SW"]) / 10)
        

        if character.race.nazwa == "Niziołek":
            self.miss['Żyw'] = 2 * wt_b + sw_b
        if character.race.nazwa != "Niziołek":
            self.miss['Żyw'] = s_b + (2 * wt_b) + sw_b
        if "Twardziel" in character.talents:
            self.miss['Żyw'] = self.miss['Żyw'] + wt_b

    def get_speed(self, character):
        self.miss["SZ"] = character.race.sz_od_rasy
