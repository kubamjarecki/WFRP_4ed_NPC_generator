import random

klasa = "Uczeni"

nazwa_profesji = {
    0 : "Uczeń Czarodzieja",
    1 : "Uczeń Czarodzieja",
    2 : "Czarodziej",
    3 : "Mistrz Magii",
    4 : "Arcymag"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Srebro",
    3 : "Złoto",
    4 : "Złoto"
}

rozwiniecia_cech = {
    "WW": 0,
    "Int": 0,
    "SW" : 0,
    "Zw" : -1,
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
        return "Aptekarz"
    
    


#losujemy rzutyi ustawiamy je według porządku jak co jest ważne  fff
waga = ["Int", "SW", "WW", "Zw", "I", "Ogd", "S", "Wt", "US", "Zr" ]
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

umiejkip= ["Broń Biała (WW) (Podstawowa)", "Broń Biała (WW) (Drzewcowa)", "Intuicja (I)", "Język (Int) (Magiczny)", "Percepcja (I)", "Splatanie Magii (SW) (Dowolny Kolor)", "Unik (Zw)", "Wiedza (Int) (Magia)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Umiejętności: Charyzma (Ogd) ", "Język (Int) (Bitewny)", "Język (Int) (Dowolny)", "Opanowanie (SW)", "Plotkowanie (Ogd)", "Zastraszanie (S)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Jeździectwo (Zw)  (Konie)", "Opieka nad Zwierzętami (Int)", "Wiedza (Int) (Wojna)", "Wycena (Int)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Język (Int) (Dowolny)", "Wiedza (Int) (Dowolna)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = [ "Magia Prosta"]
talenty1 = ["Czytanie/Pisanie", "Percepcja Magiczna", "Zmysł Magii"]
talenty2 = ["Magia Tajemna (Dowolna Tradycja)", "Rozpoznanie", "Artefaktu", "Ruchliwe Dłonie", "Szósty Zmysł"]
talenty3 = ["Dwie Bronie", "Groźny", "Precyzyjne Inkantowanie", "Wykrywanie Magii"]
talenty4 = [ "Mag Bitewny", "Straszny", "Zmysł Bitewny", "Żelazna Wola"]

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



wyp1 = ["kostur", "Księga Zaklęć"]
wyp2 = ["licencja na Uprawianie Magii"]
wyp3 = ["lekki koń bojowy", "przedmiot magiczny", "Uczeń"]
wyp4 = ["biblioteka (Magia)", "Uczeń", "warsztat (Magia)"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)

# print(profes.cechy)
# print(profes.talenty)
# print(profes.umiejki)
# print(profes.wyposazenie)

#print(profes)