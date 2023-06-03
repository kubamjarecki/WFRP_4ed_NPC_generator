import random

klasa = "Pospólstwo"

rozwiniecia_cech = {
    "S": 0,
    "Wt": 0,
    "SW" : 0,
    "WW" : -1,
    "I" : -2,
    "Ogd" : -3,
}

waga = ["WW", "S", "Wt", "SW", "I", "Ogd", "Zw", "Int",  "Zr", "US"]

nazwa_profesji = {
    0 : "Poszukiwacz",
    1 : "Poszukiwacz ",
    2 : "Górnik",
    3 : "Sztygar",
    4 : "Mistrz Górnictwa"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Brąz",
    4 : "Srebro"
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

umiejkip= ["Broń Biała (WW) (Dwuręczna)", "Intuicja (I)", "Odporność (Wt)", "Opanowanie (SW)", "Percepcja (I)", "Pływanie (S)", "Sztuka Przetrwania (Int)", "Wiedza (Int) (Lokalna)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Broń Biała (WW) (Podstawowa)", "Mocna Głowa (Wt)", "Rzemiosło (Zr) (Materiały Wybuchowe)", "Sekretne Znaki (Int) (Górników)", "Wspinaczka (S)", "Wycena (Int)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Plotkowanie (Ogd)", "Rzemiosło (Zr) (Inżynieria)", "Skradanie (Podziemia)", "Wiedza (Int) (Geologia)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Charyzma (Ogd) ", "Dowodzenie (Ogd)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Tragarz"]
talenty1 = ["Doświadczony Wędrowiec (Teren Skalisty)",  "Włóczykij", "Wytrwały"]
talenty2 = ["Bardzo Silny", "Mocne Plecy", "Silny Cios", "Widzenie w Ciemności"]
talenty3 = ["Cios Mierzony", "Szczur Tunelowy", "Wytwórca (Materiały Wybuchowe)", "Złota Rączka"]
talenty4 = ["Czytanie/Pisanie", "Defraudant", "Odporność Psychiczna", "Przekonujący"]

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



wyp1 = ["kiepska mapa", "metalowa miska albo patelnia", "szpadel", "węgiel do rysowania"]
wyp2 = ["broń ręczna (kilof)", "lampa Davricha", "lampa oliwna", "skórzana kurta"]
wyp3 = ["hełm", "narzędzia pracy (Inżyniera)", "wielka broń (dwuręczny kilof)"]
wyp4 = ["brygada Górników", "zestaw do pisania"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]


profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)
