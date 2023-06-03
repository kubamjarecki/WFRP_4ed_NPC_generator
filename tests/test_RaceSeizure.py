import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from classes.Character import Character
from classes.RaceSeizure import RaceSeizure
from classes.RaceTraits import RaceTraits

# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    def test_if_RaceSeizure_know_tabela_ras(self):
        rasa = RaceSeizure()
        self.assertEqual(rasa.tabela_ras, {
    1: "Leśny elf", 2: "Wysoki elf", 3: "Krasnolud", 4: "Niziołek", 5: "Człowiek"
    })
        
    def test_does_function_for_creating_string_works(self):
        rasa = RaceSeizure()
        rasa.formatowanie_wyswietlania_tablicy_ras(rasa.tabela_ras)
        #print(rasa.rasy_str)
        self.assertIn("Wysoki elf", rasa.rasy_str)
        #print(rasa.rasy_str)
    
    @patch("classes.RaceSeizure.input")
    def test_ask_for_race_write_input_in(self, mock_input):
        mock_input.return_value ="1"
        rasa = RaceSeizure()
        rasa.ask_for_race()
        self.assertEqual(rasa.input_rasa, "1")
    
    @patch("classes.RaceSeizure.input")
    def test_ask_for_race_write_input_in2(self, mock_input):
        mock_input.return_value =""
        rasa = RaceSeizure()
        rasa.ask_for_race()
        self.assertEqual(rasa.input_rasa, None)
    
    def test_give_race_give_inputed_race(self):
        rasa = RaceSeizure()
        postac = Character()
        rasa.input_rasa = "1"
        rasa.give_race(postac)
        self.assertEqual(postac.race.nazwa, "Leśny elf")
        self.assertIs(type(postac.race), RaceTraits)

    @patch("random.randint")
    def test_give_race_random_race_high_elf(self, mock_random):
        mock_random.return_value = 99
        rasa = RaceSeizure()
        postac = Character()
        rasa.input_rasa = None
        rasa.give_race(postac)
        self.assertEqual(postac.race.nazwa, "Wysoki elf")
        self.assertEqual(postac.race.sz_od_rasy, 4)
        self.assertIs(type(postac.race), RaceTraits)
    
    @patch("random.randint")
    def test_give_race_random_race_wood_elf(self, mock_random):
        mock_random.return_value = 100
        rasa = RaceSeizure()
        postac = Character()
        rasa.input_rasa = None
        rasa.give_race(postac)
        self.assertEqual(postac.race.nazwa, "Leśny elf")
        self.assertIs(type(postac.race), RaceTraits)

    @patch("random.randint")
    def test_give_race_random_race_dwarf(self, mock_random):
        mock_random.return_value = 98
        rasa = RaceSeizure()
        postac = Character()
        rasa.input_rasa = None
        rasa.give_race(postac)
        self.assertEqual(postac.race.nazwa, "Krasnolud")
        self.assertIs(type(postac.race), RaceTraits)
    
    @patch("random.randint")
    def test_give_race_random_race_hobbit(self, mock_random):
        mock_random.return_value = 91
        rasa = RaceSeizure()
        postac = Character()
        rasa.input_rasa = None
        rasa.give_race(postac)
        self.assertEqual(postac.race.nazwa, "Niziołek")
        self.assertIs(type(postac.race), RaceTraits)

    @patch("random.randint")
    def test_give_race_random_race_man(self, mock_random):
        mock_random.return_value = 90
        rasa = RaceSeizure()
        postac = Character()
        rasa.input_rasa = None
        rasa.give_race(postac)
        self.assertEqual(postac.race.nazwa, "Człowiek")
        self.assertIs(type(postac.race), RaceTraits)
    

    #def test_RaceTraits_class_creation(self):
        
        
