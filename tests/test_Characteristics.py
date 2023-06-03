import unittest
from unittest.mock import patch, MagicMock

from classes.Characteristics import Characteristics
from classes.Character import Character



# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    @patch("builtins.input", side_effect=["t","13","14","15","1", "kiełbassa", "16", "17", "18", "19", "20","2", "2", "1"])
    def test_ask_for_characteristics(self, mock_input):
        characteristics = Characteristics()
        characteristics.ask_for_characteristics()
        self.assertEqual(characteristics.characteristics, {"WW" : "13","US" : "14", "S" : "15","Wt" : "16","I" : "17","Zw" : "18","Zr" : "19","Int" : "20","SW" : "2","Ogd" : "2"})

    @patch("random.randint")
    def test_draw_random_characteristics(self, mock_random):
        mock_random.return_value = 10
        character = Character()
        character.profession = MagicMock
        character.profession.waga_list = ["Ogd", "US", "Int", "Zw", "WW", "SW", "Wt", "I", "S", "Zr", ]
        characteristics = Characteristics()
        characteristics.draw_random_characteristics(character)
        self.assertEqual(characteristics.characteristics, {"WW" : 20,"US" : 20, "S" : 20,"Wt" : 20,"I" : 20,"Zw" : 20,"Zr" : 20,"Int" : 20,"SW" : 20,"Ogd" : 20})

    def test_raise_characteristics_with_talents(self):
        characteristics = Characteristics()
        character = Character()
        character.talents = ["Zręczny"]
        characteristics.characteristics = {"WW" : 20,"US" : 20, "S" : 20,"Wt" : 20,"I" : 20,"Zw" : 20,"Zr" : 20,"Int" : 20,"SW" : 20,"Ogd" : 20}
        characteristics.raise_characteristics_with_talents(character)
        self.assertEqual(characteristics.characteristics, {"WW" : 20,"US" : 20, "S" : 20,"Wt" : 20,"I" : 20,"Zw" : 20,"Zr" : 25,"Int" : 20,"SW" : 20,"Ogd" : 20})

    def test_raise_characteristics_with_race(self):
        characteristics = Characteristics()
        character = Character()
        character.race = MagicMock
        character.race.cechy_bez_rzutów_slownik = {"WW" : 30,"US" : 30, "S" : 30,"Wt" : 30,"I" : 30,"Zw" : 30,"Zr" : 30,"Int" : 30,"SW" : 30,"Ogd" : 30}
        characteristics.characteristics = {"WW" : 13,"US" : 13, "S" : 13,"Wt" : 13,"I" : 13,"Zw" : 13,"Zr" : 13,"Int" : 13,"SW" : 13,"Ogd" : 13}
        characteristics.raise_characteristics_with_race(character)
        self.assertEqual(characteristics.characteristics, {"WW" : 43,"US" : 43, "S" : 43,"Wt" : 43,"I" : 43,"Zw" : 43,"Zr" : 43,"Int" : 43,"SW" : 43,"Ogd" : 43})

    def test_raise_characteristics_with_profession(self):
        characteristics = Characteristics()
        characteristics.characteristics = {"WW" : 30,"US" : 30, "S" : 30,"Wt" : 30,"I" : 30,"Zw" : 30,"Zr" : 30,"Int" : 30,"SW" : 30,"Ogd" : 30}
        character = Character()
        character.profession = MagicMock
        character.profession.rozwiniecia_cech_dict = rozwiniecia_cech = {"Int": 0,"Ogd": 0,"US" : 0,"Zw" : -1,"WW" : -2,"I" : -3}
        character.level = 4
        characteristics.raise_characteristics_with_profession(character)
        self.assertEqual(characteristics.characteristics2, {"WW" : 40,"US" : 50, "S" : None,"Wt" : None,"I" : 35,"Zw" : 45,"Zr" : None,"Int" : 50,"SW" : None,"Ogd" : 50})
    

    def test_give_characteristics_to_character(self):
        characteristics = Characteristics()
        character = Character()
        characteristics.characteristics = {"WW" : 30,"US" : 30, "S" : 30,"Wt" : 30,"I" : 30,"Zw" : 30,"Zr" : 30,"Int" : 30,"SW" : 30,"Ogd" : 30}
        characteristics.characteristics2 = {"WW" : 40,"US" : 50, "S" : None,"Wt" : None,"I" : 35,"Zw" : 45,"Zr" : None,"Int" : 50,"SW" : None,"Ogd" : 50}
        characteristics.give_characteristics_to_character(character)
        # self.assertIn({"WW" : 30,"US" : 30, "S" : 30,"Wt" : 30,"I" : 30,"Zw" : 30,"Zr" : 30,"Int" : 30,"SW" : 30,"Ogd" : 30}, character.characteristics)
        # self.assertIn({"WW" : 40,"US" : 50, "S" : 30,"Wt" : 30,"I" : 35,"Zw" : 45,"Zr" : 30,"Int" : 50,"SW" : 30,"Ogd" : 50}, character.characteristics)
        self.assertEqual(character.characteristics[0],{"WW" : 30,"US" : 30, "S" : 30,"Wt" : 30,"I" : 30,"Zw" : 30,"Zr" : 30,"Int" : 30,"SW" : 30,"Ogd" : 30})
        self.assertEqual(character.characteristics[1],{"WW" : 40,"US" : 50, "S" : 30,"Wt" : 30,"I" : 35,"Zw" : 45,"Zr" : 30,"Int" : 50,"SW" : 30,"Ogd" : 50})

    