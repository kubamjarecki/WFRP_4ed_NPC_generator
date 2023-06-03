import random
profesje = {
    1: "Aptekarz", 2: "Inżynier", 3: "Inżynier", 4: "Inżynier", 5: "Medyczka", 6: "Prawnik", 7: "Prawnik",
    8: "Uczony", 9: "Uczony", 10: "Agitator", 11: "Agitator", 12: "Kupiec", 13: "Kupiec", 14: "Kupiec",
    15: "Kupiec", 16: "Mieszczanin", 17: "Mieszczanin", 18: "Mieszczanin", 19: "Mieszczanin", 20: "Mieszczanin",
    21: "Mieszczanin", 22: "Rzemieślnik", 23: "Rzemieślnik", 24: "Rzemieślnik", 25: "Rzemieślnik", 26: "Rzemieślnik",
    27: "Rzemieślnik", 28: "Strażnik", 29: "Strażnik", 30: "Strażnik", 31: "Szczurołap", 32: "Śledczy",
    33: "Śledczy", 34: "Żebrak", 35: "Artysta", 36: "Doradca", 37: "Doradca", 38: "Namiestnik", 39: "Namiestnik",
    40: "Poseł", 41: "Poseł", 42: "Służący", 43: "Szlachcic", 44: "Szpieg", 45: "Zwadźca", 46: "Chłop",
    47: "Górnik", 48: "Górnik", 49: "Górnik", 50: "Górnik", 51: "Górnik", 52: "Łowca", 53: "Łowca", 54: "Zarządca",
    55: "Zarządca", 56: "Zwiadowca", 57: "Domokrążca", 58: "Domokrążca", 59: "Kuglarz", 60: "Kuglarz",
    61: "Łowca Nagród", 62: "Łowca Nagród", 63: "Łowca Nagród", 64: "Łowca Nagród", 65: "Posłaniec", 66: "Posłaniec",
    67: "Woźnica", 68: "Doker", 69: "Doker", 70: "Flisak", 71: "Flisak", 72: "Pilot Rzeczny", 73: "Pirat Rzeczny",
    74: "Przemytnik", 75: "Przemytnik", 76: "Przewoźnik", 77: "Przewoźnik", 78: "Żeglarz", 79: "Banita",
    80: "Banita", 81: "Banita", 82: "Hiena Cmentarna", 83: "Rekietier", 84: "Zlodziej", 85: "Gladiator",
    86: "Gladiator", 87: "Gladiator", 88: "Ochroniarz", 89: "Ochroniarz", 90: "Ochroniarz", 91: "Oprych",
    92: "Oprych", 93: "Oprych", 94: "Zabójca", 95: "Zabójca", 96: "Zabójca", 97: "Zabójca", 98: "Żołnierz",
    99: "Żołnierz", 100: "Żołnierz"
    }

cechy= {
    "WW" : 30,
    "US" : 20, 
    "S" : 20,
    "Wt" : 30,
    "I" : 20,
    "Zw" : 10,
    "Zr" : 30,
    "Int" : 20,
    "SW" : 40,
    "Ogd" : 10,
}

umiejki= ["Broń Biała (WW) (Podstawowa)", 
    "Język (Int) (Khazalid)", 
    "Opanowanie (SW)" ,
    "Mocna Głowa (Wt)", 
    "Rzemiosło (Zr) (Dowolne)", 
    "Wiedza (Int) (Geologia)",
    "Wiedza (Int) (Krasnoludy)", 
    "Wiedza (Int) (Metalurgia)", 
    "Wycena (Int)", 
    "Występy (Ogd) (Gawędziarstwo)",
    "Zastraszanie (S)"]

talenty2 = ["Czytanie/Pisanie", "Nieustępliwy"]
talenty3 = ["Odporność Psychiczna", "Nieugięty"]
talentyx = [ talenty2, talenty3, "Odporny na Magię", "Tragarz", "Widzenie w Ciemności"]



wzrost = [130, 2]

imiona_m = ["Alarik", "Alrik", "Argat", "Argorn", "Arngrim", "Azram", "Azrel", "Bafur", "Baldrik", "Balim", "Balin", "Balzud", "Bardin", "Barnok", "Beledar", "Belorn", "Bifur", "Bohdi", "Boltrez", "Bombur", "Borek", "Borgin", "Borig", "Borri","Bragi", "Brand", "Brock", "Broderin", "Brokk", "Brond", "Brun", "Burlok", "Dain", "Darin", "Darluk", "Decredie", "Deemax", "Dern", "Dimzad", "Dirk", "Dolgan", "Dori", "Dorin", "Dowbur", "Dron", "Drumin", "Dumwin", "Duncan", "Dunnor", "Durin", "Durlag", "Durnatz", "Dwalin", "Fimbur", "Fjalar", "Flint", "Frar", "Fundin", "Gafar", "Garag", "Garil", "Garin", "Garick", "Garm", "Gazil", "Gazula", "Gazunda", "Gharth", "Gimli", "Gloin", "Glosh", "Gnarok", "Gnimsh", "Gomrund", "Gotmong", "Gorm", "Gorum", "Gotran", "Gotrek", "Gotri", "Grallen", "Greip", "Grim", "Grimnir", "Grolf", "Grom", "Grommo", "Gromph", "Grum", "Grun", "Grunthor", "Hadrin", "Hagmar", "Hagri", "Haki", "Hannar", "Hargin", "Hargrim", "Helgrind", "Holgar", "Hornborin", "Hrotghar",
"Hekrath", "Ibun", "Ivan", "Kargan", "Kargrim", "Kazador", "Kazgar", "Kazrik", "Ketiger", "Kharas", "Kili", "Kragg", "Krangal", "Lofar", "Logi", "Mabal", "Malakai", "Malkar", "Melhorn", "Mimir", "Modi", "Molrik", "Nabbi", "Nahar", "Nain", "Narg", "Nester", "Nibin", "Nordri", "Nori", "Norin", "Nyrad", "Odum", "Oinn", "Okri", "Palin", "Ranhar", "Reghar", "Reck", "Reginn", "Reorx", "Rind", "Rogar", "Serg", "Sirrush",
"Skaagne", "Skalf", "Snorri", "Sorgi", "Stapmi", "Steg", "Stron", "Sudri", "Surt", "Taggin", "Tairon", "Teran", "Thadrin", "Thain", "Thekkr", "Thingrim", "Thir", "Thor", "Thorek", "Thorgal", "Thorgrim", "Thorin", "Throd", "Thror,Thunar", "Tingrim", "Trygg", "Turin", "Tyorl", "Ug", "Ulfar", "Ulli", "Ulther", "Uther", "Ungrim", "Varek", "Wargrim", "Westri", "Widar", "Wjard", "Yarpen", "Yazeran", "Ymir", "Yodri", "Yog", "Zonri"]


imiona_z = ["Akre", "Ametrin", "Amma", "Angeya", " Angrboda", " Ankharma", " Anvila", " Arka", " Arrica", " Athrina", " Atla", " Aurboda", " Ayla", " Azlana", " Azraya", " Bestla", " Beyla", " Blid", " Boria", " Daina", " Dalla", " Danra", " Diara", " Drumba", " Dunerka", " Edria", " Eistla", " Erna", " Eudora", " Farmira", " Fulla", " Gael", " Gasta", " Gilderia", " Grella", " Helgar", " Hilga", " Jaheira", 
"Janara", " Jarnsaksa", " Jorika", " Kamira", " Kathara", " Keira", " Keri", " Krina", " Layfeja", " Magda", " Margara", " Meili", " Meure", " Modira", " Myrtha", " Oria", " Renfri", " Rhizma", " Rigunta", " Runa", " Serewassa", " Siri", " Sylga", " Teria", " Terigne", " Tesela", " Tessa", " Thera", " Therla", " Titta", " Ulfrun", " Ulla", " Umina", " Valaya", " Vanirka", " Varna", " Vigaya"]
los = random.randint(0,74)
if los > 74:
    los = 65
a = imiona_z[los]
los = random.randint(0,191)
b = imiona_m[los]
imiex_z = a + " " + b + "sdottir"


los = random.randint(0,191)
a = imiona_m[los]
los = random.randint(0,191)
b = imiona_m[los]
imiex_m =  a + " " + b + "son"


wlosy = {0 : "Blond",
1 : "Lniany",
2 : "Rudawy",
3 : "Brązowy",
4 : "Brązowy",
5 : "Brązowy",
6 : "Miedziany",
7 : "Miedziany",
8 : "Miedziany",
9 : "Miedziany",
10 : "Brąz",
11 : "Brąz",
12 : "Brąz",
13 : "Brąz",
14 : "Brąz",
15 : "Brąz",
16 : "Ciemny brąz",
17 : "Rudy brąz",
18 : "Czarny",
19 : "Czarny"} 

oczy = {0 : "Czarny jak wegiel",
1 : "Szary jak olów",
2 : "Stalowoszary",
3 : "Niebieski",
4 : "Niebieski",
5 : "Niebieski",
6 : "Brązowy jak ziemia",
7 : "Brązowy jak ziemia",
8 : "Brązowy jak ziemia",
9 : "Brązowy jak ziemia",
10 : "Ciemnobrązowy",
11 : "Ciemnobrązowy",
12 : "Ciemnobrązowy",
13 : "Orzechowy",
14 : "Orzechowy",
15 : "Orzechowy",
16 : "Zielony",
17 : "Ciemny miedziany",
18 : "Złoty",
19 : "Złoty"}

oczy_in = {0: 'Blond', 1: 'Lniany', 2: 'Rudawy', 3: 'Brązowy', 4: 'Miedziany', 5: 'Brąz', 6: 'Ciemny brąz', 7: 'Rudy brąz', 8: 'Czarny'}
wlosy_in = {0: 'Czarny jak wegiel', 1: 'Szary jak olów', 2: 'Stalowoszary', 3: 'Niebieski', 4: 'Brązowy jak ziemia', 5: 'Ciemnobrązowy', 6: 'Orzechowy', 7: 'Zielony', 8: 'Ciemny miedziany', 9: 'Złoty'}

punkty_bohatera0 = 0
punkty_przeznaczenia0 = 2
punkty_wolne = 2
szybkosc = 3