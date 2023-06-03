import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from classes.Name import Name


# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    @patch("classes.Name.input")
    def test_ask_for_name_with_input(self, mock_input):
        imie = Name()
        mock_input.return_value = "Stefan"
        imie.ask_for_name()
        self.assertEqual(imie.name, "Stefan")

    @patch("classes.Name.input")
    def test_ask_for_name_without_input(self, mock_input):
        imie = Name()
        mock_input.return_value = ""
        imie.ask_for_name()
        self.assertEqual(imie.name, None)
    
    def test_name_to_character_typed(self):
        character = MagicMock
        name = Name()
        name.name = "Stefan"
        name.name_to_character(character)
        self.assertEqual(character.name, "Stefan")


    def test_name_to_character_random(self):
        character = MagicMock
        name = Name()
        character.race = MagicMock
        character.gender = "Mężczyzna"
        name.name = None
        character.race.losowe_imie_meskie = "Stefan"
        name.name_to_character(character)
        self.assertEqual(character.name, "Stefan")





    
    