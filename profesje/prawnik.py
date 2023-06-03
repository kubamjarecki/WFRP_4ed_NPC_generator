import random

klasa = "Uczeni"

nazwa_profesji = {
    0 : "Student Prawa",
    1 : "Student Prawa",
    2 : "Prawnik ",
    3 : "Obrońca ",
    4 : "Sędzia "
}
status = {
    0 : "Brąz",
    1 : "Brąz ",
    2 : "Srebro",
    3 : "Złoto",
    4 : "Złoto"
}

rozwiniecia_cech = {
    "Int": 0,
    "I": 0,
    "Zr" : 0,
    "Ogd" : -1,
    "SW" : -2,
    "Wt" : -3,
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
        

#losujemy rzutyi ustawiamy je według porządku jak co jest ważne  fff
waga = ["Int", "Ogd", "SW", "Zr", "I","Wt", "Zw", "S", "WW", "US", ]
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

umiejkip= ["Badania Naukowe (Int)", "Język (Int) (Klasyczny)", "Mocna Głowa (Wt)", "Odporność (Wt)", "Percepcja (I)", "Targowanie (Ogd)", "Wiedza (Int) (Prawo)", "Wiedza (Int) (Teologia)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Przekupstwo (Ogd)", "Charyzma (Ogd) ", "Plotkowanie (Ogd)", "Intuicja (I)", "Język (Int) (Gildii)", "Sekretne Znaki (Int) (Gildii)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Sztuka (Zr) (Pisarstwo)", "Wiedza (Int)(Dowolna)", "Występy (Ogd) (Przemowy)", "Zastraszanie (S)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Opanowanie (SW)", "Wiedza (Int) (Polityka)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Czytanie/Pisanie"]
talenty1 = ["Etykieta (Uczeni)", "Gadanina", "Szybkie Czytanie"]
talenty2 = ["Charyzmatyczny", "Etykieta(Członkowie Gildii)", "Przekonujący", "Przestępca"]
talenty3 = ["Błyskotliwość", "Gładkie Słówka", "Mól Książkowy", "Porywająca Gorliwość"]
talenty4 = ["Majętny", "Szycha", "Władcza Postura", "Znawca (Prawo)"]

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



wyp1 = ["księga (Prawo)", "lupa"]
wyp2 = ["licencja Gildii", "szaty dworskie", "zestaw do pisania"]
wyp3 = ["kantor", "Asystent (Student lub Służący)"]
wyp4 = ["młotek Sędziego", "pretensjonalna peruka"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)