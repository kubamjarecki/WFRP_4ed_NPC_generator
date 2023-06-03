import random

klasa = "Mieszczanie"

nazwa_profesji = {
    0 : "Uczeń Szczurołapa",
    1 : "Uczeń Szczurołapa",
    2 : "Szczurołap",
    3 : "Strażnik Kanałów",
    4 : "Tępiciel"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Srebro",
    3 : "Srebro",
    4 : "Srebro"
}

rozwiniecia_cech = {
    "WW": 0,
    "US": 0,
    "SW" : 0,
    "Wt" : -1,
    "I" : -2,
    "S" : -3,
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
waga = ["WW", "US", "Wt","S", "I", "SW", "Zw", "Ogd", "Int", "Zr",]
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

umiejkip= ["Atletyka (Zw)", "Tresura (Int) (Psy)", "Oswajanie (SW)", "Mocna Głowa (Wt)", "Odporność (Wt)", "Broń Biała (WW) (Podstawowa)", "Broń Zasięgowa (US)(Proca)", "Skradanie (Zw) (Miasto albo Podziemia)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1
    
umiejkip= ["Opieka nad Zwierzętami (Int)", "Percepcja (I)", "Plotkowanie (Ogd)", "Targowanie (Ogd)", "Wiedza (Int) (Trucizny)", "Zastawianie Pułapek (Zr)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Broń Zasięgowa (US) (Kusza Pistoletowa)", "Opanowanie (SW)", "Unik (Zw)", "Wspinaczka (S)"]

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Dowodzenie (Ogd)", "Tropienie (I)"]
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Widzenie w Ciemności"]
talenty1 = ["Odporny na (Choroby)", "Ogłuszenie", "Silny Cios"]
talenty2 = ["Etykieta (Członkowie Cechu)", "Nieustraszony (Szczury)", "Niezwykle odporny", "Walka w Ciasnocie"]
talenty3 = ["Silne Nogi", "Szczur Kanałowy", "Twardziel", "Waleczne Serce"]
talenty4 = ["Groźny", "Krzepki", "Odporność Psychiczna", "Nieustraszony (Skaveny)"]

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



wyp1 = ["mały, ale zajadły pies", "proca z amunicją", "worek"]
wyp2 = ["sidła na zwierzęta", "drąg na martwe szczury"]
wyp3 = ["lampa Davricha", "broń ręczna", "skórzana kurta"]
wyp4 = ["Asystent", "duży i zajadły pies", "worek zatrutej przynęty (10 Porcji Sercoboju)"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)