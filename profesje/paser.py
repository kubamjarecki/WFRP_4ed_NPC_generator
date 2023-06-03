import random

klasa = "Łotrzy"

nazwa_profesji = {
    0 : "Pośrednik",
    1 : "Pośrednik",
    2 : "Paser",
    3 : "Mistrz Paserów",
    4 : "Broker Informacji"
}
status = {
    0 : "Srebro",
    1 : "Srebro",
    2 : "Srebro",
    3 : "Srebro",
    4 : "Srebro"

}

"Brąz", "Srebro", "Złoto"
rozwiniecia_cech = {
    "Zw": 0,
    "I": 0,
    "Ogd" : 0,
    "Zr" : -1,
    "Int" : -2,
    "SW" : -3,
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
waga = [ "Ogd", "Int", "SW", "Zr", "I", "Zw", "WW", "S", "Wt", "US"]
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

umiejkip= ["Broń Biała (WW) (Podstawowa)", "Charyzma (Ogd) ", "Hazard (Int)", "Mocna Głowa (Wt)", "Plotkowanie (Ogd)", "Targowanie (Ogd)", "Unik (Zw)", "Wycena (Int)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Intuicja (I)", "Opanowanie (SW)", "Percepcja (I)", "Rzemiosło (Zr)(Grawer)", "Sekretne Znaki (Int) (Złodziei)", "Zastraszanie (S)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Przekupstwo (Ogd)", "Wiedza (Int) (Lokalna)", "Wiedza (Int) (Sztuka (Zr))", "Występy (Ogd) (Gawędziarstwo)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Badania Naukowe (Int)", "Wiedza (Int) (Heraldyka)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Żyłka Handlowa"]
talenty1 = ["Szuler", "Towarzyski", "Ulicznik"]
talenty2 = ["Błyskotliwość", "Etykieta (Przestępcy)", "Numizmatyka", "Przestępca"]
talenty3 = ["Charyzmatyczny", "Geniusz Arytmetyczny", "Ogłuszenie", "Szycha"]
talenty4 = ["Cios Poniżej Pasa", "Groźny", "Łapówkarz", "Żelazna Wola"]

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



wyp1 = ["broń ręczna", "skradzione dobra warte 3k10 szylingów"]
wyp2 = ["monokl", "narzędzia pracy (Grawera)", "zestaw do pisania"]
wyp3 = ["lombard"]
wyp4 = ["Cios Poniżej Pasa", "Groźny", "Łapówkarz", "Żelazna Wola"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)