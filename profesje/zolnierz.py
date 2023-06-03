import random

klasa = "Wojownicy"

rozwiniecia_cech = {
    "Wt": 0,
    "WW": 0,
    "SW" : 0,
    "US" : -1,
    "I" : -2,
    "Ogd" : -3,
}

waga = ["WW", "Wt", "US", "SW", "S", "I", "Zw", "Ogd", "Int", "Zr"]

nazwa_profesji = {
    0 : "Rekrut",
    1 : "Rekrut",
    2 : "Żołnierz",
    3 : "Sierżant",
    4 : "Oficer"
}
status = {
    0 : "Srebro",
    1 : "Srebro",
    2 : "Srebro",
    3 : "Srebro",
    4 : "Złoto"
}
"Brąz", "Srebro", "Złoto"
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
    def __str__(self):
        pass
        

#losujemy rzutyi ustawiamy je według porządku co jest ważne  fff
rzuty = []
a = 10
while a>0:
     b = random.randint(1,10) + random.randint(1,10) 
     rzuty.append(b)
     a = a -1
    
    
slownik_cech_i_rzutow_w_kolejnosci_wagi = {}
rzuty.sort()
rzuty.reverse()
#print (rzuty)
a = 0
while a<10:
    slownik_cech_i_rzutow_w_kolejnosci_wagi[waga[a]]=rzuty[a]
    a = a + 1
#print(slownik_cech_i_rzutow_w_kolejnosci_wagi)

#budujemy słownik z umiejętności. Ich wartości będą wynosić od -2 na najwyższym tierze, do 0 na najniższym. Następnie 
# dodamy tier jaką mam mieć postać (od 0, do 4)

umiejkip= ["Atletyka (Zw)", "Broń Biała (WW) (Podstawowa)", "Język (Int) (Bitewny)", "Muzyka (Zr) (Bęben albo Piszczałka)", "Odporność (Wt)", "Opanowanie (SW)", "Unik (Zw)", "Wspinaczka (S)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
    
umiejkip= ["Broń Biała (WW) (Dowolna)", "Broń Zasięgowa (US) (Dowolna)", "Hazard (Int)", "Mocna Głowa (Wt)", "Plotkowanie (Ogd)", "Sztuka Przetrwania (Int)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Dowodzenie (Ogd)", "Intuicja (I)", "Leczenie (Int)", "Percepcja (I)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Nawigacja (I)", "Wiedza (Int) (Sztuka (Zr) Wojenna)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Urodzony Wojownik"]
talenty1 = ["Mocne Plecy", "Strzelec Wyborowy", "Szuler Kościany"]
talenty2 = ["Etykieta (Żołnierze)", "Musztra", "Szybkie Przeładowanie", "Tarczownik"]
talenty3 = ["Niewzruszony", "Walka w Ciasnocie", "Wódz", "Zmysł Bitewny"]
talenty4 = ["Inspirujący", "Mówca", "Obieżyświat", "Waleczne Serce"]

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



wyp1 = ["mundur", "skórzany napierśnik", "sztylet"]
wyp2 = ["broń (Dowolna)", "hełm", "napierśnik"]
wyp3 = ["oddział Żołnierzy", "symbol rangi"]
wyp4 = ["lekki koń bojowy z siodłem i uprzężą,mapa", "mundur dobrej jakości", "oddział Żołnierzy", "symbol rangi"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]


profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)