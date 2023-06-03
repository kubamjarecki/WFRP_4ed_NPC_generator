import unittest
from classes.ProfessionTraits import ProfessionTraits
from profesje.agitator import klasa, nazwa_profesji, status, rozwiniecia_cech, waga, slownik_umiejetnosci_oraz_levelu, talenty, wyp
# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    def test_ProfessionTraits_has_all_atributes_after_creation(self):
        profes = ProfessionTraits(klasa, nazwa_profesji, status, rozwiniecia_cech, waga, slownik_umiejetnosci_oraz_levelu, talenty, wyp)
        self.assertIs(type(profes.klasa_str), str  )
        self.assertIs(type(profes.nazwa_profesji_dict), dict )
        self.assertIs(type(profes.status_dict), dict )
        self.assertIs(type(profes.rozwiniecia_cech_dict), dict  )
        self.assertIs(type(profes.waga_list), list  )
        self.assertIs(type(profes.umiejki_i_level_dict), dict  )
        self.assertIs(type(profes.talenty_i_level_dict), dict  )
        self.assertIs(type(profes.wyposazenie_list_of_lists), list )