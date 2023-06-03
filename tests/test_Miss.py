import unittest
from unittest.mock import patch, MagicMock

from classes.Miss import Miss
from classes.Character import Character



# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    @patch("classes.Miss.input")
    def test_get_PP_and_PB_from_input(self, mock_input):
        mock_input.return_value = "1"
        miss = Miss()
        character = MagicMock()
        character.race = MagicMock()
        character.race.pp_poczatkowe_int = 3
        character.race.pb_poczatkowe = 2
        character.race.punkty_do_rozdania = 2
        miss.get_PP_and_PB(character)
        self.assertEqual(miss.miss['PB'], 3)
        self.assertEqual(miss.miss['PP'], 4)
        
    @patch("classes.Miss.input")
    def test_get_PP_random(self, mock_input):
        mock_input.return_value = ""
        miss = Miss()
        character = MagicMock()
        character.race = MagicMock()
        character.race.pp_poczatkowe_int = 3
        character.race.pb_poczatkowe = 2
        character.race.punkty_do_rozdania = 2
        miss.get_PP_and_PB(character)
        self.assertEqual(type(miss.miss['PB']), int)
        self.assertEqual(type(miss.miss['PP']), int)

    def test_get_status(self):
        miss = Miss()
        character = MagicMock()
        character.profession = MagicMock()
        character.profession.status_dict = {0 : "Brąz",1 : "Dupa ",2 : "Chuj", 3 : "Kiełbasa",4 : "Ziemniaczki"}
        character.level = 3
        miss.get_status(character)
        self.assertEqual(miss.miss['Status'], "Kiełbasa")
        
    def test_get_HP(self):
        miss = Miss()
        character = MagicMock()
        character.characteristics = [MagicMock, {"WW" : 43,"US" : 43, "S" : 43,"Wt" : 43,"I" : 43,"Zw" : 43,"Zr" : 43,"Int" : 43,"SW" : 43,"Ogd" : 43}]
        character.race = MagicMock()
        character.race.nazwa = "Krasnolud"
        character.talents = ["Twardziel"]
        miss.get_HP(character)
        self.assertEqual(miss.miss['Żyw'], 20)

    def test_get_speed(self):
        miss = Miss()
        character = MagicMock()
        character.race = MagicMock()
        character.race.sz_od_rasy = 13
        miss.get_speed(character)
        self.assertEqual(miss.miss["SZ"], 13 )