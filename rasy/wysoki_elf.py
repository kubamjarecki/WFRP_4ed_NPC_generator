
import random

profesje = {
    1: 'Aptekarz', 2: 'Aptekarz', 3: 'Czarodziej', 4: 'Czarodziej', 5: 'Czarodziej', 6: 'Czarodziej',
    7: 'Medyk', 8: 'Medyk', 9: 'Prawnik', 10: 'Prawnik', 11: 'Prawnik', 12: 'Prawnik', 13: 'Uczony',
    14: 'Uczony', 15: 'Uczony', 16: 'Uczony', 17: 'Kupiec', 18: 'Kupiec', 19: 'Kupiec', 20: 'Kupiec',
    21: 'Kupiec', 22: 'Mieszczanin', 23: 'Mieszczanin', 24: 'Rzemieślnik', 25: 'Rzemieślnik',
    26: 'Rzemieślnik', 27: 'Strażnik', 28: 'Śledczy', 29: 'Śledczy', 30: 'Artysta', 31: 'Doradca',
    32: 'Doradca', 33: 'Namiestnik', 34: 'Namiestnik', 35: 'Poseł', 36: 'Poseł', 37: 'Poseł',
    38: 'Szlachcic', 39: 'Szlachcic', 40: 'Szlachcic', 41: 'Szpieg', 42: 'Szpieg', 43: 'Szpieg',
    44: 'Zwadźca', 45: 'Zwadźca', 46: 'Łowca', 47: 'Łowca', 48: 'Łowca', 49: 'Zielarz', 50: 'Zielarz',
    51: 'Zwiadowca', 52: 'Zwiadowca', 53: 'Zwiadowca', 54: 'Zwiadowca', 55: 'Zwiadowca', 56: 'Zwiadowca',
    57: 'Kuglarz', 58: 'Kuglarz', 59: 'Kuglarz', 60: 'Łowca Nagród', 61: 'Łowca Nagród', 62: 'Łowca Nagród',
    63: 'Posłaniec', 64: 'Przemytnik', 65: 'Przewoźnik', 66: 'Żeglarz', 67: 'Żeglarz', 68: 'Żeglarz',
    69: 'Żeglarz', 70: 'Żeglarz', 71: 'Żeglarz', 72: 'Żeglarz', 73: 'Żeglarz', 74: 'Żeglarz', 75: 'Żeglarz',
    76: 'Żeglarz', 77: 'Żeglarz', 78: 'Żeglarz', 79: 'Żeglarz', 80: 'Żeglarz', 81: 'Banita', 82: 'Banita',
    83: 'Banita', 84: 'Rajfur', 85: 'Rajfur', 86: 'Szarlatan', 87: 'Szarlatan', 88: 'Szarlatan',
    89: 'Gladiator', 90: 'Gladiator', 91: 'Kawalerzysta', 92: 'Kawalerzysta', 93: 'Kawalerzysta',
    94: 'Kawalerzysta', 95: 'Ochroniarz', 96: 'Ochroniarz', 97: 'Oprych', 98: 'Rycerz', 99: 'Żołnierz',
    100: 'Żołnierz'}

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

umiejki= ["Broń Biała (WW) (Podstawowa)", "Broń Zasięgowa (US) (Łuk)", "Dowodzenie (Ogd)", "Język (Int) (Eltharin)", "Muzyka (Zr)(Dowolny instrument)", "Nawigacja (I)", "Opanowanie (SW)", "Pływanie (S)", "Percepcja (I)", "Wycena (Int)", "Występy (Ogd) (Śpiewanie)", "Żeglarstwo (Zw)"]

talenty2 = [ "Szósty Zmysł", "Percepcja Magiczna"]
talenty3 = ["Błyskotliwość", "Zimna Krew"]
talentyx = [talenty2, talenty3, "Czytanie/Pisanie", "Wyczulony Zmysł (Wzrok)", "Widzenie w Ciemności"]

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

imiona3 = {1: 'andril', 2: 'anel', 3: 'ellion', 4: 'fin', 5: 'il', 6: 'irian', 7: 'mor', 8: 'nil', 9: 'ric', 10: 'wing'}

los = random.randint(1,10)
if los> 10:
    los = 9

a = imiona1[los]
los = random.randint(1,10)

if los> 10:
    los = 9
b = imiona2[los]
los = random.randint(1,10)

if los> 10:
    los = 9
c = imiona3[los]
imiex_z = a + b + c

los = random.randint(1,10)
if los> 10:
    los = 9
a = imiona1[los]
los = random.randint(1,10)
if los> 10:
    los = 9
b = imiona2[los]
los = random.randint(1,10)
if los> 10:
    los = 9
c = imiona3[los]
imiex_m = a + b + c

wlosy = { 1: 'Srebrnosiwy', 2: 'Popielaty', 3: 'Jasny blond', 4: 'Miodowoblond', 5: 'Miodowoblond', 6: 'Miodowoblond', 7: 'Żółty', 8: 'Żółty', 9: 'Żółty', 10: 'Żółty', 11: 'Miedziany blond', 12: 'Miedziany blond', 13: 'Miedziany blond', 14: 'Blond', 15: 'Blond', 16: 'Blond', 17: 'Migdałowy', 18: 'Czerwony', 19: 'Czarny'}

oczy = {1: 'Czarny jak smoła', 2: 'Ametystowy', 3: 'Akwamaryna', 4: 'Szafirowy', 5: 'Szafirowy', 6: 'Szafirowy', 7: 'Turkusowy', 8: 'Turkusowy', 9: 'Turkusowy', 10: 'Turkusowy', 11: 'Szmaragdowy', 12: 'Szmaragdowy', 13: 'Szmaragdowy', 14: 'Bursztynowy', 15: 'Bursztynowy', 16: 'Bursztynowy', 17: 'Miedziany', 18: 'Cytrynowożółty', 19: 'Złoty'}
