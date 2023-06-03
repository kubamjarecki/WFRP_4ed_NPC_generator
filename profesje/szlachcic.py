import random

klasa = "Dworzanie"

rozwiniecia_cech = {
    "WW": 0,
    "I": 0,
    "Zr" : 0,
    "Ogd" : -1,
    "Int" : -2,
    "SW" : -3,
}

waga = ["WW", "I", "Ogd", "S", "Int", "SW", "Zr", "Wt", "Zw", "US"]

nazwa_profesji = {
    0 : "Dziedzic",
    1 : "Dziedzic",
    2 : "Szlachcic",
    3 : "Magnat",
    4 : "Lord"
}
status = {
    0 : "Złoto",
    1 : "Złoto",
    2 : "Złoto",
    3 : "Złoto",
    4 : "Złoto"
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

umiejkip= ["Broń Biała (WW) (Szermiercza)", "Hazard (Int)", "Dowodzenie (Ogd)", "Mocna Głowa (Wt)", "Muzyka (Zr) (Dowolna)", "Przekupstwo (Ogd)", "Wiedza (Int) (Heraldyka)", "Zastraszanie (S)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Broń Biała (WW) (Parująca)", "Charyzma (Ogd) ", "Język (Int)(Klasyczny)", "Jeździectwo (Zw)  (Konie)", "Plotkowanie (Ogd)", "Wiedza (Int) (Lokalna)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Intuicja (I)", "Język (Int) (Dowolny)", "Percepcja (I)", "Wiedza (Int)(Polityka)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Tropienie (I)", "Wiedza (Int) (Dowolna)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Błękitna Krew"]
talenty1 = ["Czytanie/Pisanie", "Etykieta (Szlachta)", "Szczęście"]
talenty2 = ["Atrakcyjny", "Charyzmatyczny", "Hulaka", "Łapówkarz"]
talenty3 = ["Intrygant", "Mówca", "Zimna krew", "Żyłka handlowa"]
talenty4 = ["Majętny", "Władcza Postura", "Wódz", "Żelazna Wola"]

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



wyp1 = ["biżuteria warta 3k10 ZK", "dworski strój", "floret", "osobisty Służący"]
wyp2 = ["biżuteria warta 50 ZK", "dobry płaszcz albo lewak", "dworski strój dobrej jakości", "dworski strój", "koń wierzchowy z rzędem albo powóz", "4 Służący domowi"]
wyp3 = ["biżuteria warta 200 ZK", "lenno", "sygnet", "2 komplety strojów dworskich dobrej jakości", "200 ZK"]
wyp4 = ["biżuteria warta 500 ZK", "floret dobrej jakości", "500 ZK", "4 komplety strojów dworskich najlepszej jakości", "Prowincja"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]


profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)