import unittest
from unittest.mock import patch, MagicMock

from classes.Equipment import Equipment
from classes.Character import Character

# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    def test_unpack_eq(self):
        character = MagicMock()
        eq = Equipment()
        wyp0 = ["Broń Biała (WW)", "sakwa", "sztylet", "ubranie"]
        wyp1 = ["młotek i gwoździe", "plik ulotek", "zestaw do pisania"]
        wyp2 = ["skórzana kurta"]
        wyp3 = ["broń ręczna", "pomocny Pamflecista"]
        wyp4 = ["imponujący kapelusz", "Patron", "prasa drukarska", "3 Pamflecistów"]
        wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]
        character.profession = MagicMock()
        character.profession.wyposazenie_list_of_lists = wyp
        character.level = 3
        eq.unpack_eq(character)
        self.assertEqual(character.equipment, ["Broń Biała (WW)", "sakwa", "sztylet", "ubranie", "młotek i gwoździe", "plik ulotek", "zestaw do pisania", "skórzana kurta", "broń ręczna", "pomocny Pamflecista"] )

    def test_create_gold_str_and_append_to_character_equipment(self):
        character = MagicMock()
        eq = Equipment()
        character.miss = MagicMock()
        character.miss.miss = {"Status":"Złoto"}
        character.equipment = []
        eq.create_gold_str_and_append_to_character_equipment(character)
        self.assertEqual(character.equipment, ["1 ZK"])