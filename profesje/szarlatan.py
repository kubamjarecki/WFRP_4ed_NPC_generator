import random

klasa = "Łotrzy"

nazwa_profesji = {
    0 : "Kanciarz",
    1 : "Kanciarz",
    2 : "Szarlatan ",
    3 : "Oszust ",
    4 : "Łajdak "
}
   
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Srebro",
    4 : "Srebro"

}

"Brąz", "Srebro", "Złoto"
rozwiniecia_cech = {
    "Ogd": 0,
    "I": 0,
    "Zr" : 0,
    "SW" : -1,
    "Zw" : -2,
    "Int" : -3,
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
waga = ["Ogd", "I", "Zr",  "SW", "Zw", "Int", "WW", "S", "Wt", "US", ]
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

umiejkip= ["Charyzma (Ogd) ", "Hazard (Int)", "Mocna Głowa (Wt)", "Plotkowanie (Ogd)", "Przekupstwo (Ogd)", "Targowanie (Ogd)", "Występy (Ogd) (Gawędziarstwo)", "Zwinne Palce (Zr)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Intuicja (I)", "Opanowanie (SW)", "Percepcja (I)", "Unik (Zw)", "Wycena (Int)", "Występy (Ogd) (Aktorstwo)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Język (Int) (Grypsera)", "Wiedza (Int) (Heraldyka)", "Otwieranie Zamków (Zr)", "Sekretne Znaki (Int) (Złodziei)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Badania Naukowe (Int)", "Wiedza (Int) (Genealogia)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Szczęście"]
talenty1 = ["Etykieta (Dowolna Grupa)",  "Szuler", "Szuler Kościany"]
talenty2 = ["Gadanina", "Przestępca", "Ruchliwe Dłonie", "Sekretna Tożsamość"]
talenty3 = ["Język (Int) (Grypsera)", "Wiedza (Int) (Heraldyka)", "Otwieranie Zamków (Zr)", "Sekretne Znaki (Int) (Złodziei)"]
talenty4 = ["Charyzmatyczny", "Mistrz Charakteryzacji", "Nos do Kłopotów", "Towarzyski"]

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



wyp1 = ["plecak", "talia kart", "zestaw kości", "2 komplety ubrań"]
wyp2 = ["1 sfałszowany dokument", "2 komplety ubrań dobrej jakości", "wybór kolorowych proszków i płynów", "wybór błyskotek i amuletów"]
wyp3 = ["zestaw do charakteryzacji", "wytrychy", "liczne sfałszowane dokumenty"]
wyp4 = ["podrobiona pieczęć", "zestaw do pisania"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)