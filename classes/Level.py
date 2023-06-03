
class Level:
    def ask_for_level_and_give(self,character):
        while True:
            user_input= input(f"Na którym poziomie ma być postać(0-4) ")
            zasieg = ["0", "1", "2", "3", "4"]
            if user_input in zasieg:
                character.level = int(user_input)
                break
            if user_input == "":
                character.level = 0
                break