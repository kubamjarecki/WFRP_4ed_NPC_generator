
"""
        Aptekarze specjalizują się w przygotowywaniu leków – zazwyczaj pastylek,
        mikstur i maści, które sprzedają zarówno pacjentom, jak i lekarzom.
        Ich pracownie wypełniają oszałamiające instalacje buzujących
        alembików, przelewających się próbówek, zużytych moździerzy z tłuczkami
        oraz innych aptekarskich utensyliów. Niektórzy Aptekarze dorabiają
        sobie, sprzedając niedozwolone substancje – od stymulantów
        dla zdesperowanych studentów po halucynogenny dziwnokorzeń dla
        znudzonych szlachciców, nie mówiąc o podejrzanych zamówieniach dla
        jeszcze bardziej podejrzanych klientów. Sprzedaż tych specyfików jest
        lukratywna, ale także niebezpieczna. Rzadkie składniki dużo kosztują,
        dlatego Aptekarze często mają problemy z płynnością finansową i podróżują
        na bezdroża, by samodzielnie zbierać składniki. Dla dodatkowego
        zarobku wielu z nich podejmuje tymczasową pracę i dołącza do
        wypraw, najemników lub wojska.
        """
import random

klasa = "Uczeni"

status = {
    0 : "Brąz",
    1 : "Srebro",
    2 : "Srebro",
    3 : "Złoto",
    4 : "Złoto"
}
nazwa_profesji = {
    0 : "Uczeń Aptekarza",
    1 : "Uczeń Aptekarza",
    2 : "Aptekarz",
    3 : "Farmaceuta",
    4 : "Mistrz Aptekarstwa"
}
rozwiniecia_cech = {
    "Wt": 0,
    "Zr": 0,
    "Int" : 0,
    "Ogd" : -1,
    "I" : -2,
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
        return "Aptekarz"
    
    


#losujemy rzutyi ustawiamy je według porządku jak co jest ważne  fff
waga = ["Int", "Zr", "Wt", "SW", "I", "Ogd", "US", "Zw", "S", "WW" ]
rzuty = []
a = 10
while a>0:
     b = random.randint(1,10) + random.randint(1,10) 
     rzuty.append(b)
     a = a -1
    
    
slownik_cech_i_rzutow_w_kolejnosci_wagi = {}
rzuty.sort()
rzuty.reverse()

a = 0
while a<10:
    slownik_cech_i_rzutow_w_kolejnosci_wagi[waga[a]]=rzuty[a]
    a = a + 1


#budujemy słownik z umiejętności. Ich wartości będą wynosić od -2 na najwyższym tierze, do 0 na najniższym. Następnie 
# dodamy tier jaką mam mieć postać (od 0, do 4)

umiejkip= ["Język (Int) (Klasyczny)", "Leczenie (Int)", "Mocna Głowa (Wt)", "Rzemiosło (Zr) (Aptekarstwo)", "Rzemiosło (Zr) (Truciciel)", "Wiedza (Int) (Chemia)", "Wiedza (Int) (Medycyna)", "Wiedza (Int) (Rośliny)"]

slownik_umiejetnosci_oraz_levelu = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 1

umiejkip= ["Charyzma (Ogd) ", "Język (Int) (Gildii)", "Percepcja (I)", "Plotkowanie (Ogd)", "Targowanie (Ogd)", "Wiedza (Int) (Nauka)"]


for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = 0
    
umiejkip= ["Badania Naukowe (Int)", "Dowodzenie (Ogd)", "Intuicja (I)", "Sekretne Znaki (Int) (Cechu)"]

   # umiejkip2 = {}

for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -1
    
umiejkip= ["Jeździectwo (Zw)  (Konie)", "Zastraszanie (S)"]

    #umiejkip3 = {}
for um in umiejkip:
    if um in slownik_umiejetnosci_oraz_levelu:
        um = um + " "
    slownik_umiejetnosci_oraz_levelu[um] = -2


talenty = []

talenty0 = ["Czytanie/Pisanie"]
talenty1 = ["Etykieta (Uczeni)", "Przyrządzanie", "Mikstur", "Wytwórca (Aptekarz)"]
talenty2 = ["Aptekarz", "Etykieta (Członkowie Cechu)", "Przestępca", "Żyłka Handlowa"]
talenty3 = ["Błyskotliwość", "Mistrz Rzemiosła (Aptekarz)", "Mól Książkowy", "Odporny na (Trucizny)"]
talenty4 = ["Mistrz Rzemiosła (Truciciel)", "Wyczulony Zmysł (Smak)", "Zimna Krew", "Znawca (Aptekarstwo)"]

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



wyp1 = ["księga (pusta)", "mikstura lecznicza", "moździerz z tłuczkiem", "skórzany kaftan"]
wyp2 = ["licencja Cechu Aptekarzy", "narzędzia pracy(Aptekarza)"]
wyp3 = ["książka (aptekarstwo)", "Uczeń", "warsztat"]
wyp4 = ["duży warsztat", "przywilej od władcy"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(slownik_cech_i_rzutow_w_kolejnosci_wagi, slownik_umiejetnosci_oraz_levelu, talenty, wyp, rozwiniecia_cech)

