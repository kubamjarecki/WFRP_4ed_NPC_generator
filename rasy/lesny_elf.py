

import random

profesje = {
    1: "Czarodziej", 2: "Czarodziej", 3: "Czarodziej", 4: "Czarodziej", 5: "Uczony", 6: "Rzemieślnik", 7: "Rzemieślnik",
    8: "Rzemieślnik", 9: "Rzemieślnik", 10: "Rzemieślnik", 11: "Artysta", 12: "Artysta", 13: "Artysta", 14: "Artysta",
    15: "Doradca", 16: "Doradca", 17: "Doradca", 18: "Doradca", 19: "Poseł", 20: "Poseł", 21: "Poseł", 22: "Poseł",
    23: "Poseł", 24: "Poseł", 25: "Poseł", 26: "Szlachcic", 27: "Szlachcic", 28: "Szlachcic", 29: "Szlachcic",
    30: "Szlachcic", 31: "Szlachcic", 32: "Szpieg", 33: "Szpieg", 34: "Szpieg", 35: "Szpieg", 36: "Łowca", 37: "Łowca",
    38: "Łowca", 39: "Łowca", 40: "Łowca", 41: "Łowca", 42: "Łowca", 43: "Łowca", 44: "Łowca", 45: "Łowca", 46: "Mistyk",
    47: "Mistyk", 48: "Mistyk", 49: "Mistyk", 50: "Mistyk", 51: "Zielarz", 52: "Zielarz", 53: "Zielarz", 54: "Zielarz",
    55: "Zielarz", 56: "Zielarz", 57: "Zielarz", 58: "Zwiadowca", 59: "Zwiadowca", 60: "Zwiadowca", 61: "Zwiadowca",
    62: "Zwiadowca", 63: "Zwiadowca", 64: "Zwiadowca", 65: "Zwiadowca", 66: "Zwiadowca", 67: "Zwiadowca", 68: "Zwiadowca",
    69: "Kuglarz", 70: "Kuglarz", 71: "Kuglarz", 72: "Kuglarz", 73: "Kuglarz", 74: "Łowca Nagród", 75: "Łowca Nagród",
    76: "Posłaniec", 77: "Posłaniec", 78: "Posłaniec", 79: "Pirat Rzeczny", 80: "Banita", 81: "Banita", 82: "Banita",
    83: "Banita", 84: "Banita", 85: "Banita", 86: "Gladiator", 87: "Gladiator", 88: "Kawalerzysta", 89: "Kawalerzysta",
    90: "Kawalerzysta", 91: "Kawalerzysta", 92: "Kawalerzysta", 93: "Ochroniarz", 94: "Ochroniarz", 95: "Rycerz",
    96: "Rycerz", 97: "Żołnierz", 98: "Żołnierz", 99: "Żołnierz", 100: "Żołnierz"
    }

cechy= {
    "WW" : 30,
    "US" : 30, 
    "S" : 20,
    "Wt" : 20,
    "I" : 40,
    "Zw" : 30,
    "Zr" : 30,
    "Int" : 20,
    "SW" : 30,
    "Ogd" : 20,
}

szybkosc = 4
punkty_bohatera0 = 0
punkty_przeznaczenia0 = 0
punkty_wolne = 2

umiejki= ["Atletyka (Zw)", "Broń Biała (WW) (Podstawowa)", "Broń Zasięgowa (US) (Łuk)", "Język (Int) (Eltharin)", "Odporność (Wt)", "Percepcja (I)", "Skradanie (Zw)", "Sztuka Przetrwania (Int)", "Tropienie (I)", "Wspinaczka (S)", "Występy (Ogd) (Śpiewanie)", "Zastraszanie (S)"]
talenty2 = [ "Twardziel", "Percepcja Magiczna"]
talenty3 = ["Czytanie/Pisanie", "Niezwykle Odporny"]
talentyx = [talenty2, talenty3, "Włóczykij", "Widzenie w Ciemności", "Wyczulony Zmysł (Wzrok)"]

wzrost = [180, 3]

imiona1 = {1 : "Aes",
2 : "Ath",
3 : "Dor",
4 : "Far",
5 : "Gal",
6 : "Im",
7 : "Lin",
8 : "Mal",
9 : "Mor",
10 : "Ullia"}

imiona2 = {1 : "a",
2 : "ath",
3 : "dia",
4 : "en",
5 : "for",
6 : "lor",
7 : "mar",
8 : "ol",
9 : "sor",
10 : "than"}

imiona3 = {1 : "arha",
2 : "anhu",
3 : "dda",
4 : "han",
5 : "loc",
6 : "noc",
7 : "oth",
8 : "ryn",
9 : "stra",
10 : "wyth"}

los = random.randint(1,10)
a = imiona1[los]
los = random.randint(1,10)
b = imiona2[los]
los = random.randint(1,10)
c = imiona3[los]
imiex_z = a + b + c

los = random.randint(1,10)
a = imiona1[los]
los = random.randint(1,10)
b = imiona2[los]
los = random.randint(1,10)
c = imiona3[los]
imiex_m = a + b + c

wlosy = {0 : "Brzozowobialy",
1 : "Blond",
2 : "Różowe zloto",
3 : "Miodowoblond",
4 : "Miodowoblond",
5 : "Miodowoblond",
6 : "Brązowy",
7 : "Brązowy",
8 : "Brązowy",
9 : "Brązowy",
10 : "Mahoniowy",
11 : "Mahoniowy",
12 : "Mahoniowy",
13 : "Ciemny brąz",
14 : "Ciemny brąz",
15 : "Ciemny brąz",
16 : "Sjena",
17 : "Hebanowy",
18 : "Niebiesko-czarny",
19 : "Niebiesko-czarny"
} 

oczy = {0 : "Kość słoniowa",
1 : "Antracyt",
2: "Kolor bluszczu",
3: "Kolor mchu",
4 : "Kolor mchu",
5 : "Kolor mchu",
6 : "Kasztanowy",
7 : "Kasztanowy",
18 : "Kasztanowy",
9 : "Kasztanowy",
10 : "Kasztanowy",
11 : "Kasztanowy",
12 : "Kasztanowy",
13 : "Ciemnobrązowy",
14 : "Ciemnobrązowy",
15 : "Ciemnobrązowy",
16 : "Jasnobrązowy",
17 : "Złotobrązowy",
18 : "Fiołkowy",
19 : "Fiołkowy"}
