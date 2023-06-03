class RaceTraits:
    def __init__(self, nazwa, cechy, umiejki, talenty, wzrost, imiex_m, imiex_z, wlosy, oczy, profesje, pp, pb, sz, p0):
        self.nazwa = nazwa
        self.cechy_bez_rzutów_slownik = cechy
        self.tabela_losowania_profesji_slownik = profesje
        self.umiejętności_od_rasy_3_i_5_lista = umiejki
        self.talenty_z_liczba_losowych_lista_list = talenty
        self.pp_poczatkowe_int = pp
        self.sz_od_rasy = sz
        self.pb_poczatkowe = pb
        self.punkty_do_rozdania = p0
        self.wzrost_bazowe_i_liczba_K10 = wzrost
        self.losowe_imie_meskie = imiex_m
        self.losowe_imie_zenskie = imiex_z
        self.slownik_do_losowania_wlosow = wlosy
        self.slownik_do_losowania_oczu = oczy


        