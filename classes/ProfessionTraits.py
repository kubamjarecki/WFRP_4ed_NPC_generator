class ProfessionTraits:
    def __init__(self, klasa, nazwa_profesji, status, rozwiniecia_cech, waga, slownik_umiejetnosci_oraz_levelu, talenty, wyp):
        self.klasa_str = klasa
        self.nazwa_profesji_dict = nazwa_profesji
        self.status_dict = status
        self.rozwiniecia_cech_dict = rozwiniecia_cech
        self.waga_list = waga
        self.umiejki_i_level_dict = slownik_umiejetnosci_oraz_levelu
        self.talenty_i_level_dict = talenty
        self.wyposazenie_list_of_lists = wyp
