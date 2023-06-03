import unittest
from unittest.mock import patch
from unittest.mock import MagicMock, Mock
from classes.Abilities  import Abilities


class Test(unittest.TestCase):

    def test_import_abilities(self):
        abilities = Abilities()
        character = MagicMock()
        character.race = MagicMock
        character.profession = MagicMock
        character.race.umiejętności_od_rasy_3_i_5_lista = 1
        character.profession.umiejki_i_level_dict = 3
        character.level = 4
        abilities.import_abilities(character)
        self.assertEqual(abilities.umiejki, 1)
        self.assertEqual(abilities.umiejki_dict, {})
        self.assertEqual(abilities.umiejetnosci_od_profesji, 3)
        self.assertEqual(abilities.race_abilities, {})
        self.assertEqual(abilities.level, 4)



    @patch("builtins.input", side_effect=["t","1","2","3", "4", "5", "6"])
    def test_ask_for_race_abilities(self, mock_input):
        character = MagicMock()
        abilities = Abilities()
        character.race = MagicMock
        character.race.umiejętności_od_rasy_3_i_5_lista = ["Charyzma (Ogd) ", "Hazard (Int)", "Intuicja (I)", "Język (Int) (Krainy Zgromadzenia)", "Mocna Głowa (Wt)", "Percepcja (I)", "Rzemiosło (Zr) (Kucharz)", "Skradanie (Zw) (Dowolne)", "Targowanie (Ogd)", "Unik (Zw)", "Wiedza (Int) (Reikland)", "Zwinne Palce (Zr)"]
        abilities.import_abilities(character)
        abilities.format_question_for_race_abilities()
        abilities.ask_for_race_abilities()
        self.assertEqual(abilities.race_abilities, {'Hazard (Int)': 5, 'Intuicja (I)': 5, 'Język (Int) (Krainy Zgromadzenia)': 5, 'Mocna Głowa (Wt)': 3, 'Percepcja (I)': 3, 'Rzemiosło (Zr) (Kucharz)': 3})
    
    @patch("random.sample")
    def test_write_random_race_abilities(self, mock_sample):
        abiilities = Abilities()
        abiilities.race_abilities = {}
        mock_sample.return_value = [0,1,2,3,4,5]
        abiilities.umiejki = ["Charyzma (Ogd) ", "Hazard (Int)", "Intuicja (I)", "Język (Int) (Krainy Zgromadzenia)", "Mocna Głowa (Wt)", "Percepcja (I)", "Rzemiosło (Zr) (Kucharz)", "Skradanie (Zw) (Dowolne)", "Targowanie (Ogd)", "Unik (Zw)", "Wiedza (Int) (Reikland)", "Zwinne Palce (Zr)"]
        abiilities.write_random_race_abilities()
        self.assertEqual(len(abiilities.race_abilities), 6)
    


    def test_write_profession_abilities(self):
        character = MagicMock()
        abilities = Abilities()
        character.profession = MagicMock
        character.profession.umiejki_i_level_dict = {'Charyzma (Ogd) ': 1, 'Mocna Głowa (Wt)': 1, 'Plotkowanie (Ogd)': 1, 'Przekupstwo (Ogd)': 1, 'Rzemiosło (Zr) (Drukarstwo)': 1, 'Sztuka (Zr) (Pisarstwo)': 1, 'Targowanie (Ogd)': 1, 'Wiedza (Int) (Polityka)': 1, 'Dowodzenie (Ogd)': 0, 'Hazard (Int)': 0, 'Intuicja (I)': 0, 'Opanowanie (SW)': 0, 'Unik (Zw)': 0, 'Występy (Ogd) (Gawędziarstwo)': 0, 'Atletyka (Zw)': -1, 'Broń Biała (WW) (Bijatyka)': -1, 'Percepcja (I)': -1, 'Zastraszanie (S)': -1, 'Jeździectwo (Zw)  (Konie)': -2, 'Wiedza (Int) (Heraldyka)': -2}
        character.level = 3
        abilities.write_profession_abilities(character)
        self.assertEqual(abilities.profession_abilities['Charyzma (Ogd) '],  20) 
        self.assertEqual(abilities.profession_abilities['Zastraszanie (S)'],  10)

    def test_join_race_and_profession_abilities(self):
        abilities = Abilities()
        abilities.race_abilities = {'Hazard (Int)': 5, 'Intuicja (I)': 5, 'Język (Int) (Krainy Zgromadzenia)': 5, 'Mocna Głowa (Wt)': 3, 'Percepcja (I)': 3, 'Rzemiosło (Zr) (Kucharz)': 3}
        abilities.profession_abilities ={'Charyzma (Ogd) ': 1, 'Mocna Głowa (Wt)': 1,}
        abilities.join_race_and_profession_abilities()
        self.assertEqual(abilities.join_abilities, {'Charyzma (Ogd) ': 1, 'Hazard (Int)': 5, 'Intuicja (I)': 5, 'Język (Int) (Krainy Zgromadzenia)': 5, 'Mocna Głowa (Wt)': 4, 'Percepcja (I)': 3, 'Rzemiosło (Zr) (Kucharz)': 3})

    def test_give_profession_abilities_to_character(self):
        character = MagicMock()
        abilities = Abilities()
        abilities.join_abilities = {'Charyzma (Ogd) ': 1, 'Hazard (Int)': 5, 'Intuicja (I)': 5, 'Język (Int) (Krainy Zgromadzenia)': 5, 'Mocna Głowa (Wt)': 4, 'Percepcja (I)': 3, 'Rzemiosło (Zr) (Kucharz)': 3}
        abilities.give_profession_abilities_to_character(character)
        self.assertEqual(character.abilities, {'Charyzma (Ogd) ': 1, 'Hazard (Int)': 5, 'Intuicja (I)': 5, 'Język (Int) (Krainy Zgromadzenia)': 5, 'Mocna Głowa (Wt)': 4, 'Percepcja (I)': 3, 'Rzemiosło (Zr) (Kucharz)': 3})

