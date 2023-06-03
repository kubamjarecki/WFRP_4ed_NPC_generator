class Character:
        name = None     # string z imieniem
        profession = None #obiekt typu RaceTraits
        race = None #obiekt typu RaceTraits
        gender = None #string "Kobieta" lub "Mężczyzna"
        level = None #int
        characteristics = None # lista z dwoma słownikami [0] początkowa, [1] końcowa
        abilities = None #słownik gdzie kluczem jest umiejętność z cechą odpowiadająca w nawiasie, a wartością liczba
        talents = None  #lista ze stringami talentów
        appearance = None # obiekt typu Appearance z atrybutami .height, .eyes, .hair
        miss = None # słownik z kluczami: PP,PB,SZ,Status, żywotność
        equipment = None #lista ze stringami wyposażenia. Ostatni to ilośc złota
        