import random

klasa = "Pospólstwo"

rozwiniecia_cech = {
    "I": 0,
    "Wt": 0,
    "Zr" : 0,
    "Int" : -1,
    "Ogd" : -2,
    "SW" : -3,
}

waga = ["Int", "SW", "Wt", "Ogd", "I",  "Zw",  "Zr",  "WW", "S","US"]

nazwa_profesji = {
    0 : "Uczeń Guślarza",
    1 : "Uczeń Guślarza",
    2 : "Guślarz",
    3 : "Starszy Guślarzy",
    4 : "Wiedzący "
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Brąz",
    4 : "Brąz"
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

umiejkip= ["Intuicja (I)", "Język (Int) (Magiczny)", "Odporność (Wt)", "Percepcja (I)", "Splatanie Magii (SW)", "Sztuka Przetrwania (Int)", "Wiedza (Int) (Ludowa)", "Wiedza (Int) (Zioła)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Opanowanie (SW)", "Plotkowanie (Ogd)", "Leczenie (Int)", "Wiedza (Int) (Lokalna)", "Rzemiosło (Zr) (Amulety)", "Rzemiosło (Zr) (Zielarz)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Targowanie (Ogd)", "Wiedza (Int) (Duchy)", "Wiedza (Int) (Genealogia)", "Wiedza (Int) (Magia)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Umiejętności: Modlitwa (Ogd)", "Zastraszanie (S)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Magia Prosta"]
talenty1 = ["Doświadczony Wędrowiec (Lasy)", "Ruchliwe Dłonie", "Włóczykij"]
talenty2 = ["Magia Tajemna (Guślarstwo)", "Posłuch u Zwierząt", "Szósty Zmysł", "Zmysł Magii"]
talenty3 = ["Czysta Dusza", "Odporny na (Choroby)", "Wykrywanie Magii", "Wytwórca (Zielarz)"]
talenty4 = ["Mistrz Rzemiosła (Zielarz)", "Odporność Psychiczna", "Widzenie w Ciemności", "Wyczulony Zmysł (Dowolny)"]

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



wyp1 = ["kostur", "plecak", "1k10 amuletów na szczęście"]
wyp2 = ["kataplazm leczniczy", "narzędzia pracy (Zielarza)", "zestaw do leczenia zatruć"]
wyp3 = ["odosobniona chata", "Uczeń"]
wyp4 = ["ceremonialny płaszcz z wiankiem", "zbiór zwierzęcych czaszek"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]


profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)
