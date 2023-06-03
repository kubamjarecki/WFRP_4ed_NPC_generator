import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from classes.Character import Character
from classes.RaceSeizure import RaceSeizure
from classes.RaceTraits import RaceTraits
from rasy.hobbit import cechy, szybkosc, punkty_bohatera0, punkty_przeznaczenia0, punkty_wolne, profesje, umiejki, talentyx, wzrost, imiex_m, imiex_z, wlosy, oczy
# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    def test_RaceTraits_has_all_atributes_after_creation(self):
        nazwa = "Hobbit"
        cechy_rasowe = RaceTraits(nazwa = nazwa, cechy = cechy, sz = szybkosc, pb = punkty_bohatera0, pp = punkty_przeznaczenia0, p0 = punkty_wolne, profesje = profesje, umiejki = umiejki, talenty=talentyx, wzrost=wzrost, imiex_m=imiex_m, imiex_z=imiex_z, wlosy = wlosy, oczy=oczy )
        self.assertIs(type(cechy_rasowe.cechy_bez_rzutów_slownik), dict )
        self.assertIs(type(cechy_rasowe.tabela_losowania_profesji_slownik), dict )
        self.assertIs(type(cechy_rasowe.umiejętności_od_rasy_3_i_5_lista), list )
        self.assertIs(type(cechy_rasowe.talenty_z_liczba_losowych_lista_list), list )
        self.assertIs(type(cechy_rasowe.pp_poczatkowe_int), int)
        self.assertIs(type(cechy_rasowe.sz_od_rasy),int  )
        self.assertIs(type(cechy_rasowe.pb_poczatkowe), int  )
        self.assertIs(type(cechy_rasowe.punkty_do_rozdania), int  )
        self.assertIs(type(cechy_rasowe.wzrost_bazowe_i_liczba_K10), list  )
        self.assertIs(type(cechy_rasowe.losowe_imie_meskie), str  )
        self.assertIs(type(cechy_rasowe.losowe_imie_zenskie), str  )
        self.assertIs(type(cechy_rasowe.slownik_do_losowania_wlosow), dict  )
        self.assertIs(type(cechy_rasowe.slownik_do_losowania_oczu), dict  )
        self.assertIs(type(cechy_rasowe.nazwa), str  )
    
        
        