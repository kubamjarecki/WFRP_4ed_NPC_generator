class Name:
    def ask_for_name(self):
        imie_input = input("Wpisz imię postaci. Zostaw puste, jeśli ma być wylosowane ")
        if imie_input == "":
            self.name = None

        if imie_input != "":
            self.name = imie_input
    
    def name_to_character(self, character):
        if self.name == None:
            if character.gender == "Kobieta":
                character.name = character.race.losowe_imie_zenskie
            
            if character.gender == "Mężczyzna":
                character.name = character.race.losowe_imie_meskie
        
        if self.name != None:
            character.name = self.name
    
