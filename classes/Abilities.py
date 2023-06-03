import random

class Abilities:
    def __init__(self):
        self.umiejki = None
        self.umiejki_dict = None
        self.umiejetnosci_od_profesji = None
        self.level = None
        self.race_abilities = {}
        self.profession_abilities = {}
        self.join_abilities = {}
    
    def import_abilities(self, character):
        self.umiejki = character.race.umiejętności_od_rasy_3_i_5_lista
        self.umiejki_dict = {}
        self.umiejetnosci_od_profesji = character.profession.umiejki_i_level_dict
        self.level = character.level

    def format_question_for_race_abilities(self):
        for idx, wart in enumerate(self.umiejki):
                self.umiejki_dict[idx] = wart

                self.umiejki_str = ""
                a = 1

                for key, value in self.umiejki_dict.items():
                    b = ""
                    c = len(value)
                    d = 30 - len(value) - len(str(key))

                    while d > 0:
                        b = b + " "
                        d = d - 1

                    if a % 4 != 0:
                        self.umiejki_str = self.umiejki_str + str(key)+ " - " + value + b
                        #print(self.umiejki_str)
                
                    if a % 4 == 0:
                        self.umiejki_str = self.umiejki_str + str(key)+ " - " + value + "\n"
                        #print(self.umiejki_str)
                    a = a + 1

    def ask_for_race_abilities(self):
        wybor_umiejek = input(f"Czy chcesz wybrać umiejętności rasowe?(t/n) ")
        if wybor_umiejek == "t":
            wh = 1
            while wh == 1:
                ilosc_umiejetnosci_do_wyboru = (len(self.umiejki)-1)
                zasieg_um = []
                for key, value in self.umiejki_dict.items():
                    zasieg_um.append(str(key))

                in_um5a = input(f"{self.umiejki_str} \n\nWybierz pierwszą umiejętność, która będzie na poziomie 5 (0-{ilosc_umiejetnosci_do_wyboru}) ")
                in_um5b = input(f"Wybierz drugą umiejętność, która będzie na poziomie 5 (0-{ilosc_umiejetnosci_do_wyboru}) ")
                in_um5c = input(f"Wybierz trzecią umiejętność, która będzie na poziomie 5 (0-{ilosc_umiejetnosci_do_wyboru}) ")
                in_um3a = input(f"Wybierz pierwszą umiejętność, która będzie na poziomie 3 (0-{ilosc_umiejetnosci_do_wyboru}) ")
                in_um3b = input(f"Wybierz drugą umiejętność, która będzie na poziomie 3 (0-{ilosc_umiejetnosci_do_wyboru}) ")
                in_um3c = input(f"Wybierz trzecią umiejętność, która będzie na poziomie 3 (0-{ilosc_umiejetnosci_do_wyboru}) ")
                umiejkix = {}

                if in_um5a in zasieg_um:
                    a = int(in_um5a)
                    if self.umiejki[a] not in umiejkix:
                        umiejkix[self.umiejki[a]] = 5
                if in_um5b in zasieg_um:
                    a = int(in_um5b)
                    if self.umiejki[a] not in umiejkix:
                        umiejkix[self.umiejki[a]] = 5
                if in_um5c in zasieg_um:
                    a = int(in_um5c)
                    if self.umiejki[a] not in umiejkix:
                        umiejkix[self.umiejki[a]] = 5
                if in_um3a in zasieg_um:
                    a = int(in_um3a)
                    if self.umiejki[a] not in umiejkix:
                        umiejkix[self.umiejki[a]] = 3
                if in_um3b in zasieg_um:
                    a = int(in_um3b)
                    if self.umiejki[a] not in umiejkix:
                        umiejkix[self.umiejki[a]] = 3
                if in_um3c in zasieg_um:
                    a = int(in_um3c)
                    if self.umiejki[a] not in umiejkix:
                        umiejkix[self.umiejki[a]] = 3
                if len(umiejkix) == 6:
                    wh = 2
                    str_umtnsc = ""
                    for key, value in umiejkix.items():
                        str_umtnsc = str_umtnsc + key + " - "+ str(value) + "\n"
                    
                    #print (f"Wybrane umiejętności to \n{str_umtnsc}")
                if len(umiejkix) != 6:
                    
                    print(f"Coś zjebałeś. Spróbuj jeszcze raz. Pamiętaj że musisz wybrać liczbę z przedziału 0 - {ilosc_umiejetnosci_do_wyboru}, oraz że nie możesz dwa razy wybrać tej samej umiejętności")
            
            self.race_abilities=umiejkix

    def write_random_race_abilities(self):
        if self.race_abilities == {}:
       
            los = random.sample(range(0,len(self.umiejki)),6)
            a=0
            for el in los:
                if a<3:
                    self.race_abilities[self.umiejki[el]] = 5
                    a = a + 1
                else:
                    self.race_abilities[self.umiejki[el]] = 3


    def write_profession_abilities(self, character):
        for key, value in character.profession.umiejki_i_level_dict.items():
            new_value = value + character.level 
            character.profession.umiejki_i_level_dict[key] = new_value
            if new_value > 0:
                self.profession_abilities[key] = new_value*5
        

    def join_race_and_profession_abilities(self):
        for key, value in self.profession_abilities.items():
            if key in self.race_abilities.keys():
                self.join_abilities[key] = (value + self.race_abilities[key])
            
            if key not in self.race_abilities.keys():
                self.join_abilities[key] = value
        
        for key, value in self.race_abilities.items():
            if key not in self.join_abilities.keys():
                self.join_abilities[key] = value

    def give_profession_abilities_to_character(self,character):
        character.abilities = self.join_abilities
    

         
