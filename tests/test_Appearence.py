import unittest
from unittest.mock import patch, MagicMock
from classes.Appearence import Appearence

# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):

    @patch('classes.Appearence.input')
    def test_ask_about_app(self, mock_input):
        app = Appearence()
        mock_input.return_value = ""
        app.ask_about_app()
        self.assertEqual(app.eager, False)

    @patch("random.randint")
    def test_random_get_hair(self, mock_random):
        mock_random.return_value = 1
        character = MagicMock()
        character.race = MagicMock()
        character.race.slownik_do_losowania_wlosow =  { 1: 'Biały', 2: 'Złoty blond', 3: 'Rudoblond', 4: 'Złoty', 5: 'Złoty', 6: 'Złoty', 7: 'Jasny brąz', 8: 'Jasny brąz', 9: 'Jasny brąz', 10: 'Kasztanowy', 11: 'Ciemny brąz', 12: 'Ciemny brąz', 13: 'Ciemny brąz', 14: 'Czarny', 15: 'Czarny', 16: 'Czarny', 17: 'Kasztanowy', 18: 'Rudy', 19: 'Siwy'}
        app = Appearence()
        app.eager = False
        app.get_hair(character)
        self.assertEqual(app.hair, 'Biały')

    @patch("classes.Appearence.input")
    def test_input_get_hair(self, mock_input):
        mock_input.return_value = "4"
        character = MagicMock()
        character.race = MagicMock()
        character.race.slownik_do_losowania_wlosow =  { 1: 'Biały', 2: 'Złoty blond', 3: 'Rudoblond', 4: 'Złoty', 5: 'Złoty', 6: 'Złoty', 7: 'Jasny brąz', 8: 'Jasny brąz', 9: 'Jasny brąz', 10: 'Kasztanowy', 11: 'Ciemny brąz', 12: 'Ciemny brąz', 13: 'Ciemny brąz', 14: 'Czarny', 15: 'Czarny', 16: 'Czarny', 17: 'Kasztanowy', 18: 'Rudy', 19: 'Siwy'}
        app = Appearence()
        app.eager = True
        app.get_hair(character)
        self.assertEqual(app.hair, 'Złoty')


    @patch("random.randint")
    def test_random_get_eyes(self, mock_random):
        mock_random.return_value = 1
        character = MagicMock()
        character.race = MagicMock()
        character.race.slownik_do_losowania_oczu =  {1: 'Zielony', 2: 'Błękitny', 3: 'Niebieski', 4: 'Niebieski', 5: 'Niebieski', 6: 'Blady szary', 7: 'Blady szary', 8: 'Blady szary', 9: 'Blady szary', 10: 'Szary', 11: 'Szary', 12: 'Szary', 13: 'Brązowy', 14: 'Brązowy', 15: 'Brązowy', 16: 'Orzechowy', 17: 'Ciemnobrązowy', 18: 'Czarny', 19: 'Czarny'}
        app = Appearence()
        app.eager = False
        app.get_eyes(character)
        self.assertEqual(app.eyes, 'Zielony')

    @patch("classes.Appearence.input")
    def test_input_get_eyes(self, mock_input):
        mock_input.return_value = "4"
        character = MagicMock()
        character.race = MagicMock()
        character.race.slownik_do_losowania_oczu =  {1: 'Zielony', 2: 'Błękitny', 3: 'Niebieski', 4: 'Niebieski', 5: 'Niebieski', 6: 'Blady szary', 7: 'Blady szary', 8: 'Blady szary', 9: 'Blady szary', 10: 'Szary', 11: 'Szary', 12: 'Szary', 13: 'Brązowy', 14: 'Brązowy', 15: 'Brązowy', 16: 'Orzechowy', 17: 'Ciemnobrązowy', 18: 'Czarny', 19: 'Czarny'}
        app = Appearence()
        app.eager = True
        app.get_eyes(character)
        self.assertEqual(app.eyes, 'Blady szary')

    @patch("classes.Appearence.input")
    def test_input_height(self, mock_input):
        mock_input.return_value = 156
        app = Appearence()
        character = MagicMock()
        character.race = MagicMock()
        character.race.wzrost_bazowe_i_liczba_K10 = [150, 4]
        app.eager = True
        app.get_height(character)
        self.assertEqual(app.height, 156)

    @patch("random.randint")
    def test_random_height(self, mock_random):
        mock_random.return_value = 2
        app = Appearence()
        character = MagicMock()
        character.race = MagicMock()
        character.race.wzrost_bazowe_i_liczba_K10 = [150, 4]
        app.eager = False
        app.get_height(character)
        self.assertEqual(app.height, 158)