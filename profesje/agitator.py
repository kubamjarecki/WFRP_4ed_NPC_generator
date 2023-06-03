import random

klasa = "Mieszczanie"

nazwa_profesji = {
    0 : "Pamflecista ",
    1 : "Pamflecista ",
    2 : "Agitator ",
    3 : "Podżegacz ",
    4 : "Demagog "
}
status = {
    0 : "Brąz",
    1 : "Brąz ",
    2 : "Brąz",
    3 : "Brąz",
    4 : "Brąz"
}

rozwiniecia_cech = {
    "Int": 0,
    "Ogd": 0,
    "US" : 0,
    "Zw" : -1,
    "WW" : -2,
    "I" : -3,
}

class OdProfesji():
    def __init__(self, cechy, umiejki, talenty, wyposazenie, rozwiniecia_cech):
        self.cechy = cechy
        self.umiejki = umiejki
        self.talenty = talenty
        self.wyposazenie = wyposazenie
        self.rozwiniecia_cech = rozwiniecia_cech
        self.status = status
        self.nazwa_profesji = nazwa_profesji
        self.klasa = klasa

        

#losujemy rzuty ustawiamy je według porządku jak co jest ważne  fff
waga = ["Ogd", "US", "Int", "Zw", "WW", "SW", "Wt", "I", "S", "Zr", ]

rzuty = []
a = 10
while a>0:
     b = random.randint(1,10) + random.randint(1,10) 
     rzuty.append(b)
     a = a -1
    
    
slownik_cech_i_rzutow_w_kolejnosci_wagi = {}
rzuty.sort()
rzuty.reverse()

a = 0
while a<10:
    slownik_cech_i_rzutow_w_kolejnosci_wagi[waga[a]]=rzuty[a]
    a = a + 1

#budujemy słownik z umiejętności. Ich wartości będą wynosić od -2 na najwyższym tierze, do 0 na najniższym. Następnie 
# dodamy tier jaką mam mieć postać (od 0, do 4)

umiejkip= ["Charyzma (Ogd) ", "Mocna Głowa (Wt)", "Plotkowanie (Ogd)", "Przekupstwo (Ogd)", "Rzemiosło (Zr) (Drukarstwo)", "Sztuka (Zr) (Pisarstwo)", "Targowanie (Ogd)", "Wiedza (Int) (Polityka)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Dowodzenie (Ogd)", "Hazard (Int)", "Intuicja (I)", "Opanowanie (SW)", "Unik (Zw)", "Występy (Ogd) (Gawędziarstwo)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Atletyka (Zw)", "Broń Biała (WW) (Bijatyka)", "Percepcja (I)", "Zastraszanie (S)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Jeździectwo (Zw)  (Konie)", "Wiedza (Int) (Heraldyka)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2

#print(slownik_umiejetnosci_oraz_levelu)

talenty = []

talenty0 = ["Naciągacz"]
talenty1 = ["Czytanie/Pisanie", "Gadanina", "Towarzyski"]
talenty2 = ["Mówca", "Porywająca Gorliwość", "Przekonujący", "Ulicznik"]
talenty3 = ["Chodu!", "Cios Poniżej Pasa", "Gładkie Słówka", "Zejście z Linii"]
talenty4 = ["Charyzmatyczny", "Etykieta (Dowolna Grupa)", "Intrygant", "Krasomówstwo"]

talenty = {}

for idx, war in enumerate(talenty0):
    talenty[war] = 1
for idx, war in enumerate(talenty1):
    talenty[war] = 0
for idx, war in enumerate(talenty2):
    talenty[war] = -1
for idx, war in enumerate(talenty3):
    talenty[war] = -2
for idx, war in enumerate(talenty4):
    talenty[war] = -3

#print(talenty)

################ROBIMY ZBIÓR CAŁEGO MOŻLIWEGO EKWIPUNKU

if klasa == "Uczeni":
    wyp0 = ["sakwa", "sztylet", "torba na ramię z zestawem do pisania oraz 1k10 kart pergaminu", "ubranie"]
if klasa == "Mieszczanie":
    wyp0 = ["kapelusz", "płaszcz", "sakwa", "sztylet", "torba na ramię z posiłkiem","ubranie"]
if klasa == "Dworzanie":
    wyp0 = ["sakiewka z niezbędnikiem (grzebieniem patyczkiem do czyszczenia uszu i pęsetą)", "wyśmienite ubranie", "sztylet"]
if klasa == "Pospólstwo":
    wyp0 = ["płaszcz", "sakwa", "sztylet", "torba na ramię z racjami żywnościowymi(1 dzień)", "ubranie"]
if klasa == "Wędrowcy":
    wyp0 = ["plecak z hubką i krzesiwem", "kocem i racjami żywnościowymi(1 dzień)", "płaszcz", "sakwa", "sztylet", "ubranie"]
if klasa == "Wodniacy":
    wyp0 = ["płaszcz", "sakwa", "sztylet", "torba na ramię z butelką alkoholu", "ubranie"]
if klasa == "Łotrzy":
    wyp0 = ["kaptur lub maska", "sakwa", "sztylet", "ubranie", "torba na ramię z 2 świecami", "1k10 zapałek"]
if klasa == "Wojownicy":
    wyp0 = ["Broń Biała (WW)", "sakwa", "sztylet", "ubranie"]



wyp1 = ["młotek i gwoździe", "plik ulotek", "zestaw do pisania"]
wyp2 = ["skórzana kurta"]
wyp3 = ["broń ręczna", "pomocny Pamflecista"]
wyp4 = ["imponujący kapelusz", "Patron", "prasa drukarska", "3 Pamflecistów"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)