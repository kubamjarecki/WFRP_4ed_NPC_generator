import unittest
import importlib
from unittest.mock import MagicMock
from unittest.mock import patch
from classes.ProfessionSeizure import ProfessionSeizure
from rasy.lesny_elf import profesje


# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    @patch("classes.ProfessionSeizure.input")
    def test_ask_for_professionSeizure_writes_input(self, mock_input):
        mock_input.return_value = "63"
        profesja = ProfessionSeizure()
        profesja.ask_for_profession()
        self.assertEqual(profesja.wybor_prof, "63")

    @patch("classes.ProfessionSeizure.input")
    def test_ask_for_professionSeizure_writes_None_if_no_input(self, mock_input):
        mock_input.return_value = ""
        profesja = ProfessionSeizure()
        profesja.ask_for_profession()
        self.assertEqual(profesja.wybor_prof, None)
    
    @patch("random.randint")
    def test_give_profession_name_random(self, mock_random):
        character = MagicMock
        character.race = MagicMock
        professor = ProfessionSeizure()
        mock_random.return_value = 1
        MagicMock.race.nazwa = "Leśny elf"
        MagicMock.race.tabela_losowania_profesji_slownik = profesje
        professor.wybor_prof = None
        professor.give_profession_name_from_input_or_random(character)
        self.assertEqual(professor.nazwa_profesji, "Czarodziej")

    def test_give_profession_name_input(self):
        character = MagicMock
        character.race = MagicMock
        professor = ProfessionSeizure()
        MagicMock.race.nazwa = "Leśny elf"
        MagicMock.race.tabela_losowania_profesji_slownik = profesje
        professor.wybor_prof = "6"
        professor.give_profession_name_from_input_or_random(character)
        self.assertEqual(professor.nazwa_profesji, "Czarodziej")

    def test_create_ProfessionTraits_object_and_add_to_character(self):
        character = MagicMock
        profesor = ProfessionSeizure()
        profesor.nazwa_profesji = "Aptekarz"
        profesor.create_ProfessionTraits_object_and_add_to_character(character)
        self.assertEqual(character.profession.klasa_str, "Uczeni")


        


