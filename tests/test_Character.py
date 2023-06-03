import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from classes.Character import Character

# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    def test_character_has_all_atributes_equal_to_None_at_start(self):
        character = Character()
        #self.assertEqual(character.name, None)
        self.assertEqual(character.profession, None)
        self.assertEqual(character.race, None)
        self.assertEqual(character.gender, None)
        self.assertEqual(character.level, None)
        self.assertEqual(character.characteristics, None)
        self.assertEqual(character.abilities, None)
        self.assertEqual(character.talents, None)
        self.assertEqual(character.appearance, None)
        self.assertEqual(character.miss, None)
        self.assertEqual(character.equipment, None)