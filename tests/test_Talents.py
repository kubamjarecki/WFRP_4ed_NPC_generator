import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from classes.Talents import Talents

class Test(unittest.TestCase):
    def test_create_list(self):
        talents = Talents()
        self.assertIsInstance(talents.talents, list)
    

    def test_draw_random_talents(self):
        talents = Talents()
        character = MagicMock
        character.race = MagicMock
        character.race.talenty_z_liczba_losowych_lista_list = ["dupa", "dupa2", 10]
        talents.draw_random_talents(character)
        self.assertEqual(len(talents.talents), 10)
        self.assertEqual(len(talents.talents), len(set(talents.talents)))
        self.assertEqual(character.race.talenty_z_liczba_losowych_lista_list, ["dupa", "dupa2"] )
    

    def test_draw_random_talents_with_no_number(self):
        talents = Talents()
        character = MagicMock
        character.race = MagicMock
        character.race.talenty_z_liczba_losowych_lista_list = ["dupa", "dupa2"]
        talents.draw_random_talents(character)
        self.assertEqual(talents.talents, [])
    
    @patch('classes.Talents.input')
    def test_choosable_talents_from_race(self, mock_input):
        mock_input.return_value = "1"
        talents = Talents()
        character = MagicMock
        character.race = MagicMock
        dupa =["stek", "kiełbasa"]
        dupa2 = ["ziemniaczki", "surówka"]
        dupa3 = ["shake", "lody"]
        character.race.talenty_z_liczba_losowych_lista_list = [dupa, dupa2, dupa3,"q", "dupa3", "dupa4", 1]
        talents.draw_random_talents(character)
        talents.choosable_talents_from_race(character)
        self.assertIn("stek", talents.talents)
        self.assertIn("ziemniaczki", talents.talents)
        self.assertIn("shake", talents.talents)
        self.assertIn("q", talents.talents)
        self.assertIn("dupa3", talents.talents)
        self.assertIn("dupa4", talents.talents)

    def test_choosable_talents_from_race_with_no_list(self):
        talents = Talents()
        character = MagicMock
        character.race = MagicMock
        character.race.talenty_z_liczba_losowych_lista_list = ["dupa", "dupa2"]
        talents.draw_random_talents(character)
        self.assertEqual(talents.talents, [])
    
    def test_talents_from_profession(self):
        talents = Talents()
        character = MagicMock
        character.profession = MagicMock
        character.profession.talenty_i_level_dict = {'Naciągacz': 1, 'Czytanie/Pisanie': 0, 'Gadanina': 0, 'Towarzyski': 0, 'Mówca': -1, 'Porywająca Gorliwość': -1, 'Przekonujący': -1, 'Ulicznik': -1, 'Chodu!': -2, 'Cios Poniżej Pasa': -2, 'Gładkie Słówka': -2, 'Zejście z Linii': -2, 'Charyzmatyczny': -3, 'Etykieta (Dowolna Grupa)': -3, 'Intrygant': -3, 'Krasomówstwo': -3}
        character.level = 2
        talents.talents_from_profession(character)
        self.assertEqual(talents.talents, [ 'Naciągacz', 'Czytanie/Pisanie', 'Gadanina', 'Towarzyski', 'Mówca', 'Porywająca Gorliwość', 'Przekonujący', 'Ulicznik'])

        