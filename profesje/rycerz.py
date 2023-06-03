import random

klasa = "Wojownicy"

rozwiniecia_cech = {
    "S": 0,
    "I": 0,
    "Zw" : 0,
    "WW" : -1,
    "SW" : -2,
    "Ogd" : -3,
}

waga = ["WW",  "Zw", "I", "S", "Ogd", "Wt", "Int", "SW", "US", "Zr"]

nazwa_profesji = {
    0 : "Giermek",
    1 : "Giermek",
    2 : "Rycerz",
    3 : "Pierwszy Rycerz",
    4 : "Rycerz Wewnętrznego Kręgu"
}
status = {
    0 : "Srebro",
    1 : "Srebro",
    2 : "Srebro",
    3 : "Złoto",
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

umiejkip= ["Atletyka (Zw)", "Broń Biała (WW) (Kawaleryjska)", "Jeździectwo (Zw) (Konie)", "Leczenie (Int)", "Opieka nad Zwierzętami (Int)", "Oswajanie (SW)", "Rzemiosło (Zr) (Podkuwanie Koni)", "Wiedza (Int) (Heraldyka)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
    
umiejkip= ["Broń Biała (WW) (Dowolna)", "Język (Int) (Bitewny)", "Odporność (Wt)", "Opanowanie (SW)", "Unik (Zw)", "Zastraszanie (S)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Charyzma (Ogd) ", "Mocna Głowa (Wt)", "Dowodzenie (Ogd)", "Wiedza (Int) (Sztuka (Zr) Wojenna)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Sekretne Znaki (Int) (Zakonu Rycerskiego)", "Wiedza (Int) (Dowolna)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Urodzony w Siodle"]
talenty1 = ["Etykieta (Dowolna Grupa)", "Tragarz", "Urodzony Wojownik"]
talenty2 = ["Groźny", "Obieżyświat", "Silny Cios", "Tarczownik"]
talenty3 = ["Niewzruszony", "Nieustraszony (Dowolny)", "Waleczne Serce", "Wódz"]
talenty4 = ["Inspirujący", "Morderczy Atak", "Rozbrojenie", "Żelazna Wola"]

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



wyp1 = ["kaftan kolczy", "koń wierzchowy z rzędem", "narzędzia pracy (Podkuwanie Koni)", "skórzana kurta", "tarcza"]
wyp2 = ["Broń Biała (WW) (Dowolna)", "kopia", "rumak z siodłem i uprzężą", "zbroja płytowa z hełmem"]
wyp3 = ["kropierz", "mały oddział Rycerzy"]
wyp4 = ["Giermek", "pełny hełm z pióropuszem", "duży oddział lub kilka małych oddziałów Rycerzy"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]


profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)