import random

klasa = "Pospólstwo"

rozwiniecia_cech = {
    "Wt": 0,
    "I": 0,
    "Zw" : 0,
    "Zr" : -1,
    "Ogd" : -2,
    "Int" : -3,
}

waga = ["I",  "Wt", "Int", "Zw", "Ogd", "S", "SW", "US", "WW",  "Zr" ]

nazwa_profesji = {
    0 : "Zbieracz Ziół",
    1 : "Zbieracz Ziół",
    2 : "Zielarz",
    3 : "Mistrz Ziołolecznictwa",
    4 : "Arcyzielarz"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Srebro",
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

umiejkip= ["Odporność (Wt)", "Oswajanie (SW)", "Percepcja (I)", "Pływanie (S)", "Rzemiosło (Zr) (Zielarz)", "Sztuka Przetrwania (Int)", "Wiedza (Int) (Zioła)", "Wspinaczka (S)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Leczenie (Int)", "Mocna Głowa (Wt)", "Opanowanie (SW)", "Plotkowanie (Ogd)", "Targowanie (Ogd)", "Wiedza (Int) (Lokalna)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Dowodzenie (Ogd)", "Intuicja (I)", "Rzemiosło (Zr) (Trucizny)", "Wiedza (Int) (Medycyna)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Powożenie (Zw)", "Nawigacja (I)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Doświadczony Wędrowiec (Dowolny Teren)"]
talenty1 = ["Włóczykij", "Wyczucie Kierunku", "Wyczulony Zmysł (Smak)"]
talenty2 = ["Czujny", "Tragarz", "Zręczne Palce", "Żyłka Handlowa"]
talenty3 = ["Błyskotliwość", "Pierwsza Pomoc", "Twardziel", "Wytwórca (Zielarz)"]
talenty4 = ["Mistrz Rzemiosła (Zielarstwo)", "Odporny na (Trucizny)", "Przyrządzanie Mikstur"]

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



wyp1 = ["buty", "płaszcz", "torba na ramię zawierająca wybór ziół"]
wyp2 = ["broń ręczna (Sierp)", "kataplazm leczniczy", "narzędzia pracy (Zielarza)"]
wyp3 = ["mikstura lecznicza", "warsztat (Zielarza)", "Zbieracz Ziół", "3 kataplazmy lecznicze"]
wyp4 = ["wóz z kucem"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]


profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)
