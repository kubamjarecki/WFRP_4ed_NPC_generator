
import random

profesje =  {
    1: 'Aptekarz', 2: 'Inżynier', 3: 'Medyk', 4: 'Medyk', 5: 'Prawnik', 6: 'Prawnik', 7: 'Uczony',
    8: 'Uczony', 9: 'Agitator', 10: 'Agitator', 11: 'Kupiec', 12: 'Kupiec', 13: 'Kupiec', 14: 'Kupiec',
    15: 'Mieszczanin', 16: 'Mieszczanin', 17: 'Mieszczanin', 18: 'Rzemieślnik', 19: 'Rzemieślnik',
    20: 'Rzemieślnik', 21: 'Rzemieślnik', 22: 'Rzemieślnik', 23: 'Strażnik', 24: 'Strażnik',
    25: 'Szczurołap', 26: 'Szczurołap', 27: 'Szczurołap', 28: 'Śledczy', 29: 'Śledczy', 30: 'Żebrak',
    31: 'Żebrak', 32: 'Żebrak', 33: 'Żebrak', 34: 'Artysta', 35: 'Poseł', 36: 'Doradca', 37: 'Namiestnik',
    38: 'Namiestnik', 39: 'Poseł', 40: 'Służący', 41: 'Służący', 42: 'Służący', 43: 'Służący',
    44: 'Służący', 45: 'Służący', 46: 'Szpieg', 47: 'Chłop', 48: 'Chłop', 49: 'Chłop', 50: 'Górnik',
    51: 'Łowca', 52: 'Łowca', 53: 'Zarządca', 54: 'Zielarz', 55: 'Zielarz', 56: 'Zielarz', 57: 'Zwiadowca',
    58: 'Domokrążca', 59: 'Domokrążca', 60: 'Kuglarz', 61: 'Kuglarz', 62: 'Kuglarz', 63: 'Łowca Nagród',
    64: 'Posłaniec', 65: 'Posłaniec', 66: 'Strażnik Dróg', 67: 'Woźnica', 68: 'Woźnica', 69: 'Doker',
    70: 'Doker', 71: 'Doker', 72: 'Flisak', 73: 'Flisak', 74: 'Flisak', 75: 'Pilot Rzeczny',
    76: 'Przemytnik', 77: 'Przemytnik', 78: 'Przemytnik', 79: 'Przemytnik', 80: 'Przewoźnik',
    81: 'Strażnik Rzeczny', 82: 'Żeglarz', 83: 'Banita', 84: 'Paser', 85: 'Hiena Cmentarna', 86: 'Rajfur',
    87: 'Rajfur', 88: 'Rajfur', 89: 'Rekietier', 90: 'Szarlatan', 91: 'Złodziej', 92: 'Złodziej',
    93: 'Złodziej', 94: 'Złodziej', 95: 'Gladiator', 96: 'Ochroniarz', 97: 'Ochroniarz', 98: 'Żołnierz',
    99: 'Żołnierz', 100: 'Żołnierz'
    }

cechy= {
    "WW" : 10,
    "US" : 30, 
    "S" : 10,
    "Wt" : 20,
    "I" : 20,
    "Zw" : 20,
    "Zr" : 30,
    "Int" : 20,
    "SW" : 30,
    "Ogd" : 30,
}

szybkosc = 3
punkty_bohatera0 = 2
punkty_przeznaczenia0 = 0
punkty_wolne = 3

umiejki= ["Charyzma (Ogd) ", "Hazard (Int)", "Intuicja (I)", "Język (Int) (Krainy Zgromadzenia)", "Mocna Głowa (Wt)", "Percepcja (I)", "Rzemiosło (Zr) (Kucharz)", "Skradanie (Zw) (Dowolne)", "Targowanie (Ogd)", "Unik (Zw)", "Wiedza (Int) (Reikland)", "Zwinne Palce (Zr)"]

talentyx = ["Mały", "Odporność (Wt) na Chaos", "Widzenie w Ciemności", "Wyczulony Zmysł (Smak)", 2]

wzrost = [95, 2]
im_m = ["Ferdinand (Fred)", "Heironymus (Hiro)", "Maximilian(Max)", "Theodosius (Theo)", "Achim", "Adam", "Albert", "Albie", "Alfred", "Alton", "Asham", "Ashford", "Astin", "Axel", "Bertik", "Bertrad", "Blasco", "Bredon", "Burgis", "Burke", "Carruthers", "Carl", "Chibald", "Cibber", "Cottington", "Dekker", "Dobb", "Drayton", "Dugal", "Dyer", "Edgar", "Eldren", "Ellyot", "Eucken", "Fashi", "Fenton", "Fenwark", "Gascoyn", "Gues", "Googe", "Gosson", "Hesselwhite", "Hobb", "Hobbin", "Hodkin", "Hoiquiss", "Hugo", "Jacob", "Jaq", "Jenkin", "Joop", "Joost", "Kelsoe", "Kemble", "Kent", "Linton", "Lodge", "Lollard", "Ludo", "Ludwedge", "Lynwerd", "Map", "Marlow", "Marston", "Martobee", "Max", "Mendel", "Merrick", "Merridee", "Moss", "Murr", "Nashe", "Niklaus", "Niles", "Nivers", "Norbe", "Nython", "Orlane", "Oscar", "Otem", "Parse", "Paul", "Pence", "Penge", "Plunkett", "Pomme", "Pons", "Poole", "Quillan", "Quince", "Quinn", "Ralf", "Reene", "Reeve", "Reswald", "Rudi", "Ruskin", "Seldon", "Sime", "Spence", "Syler", "Talbot", "Tananger", "Taqi", "Tarquin", "Tasse", "Taum", "Tavi", "Tew", "Thame", "Theo", "Thomas", "Thorne", "Tibbs", "Tichbourne", "Tillyard", "Tobus", "Tolquist", "Tuck", "Tyldan", "Tyman", "Tyndal", "Udo", "Valens", "Vaughn", "Vicars", "Victor", "Wade", "Walter", "Warwyck", "Wat", "Watters", "Wim", "Wyatt"]
im_z = ["Antoniella (Anni)", "Esmerelda(Esme)", "Thomasina (Tina)", "Rosalinda(Rosa)", "Agnes", "Alice", "Amabelle", "Barthony", "Beasley", "Beaswell", "Bree", "Briley", "Canty", "Crowley", "Cubbardy", "Dee", "Dendy", "Dudney", "Dunleary", "Elena", "Eva", "Frida", "Gentry", "Greta", "Hanna", "Heidi", "Hilda", "Hoby", "Janna", "Karin", "Ketta", "Lane", "Leese", "Leni", "Lidda", "Linshey", "Lyly", "Maere", "Marie", "Misha", "Mosely", "Petra", "Quettery", "Silma", "Sophia", "Susi", "Tarby", "Tella", "Theda", "Tilbury", "Tish", "Ulla", "Wanda"]

nazwisko = ["Ashfield", "Brandysnap", "Hayfoot", "Rumster", "Shortbottom", "Thorncobble", "Haleberry", "Greenhill", "Furfoot", "Greendale", "Warmfeet", "Brandysnap "]

rand_im = random.randint(0,(len(im_m))- 1)
rand_iz = random.randint(0, (len(im_z))-1)
rand_naz = random.randint(0,(len(nazwisko))-1)

imiex_m = im_m[rand_im] + " " + nazwisko[rand_naz]
imiex_z = im_z[rand_iz] + " " + nazwisko[rand_naz]

wlosy = { 1: 'Biały', 2: 'Lniany', 3: 'Rudawy', 4: 'Złoty', 5: 'Złoty', 6: 'Złoty', 7: 'Kasztanowy', 8: 'Kasztanowy', 9: 'Kasztanowy', 10: 'Kasztanowy', 11: 'Rudy', 12: 'Rudy', 13: 'Musztardowy', 14: 'Musztardowy', 15: 'Musztardowy', 16: 'Musztardowy', 17: 'Migdałowy', 18: 'Czekoladowy', 19: 'Lukrecjowy'}

oczy = {1: 'Jasnoszary', 2: 'Szary', 3: 'Błękitny', 4: 'Niebieski', 5: 'Niebieski', 6: 'Niebieski', 7: 'Zielony', 8: 'Zielony', 9: 'Zielony', 10: 'Zielony', 11: 'Orzechowy', 12: 'Orzechowy', 13: 'Orzechowy', 14: 'Brązowy', 15: 'Brązowy', 16: 'Brązowy', 17: 'Miedziany', 18: 'Ciemnobrązowy', 19: 'Ciemnobrązowy'}

wlosy_in = {0: 'Biały', 1: 'Lniany', 2: 'Rudawy', 3: 'Złoty', 4: 'Kasztanowy', 5: 'Rudy', 6: 'Musztardowy', 7: 'Migdałowy', 8: 'Czekoladowy', 9: 'Lukrecjowy'}

oczy_in = {0: 'Jasnoszary', 1: 'Szary', 2: 'Błękitny', 3: 'Niebieski', 4: 'Zielony', 5: 'Orzechowy', 6: 'Brązowy', 7: 'Miedziany', 8: 'Ciemnobrązowy'}
