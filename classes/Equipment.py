import random

class Equipment:
    def unpack_eq(self, character):
        a = 0
        character.equipment = []
        while a <= character.level:
        
            for el in character.profession.wyposazenie_list_of_lists[a]:
                character.equipment.append(el)
        
            a = a + 1
    def create_gold_str_and_append_to_character_equipment(self,character):
        status = character.miss.miss['Status']
        if status == "Złoto":
            majatek = "1 ZK"
        if status == "Srebro":
            a = random.randint(1, 10)
            majatek = f"{a} SS"
        if status == "Brąz":
            a = random.randint(2, 20)
            majatek = f"{a} BP"
        character.equipment.append(majatek)

