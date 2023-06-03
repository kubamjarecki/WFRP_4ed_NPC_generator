
import random

profesje = {
    1: 'Aptekarz', 2: 'Czarodziej', 3: 'Inżynier', 4: 'Kapłan', 5: 'Kapłan', 6: 'Kapłan', 7: 'Kapłan',
    8: 'Kapłan', 9: 'Medyk', 10: 'Mnich', 11: 'Mnich', 12: 'Prawnik', 13: 'Uczony', 14: 'Uczony',
    15: 'Agitator', 16: 'Kupiec', 17: 'Mieszczanin', 18: 'Mieszczanin', 19: 'Mieszczanin',
    20: 'Rzemieślnik', 21: 'Rzemieślnik', 22: 'Strażnik', 23: 'Szczurołap', 24: 'Szczurołap', 25: 'Śledczy',
    26: 'Żebrak', 27: 'Żebrak', 28: 'Artysta', 29: 'Doradca', 30: 'Namiestnik', 31: 'Poseł', 32: 'Służący',
    33: 'Służący', 34: 'Służący', 35: 'Szlachcic', 36: 'Szpieg', 37: 'Zwadźca', 38: 'Chłop', 39: 'Chłop',
    40: 'Chłop', 41: 'Chłop', 42: 'Chłop', 43: 'Górnik', 44: 'Guślarz', 45: 'Łowca', 46: 'Łowca',
    47: 'Mistyk', 48: 'Zarządca', 49: 'Zielarz', 50: 'Zwiadowca', 51: 'Biczownik', 52: 'Biczownik',
    53: 'Domokrążca', 54: 'Kuglarz', 55: 'Kuglarz', 56: 'Łowca Czarownic', 57: 'Łowca Nagród',
    58: 'Posłaniec', 59: 'Strażnik Dróg', 60: 'Woźnica', 61: 'Doker', 62: 'Doker', 63: 'Flisak',
    64: 'Flisak', 65: 'Flisak', 66: 'Pilot Rzeczny', 67: 'Pirat Rzeczny', 68: 'Przemytnik',
    69: 'Przewoźnik', 70: 'Przewoźnik', 71: 'Strażnik Rzeczny', 72: 'Strażnik Rzeczny', 73: 'Żeglarz',
    74: 'Żeglarz', 75: 'Banita', 76: 'Banita', 77: 'Banita', 78: 'Banita', 79: 'Czarownica', 80: 'Paser',
    81: 'Hiena Cmentarna', 82: 'Rajfur', 83: 'Rajfur', 84: 'Rekietier', 85: 'Szarlatan', 86: 'Złodziej',
    87: 'Złodziej', 88: 'Złodziej', 89: 'Gladiator', 90: 'Kapłan Bitewny', 91: 'Kawalerzysta',
    92: 'Kawalerzysta', 93: 'Ochroniarz', 94: 'Ochroniarz', 95: 'Oprych', 96: 'Rycerz', 97: 'Żołnierz',
    98: 'Żołnierz', 99: 'Żołnierz', 100: 'Żołnierz'}

cechy= {
    "WW" : 20,
    "US" : 20, 
    "S" : 20,
    "Wt" : 20,
    "I" : 20,
    "Zw" : 20,
    "Zr" : 20,
    "Int" : 20,
    "SW" : 20,
    "Ogd" : 20,
}

szybkosc = 4
punkty_bohatera0 = 1
punkty_przeznaczenia0 = 2
punkty_wolne = 3

talenty2 = [ " Błyskotliwość", "Charyzmatyczny"]
umiejki= [ "Broń Biała (WW) (Podstawowa)", "Broń Zasięgowa (US) (Łuk)", "Charyzma (Ogd) ", "Dowodzenie (Ogd)", "Język (Int) (bretoński)", "Język (Int) (Jałowej Krainy)", "Opanowanie (SW)", "Opieka nad Zwierzętami (Int)", "Plotkowanie (Ogd)", "Targowanie (Ogd)", "Wiedza (Int) (Reikland)", "Wycena (Int)"]

talentyx = [talenty2, 3]

wzrost = [150, 4]
im_m = ["Adhemar", "Anders", "Artur", "Beatrijs", "Clementia", "Detlev", "Frederich", "Gerner", "Gertraud", "Haletha", "Heinrich", "Henryk", "Karl", "Kruger", "Marieke", "Sebastien", "Talther", "Talunda", "Ulrich", "Werther", "Wilryn", "Adelbert", "Adolf", "Adolphus", "Albert", "Albrecht", "Adhelm", "Alex", "Alexei", "Alfred", "Alfricht", "Anders", "Andreas", "Anton,", "Arthur", "Axel", "Barthelm", "BengtS", "Bernhard", "Berthold", "Bogoslav", "Boris", "Bruno", "Carolus", "Karl", "Klaus", "Konrad", "Diehl", "Dieter", "Dietrich", "Eberhard,", "Eckhard", "Edgar", "Ehrhard", "Ehrmann", "Emmerich", "Erich", "Ernst", "Erwin", "Faustmann", "Felix", "Ferdinand", "Franz", "Friedrich", "Fritz", "Frederik", "Gebhard", "Georg", "Gerhard", "Gottfried", "Gotthard", "Gottlieb", "Gregor", "Gunnar", "Gunther", "Gustav", "Gustavus", "Hals", "Hannes", "Hans", "Hartwig", "Heinrich", "Heinz", "Hieronymus", "Helmut", "Hergard", "Herman", "Herpin", "Hildebrand", "HolgerS", "Hugo", "Hultz", "Humfried", "Jakob", "Joachim", "Johann", "Johannes", "Josef", "Kaspar", "Kastor", "KnnudS", "Kurt", "Lorenz", "Leonard", "Luitpold", "Ludovicus", "Ludwig", "Lukas", "Magnus", "Mannfred", "Mannricht", "Mannsfried", "Mannslieb", "Martin", "Matthias", "Maximillian", "Melched", "Moritz", "Nikolas", "Nikolaus", "OlafS", "Oskar", "Otto", "Paul", "Paulus", "Peter", "Pieter", "Quintus", "Ralf", "Randolf", "Ranelf", "Rannalt", "RolfS", "Reinald", "Reiner", "Reinhard", "Reinhold", "Reinwald", "Rudiger", "Rutger", "Rudolf", "Ruprecht", "Seiger", "Siegfried", "Sigismund", "Sigmund", "Stehmar", "Stephan", "Talecht", "Thedosius", "Theopilius", "Thomas", "Tobias", "Udo", "Uhler", "Ulfred", "Ulli", "Ulrich", "Ulrict", "Viktor", "Vorster", "Waldemar", "Walter", "Werner", "Wilhelm", "Wolf", "Wolfgang", "Wolmar"]
im_z = ["Erika", "Frauke", "Helga", "Irmina", "Jehanne", "Lorelay", "Ulrika", "Willelma", "Sigfreda", "Willelma", " Maria", "Emma", "Emilia", "Mia", "Anna", "Hanna", "Johanna", "Agnes", "Agnetha", "Alexa", "Alfrida", "Alice", "Amalie", "Andrea", "Anika", "Anna", "AstridS", "Barbara", "Beatrix", "Bertha", "Bianka", "Birgit", "Bogoslava", "Brigitte", "Brita", "Brunhild", "Charlotte", "Carina", "Carmilla", "Claudia", "Dagmar", "Elena", "Elfrida", "Elisabeth", "Elsa", "Emmanuelle", "Emilie", "Erika", "Esther", "Etelka", "Eva", "Franziska", "Gabrielle", "Gerda", "Gertrud", "Gilda", "Greta", "Gretel", "Gretchen", "Hanna", "Hannath", "Hedwig", "Heidi", "Helena", "Hilda", "Hildegard", "Hunni", "Ilsa", "Ilse", "Inga", "IngridS", "Irene", "Irina", "Isolde", "Johanna", "Janna", "Juliane", "Karelia", "Karin", "Karoline", "Katharine", "Katrina", "KristenS", "Klara", "Leonore", "Ludmilla", "Luise", "Lise", "Magdalene", "Magda", "Margaritha", "Marianne", "Marlene", "Marthe", "Marte", "Martina", "Marie", "Mathilde", "Tilda", "Natasha", "Ottilia", "Petra", "Regina", "Renata", "Renate", "Selena", "Sigismunda", "Sigrid", "Sigrun", "Sigunda", "Solma", "SolveigS", "Sophia", "Susanne", "Talima,. Thedora", "Theodosia", "Theda", "Therese", "Thylda", "Ulrica", "Ulrike", "Ulla", "Ursula", "Veronica", "Wanda", "Wertha", "Wilhemina", "Wolfhilda"]

nazwisko = ["Müller", "Schneider", "Fischer", "Weber", "Meier", "Wagner", "Bäcker", "Hofmann", "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schwarz", "Zimmermann", "Braun", "Lange", "Fuchs", "Kaiser", "König", "Krause", "Köhler", "Schuhmacher", "Schmidt", "Beinbruch", "Bendow", "Bennefeld", "Bennefeldt", "Berger", "Bergmann", "Bernecker", "Bildt", "Braun", "Breitner", "Breull", "Bruckner", "Backer", "Dessau", "Dietz", "Dreschel", "Drucker", "Dudenbostel", "Dunkelberg", "Eberhauer", "Eckhard", "Eichheim", "Engelhart", "Engelmann", "Errlich", "Faustmann", "Finck", "Flaschmann", "Fleischer", "Flick", "Fraunhofer", "Fredersdorff", "Ganghofer", "Gebiihr", "Geldrecht", "Geller", "Genscher", "Gerber", "Gesner", "Goebbels", "Goffmann", "Gruber", "Griin", "Griinberg", "Gunzenhauser", "Hackenbusch", "Haffenheim", "Haffmeister", "Hannicke", "Hardenberg", "Hartmann", "Haufmann", "Heilborn", "Heising", "Hellbach", "Herrscher", "Heschendorf", "Heuser", "Hindenburg", "Hockmann", "Hohenberg", "Holstweig", "Hostettler", "Huber", "Hubergreiber", "Hollmer", "Horbiger", "Immelmann", "Junkermann", "Jager", "Kerzer", "Kessler", "Kesselmann", "Kesselring", "Kiefern", "Kirchner", "Kleemann", "Kleist", "Kleiter", "Klipstein", "Korff", "Krause", "Kreutzmann", "Kriiger", "Kunz", "Kupfer", "Kurz", "Korbitz", "Koster", "Lepr", "Leibelt", "Lentz", "Leonhardt", "Liebeneiner", "Liebowitz", "Lindenlaub", "Lizt", "Lohrentzen", "Luchter", "Meyer", "Meinhard", "Meissen", "Merkwiirdigliebe", "Mierendorff", "Miiller", "Nordberg", "Osterwald", "Platen", "Prasch", "Prunkvoll", "Pollnitz", "Rabenfels", "Regelsberg", "Reitsmann", "Retzer", "Richsteiger", "Riedmann", "Rosenkrantz", "Rupp", "Schatzenheimer", "Schicklgruber", "Schiller", "Schimmel", "Schlichter", "Schlichtkrull", "Schmidhuber", "Schmidt", "Schmiedehammer", "Schneider", "Schroder", "Schumacher", "Schutzmann", "Schwarz", "Schwarzberg", "Schwarzkopf", "Schwensen", "Schiinzel", "Schon", "Seefeldt", "Seydlitz", "Sonnefeld", "Stadtmiiller", "Steiger", "Stein", "Steinbocka", "Steinmeyer", "Sternheimer", "Stiefel", "Streckmann", "Stiiwe", "Vespermann", "Vogel", "Voller", "Wagner", "Wassmeier", "Geissbach"]

rand_im = random.randint(0, (len(im_m))-1)
rand_iz = random.randint(0, (len(im_z))-1)
rand_naz = random.randint(0, (len(nazwisko))-1)

imiex_m = im_m[rand_im] + " " + nazwisko[rand_naz]
imiex_z = im_z[rand_iz] + " " + nazwisko[rand_naz]

wlosy = { 1: 'Biały', 2: 'Złoty blond', 3: 'Rudoblond', 4: 'Złoty', 5: 'Złoty', 6: 'Złoty', 7: 'Jasny brąz', 8: 'Jasny brąz', 9: 'Jasny brąz', 10: 'Kasztanowy', 11: 'Ciemny brąz', 12: 'Ciemny brąz', 13: 'Ciemny brąz', 14: 'Czarny', 15: 'Czarny', 16: 'Czarny', 17: 'Kasztanowy', 18: 'Rudy', 19: 'Siwy'}

oczy = {1: 'Zielony', 2: 'Błękitny', 3: 'Niebieski', 4: 'Niebieski', 5: 'Niebieski', 6: 'Blady szary', 7: 'Blady szary', 8: 'Blady szary', 9: 'Blady szary', 10: 'Szary', 11: 'Szary', 12: 'Szary', 13: 'Brązowy', 14: 'Brązowy', 15: 'Brązowy', 16: 'Orzechowy', 17: 'Ciemnobrązowy', 18: 'Czarny', 19: 'Czarny'}