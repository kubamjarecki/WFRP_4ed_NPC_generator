import random

klasa = "Wodniacy"

nazwa_profesji = {
    0 : "Rybak",
    1 : "Rybak",
    2 : "Flisak",
    3 : "Znawca Rzeki",
    4 : "Starszy Rzeczny"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Brąz",
    4 : "Srebro"
}

rozwiniecia_cech = {
    "Wt": 0,
    "Zw": 0,
    "Zr" : 0,
    "WW" : -1,
    "I" : -2,
    "Ogd" : -3,
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
waga = ["WW", "Wt", "Zw", "I", "Ogd", "S", "Zr", "Int", "SW",  "US", ]
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

umiejkip= ["Atletyka (Zw)", "Mocna Głowa (Wt)", "Odporność (Wt)", "Plotkowanie (Ogd),Pływanie (S)", "Sztuka Przetrwania (Int)", "Unik (Zw)", "Wioślarstwo (S)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Broń Zasięgowa (US) (Miotana)", "Broń Zasięgowa (US) (Oplątująca)", "Hazard (Int)", "Wiedza (Int) (Lokalna)", "Wiedza (Int) (Szlaki Rzeczne)", "Zastawianie Pułapek (Zr)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Broń Biała (WW) (Drzewcowa)", "Intuicja (I)", "Percepcja (I)", "Charyzma (Ogd)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Wiedza (Int) (Ludowa)", "Występy (Ogd) (Gawędziarstwo)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Świetny Pływak"]
talenty1 = ["Doświadczony Wędrowiec (Bagna)", "Rybak",  "Towarzyski"]
talenty2 = ["Mocne Plecy", "Włóczykij", "Wodniak", "Wytwórca (Szkutnik)"]
talenty3 = ["Bardzo Silny", "Waleczne Serce", "Wytrwały", "Znawca (Szlaki Rzeczne)"]
talenty4 = ["Czujny", "Odporność Psychiczna", "Mistrz Rzemiosła (Szkutnictwo)", "Mówca"]

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



wyp1 = ["skórzane nogawice", "wiadro", "wędka z przynętą"]
wyp2 = ["pułapka na węgorze", "skórzany kaftan", "sieć", "włócznia"]
wyp3 = ["lampa sztormowa z oliwą", "łódź wiosłowa"]
wyp4 = ["chata lub szkuta"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)