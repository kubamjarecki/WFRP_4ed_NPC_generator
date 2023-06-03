class Gender:
    
    def ask_for_gender(self):
        name_input = input("Wybierz płeć postaci(K/M) ")
        if name_input == "K":
            self.input = "Kobieta"
        else:
            self.input = "Mężczyzna"
    
    def give_gender_to_character(self, character):
        character.gender = self.input