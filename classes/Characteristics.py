import random

class Characteristics:
    def __init__(self):
        self.characteristics = {"WW" : None,"US" : None, "S" : None,"Wt" : None,"I" : None,"Zw" : None,"Zr" : None,"Int" : None,"SW" : None,"Ogd" : None}
        self.characteristics2 = {"WW" : None,"US" : None, "S" : None,"Wt" : None,"I" : None,"Zw" : None,"Zr" : None,"Int" : None,"SW" : None,"Ogd" : None}
    
    def ask_for_characteristics(self):
        while True:
            eager = input("Czy chcesz wpisać własne rzuty na cechy(t/n) ")
            if eager == "t" or eager == "T":
                zasieg = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
                
                for key in self.characteristics:
                        while True:
                            char_input = input(f"Podaj wartość cechy {key}: ")
                            if char_input in zasieg:
                                self.characteristics[key] = char_input
                                break
                        
                break

                
                
            if eager == "n" or eager == "N" or eager == "":  
                 break

    def draw_random_characteristics(self, character):
        if self.characteristics["WW"] == None:
            waga = character.profession.waga_list
            rzuty = []
            a = 10
            while a>0:
                b = random.randint(1,10) + random.randint(1,10) 
                rzuty.append(b)
                a = a -1
                
                
            slownik_cech_i_rzutow_w_kolejnosci_wagi = {}
            rzuty.sort()
            rzuty.reverse()
            #print (rzuty)
            a = 0
            while a<10:
                slownik_cech_i_rzutow_w_kolejnosci_wagi[waga[a]]=rzuty[a]
                a = a + 1

            self.characteristics = slownik_cech_i_rzutow_w_kolejnosci_wagi
            self.dobroc = 0
            for key, value in self.characteristics.items():
                self.dobroc = self.dobroc + int(value)


    def raise_characteristics_with_talents(self, character):
        if "Urodzony Wojownik" in character.talents:
            self.characteristics["WW"] = self.characteristics["WW"] + 5
        if "Charyzmatyczny" in character.talents:
            self.characteristics["Ogd"] = self.characteristics["Ogd"] + 5
        if "Błyskotliwość" in character.talents:
            self.characteristics["Int"] = self.characteristics["Int"] + 5
        if "Bardzo silny" in character.talents:
            self.characteristics["S"] = self.characteristics["S"] + 5
        if "Niezwykle Odporny" in character.talents:
            self.characteristics["Wt"] = self.characteristics["Wt"] + 5
        if "Strzelec Wyborowy" in character.talents:
            self.characteristics["US"] = self.characteristics["US"] + 5
        if "Szybki Refleks" in character.talents:
            self.characteristics["Zw"] = self.characteristics["Zw"] + 5
        if "Zimna Krew" in character.talents:
            self.characteristics["SW"] = self.characteristics["SW"] + 5
        if "Zręczny" in character.talents:
            self.characteristics["Zr"] = self.characteristics["Zr"] + 5
        if "Czujny" in character.talents:
            self.characteristics["I"] = self.characteristics["I"] + 5
    
    def raise_characteristics_with_race(self, character):
        for key, value in self.characteristics.items():
            self.characteristics[key] = self.characteristics[key] + character.race.cechy_bez_rzutów_slownik[key]

    def raise_characteristics_with_profession(self, character):
        for key, value in character.profession.rozwiniecia_cech_dict.items():
            character.profession.rozwiniecia_cech_dict[key] = character.profession.rozwiniecia_cech_dict[key] + character.level
            if character.profession.rozwiniecia_cech_dict[key] > 0:
                self.characteristics2[key] = self.characteristics[key] + (character.profession.rozwiniecia_cech_dict[key] * 5)
    
    def give_characteristics_to_character(self, character):
        characteristic_with_no_None = {}
        for key, value in self.characteristics2.items():
            if value != None:
                characteristic_with_no_None[key] = self.characteristics2[key]
            
            if value == None:
                characteristic_with_no_None[key] = self.characteristics[key]
            

        character.characteristics = [self.characteristics, characteristic_with_no_None]