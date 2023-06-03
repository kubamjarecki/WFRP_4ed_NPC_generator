import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from classes.Gender import Gender



# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):

    @patch("classes.Gender.input")
    def test_Gender_ask_for_gender(self, mock_input):
        mock_input.return_value = ""
        gender = Gender()
        gender.ask_for_gender()
        self.assertEqual(gender.input, "Mężczyzna")
    
    def test_give_gender_to_character_from_input(self):
        character = MagicMock
        gender = Gender()
        gender.input = "Kobieta"
        gender.give_gender_to_character(character)
        self.assertEqual(character.gender, "Kobieta")