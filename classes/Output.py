import random
import time
import webbrowser


class Output:
    tips_of_a_day = [
        "Jak nadejdzie białe zimno, pamiętaj aby nie jeść żółtego śniegu",
        "Pamiętaj żeby brać prysznic, ludzie będą Cię inaczej traktować, jesli nie będzie tego robić",
        "Jedz śniadania, gdyż zdrowe są one i smaczne",
        "Atakowanie postaci niezależnych może sprawić że staną się one wrogie",
        "Czas leczy rany, jednak nie wszystkie, niektóre wymagają pomocy medycznej",
        "Wiele postaci ma dużo do powiedzenia, jednak nie wszystko jest ważne",
        "Jesteś brzydki i wali ci z japy",
        "Mistrz Gry ma zawsze rację",
        r"Jeśli przyłożysz ucho do uda ciężarnej kobiety możesz usłyszeć 'Co Ty kurwa robisz?!'",
        "Lizanie klamek w niektórych kulturach uznawane jest za nietaktowne",
        "W większości miejsc nie możesz poruszać się nago, bez zwracania na siebie uwagi",
        "Jeśli ktoś Cię zaatakuje, możesz zostać ranny",
        "Pływanie? Na chuj to komu?",
        "W imperium nie ma mutantów!",
        "Jeśli Mistrz Gry mówi że czegoś nie można zrobić, polej mu kopa smaku",
        "Przyjaciele są jak drzewa. Upadną jeśli uderzysz je kilka razy siekierą",
        "Broń wymaga ostrzenia",
        "Podczas walki pancerz może ulec uszkodzeniu",
        "Sasin wydał 70 mln na wybory, które się nie odbyły",
        "Przed wyruszeniem w drogę należy zebrać drużynę",
        "Spożywanie napojów alkoholowych może wydłużyć czas podróży",
        "Jeśli MG na szybko losuje imię NPCa, możesz śmiało założyć że nie jest to ważna postać",
        "Granie niziołkiem może spowodować szybką utratę PPków i trwałym uszczerbkiem na zdrowiu psychicznym",
        "Pachu ma małego",
        "Jeśli koń jest podkuty łatwiej będzie Ci z niego spaść, niż kiedy idziesz pieszo",
        "Jeśli okradania złodzieja nie należy traktować jak kradzieży, to jeśli usunąć z tego łańcuszka złodzieja, wychodzi, że kradzież nie jest kradzieżą",
        "Pułapki w lochach mogą okazać się zabójcze",
        "Kalkuluje zajebistość postaci",
        "Jesteś pewien, że ta postać jest grywalna?",
        "Jeśli kolega gra gnomem, pilnuj swoich butów",
        "Ingerencja z chaosem to najszybszy sposób do wyhodowania sobie trzeciej ręki",]

    def __init__(self):
        self.podpis = "Created by DugSnaga"

    def random_tip_of_a_day(self):
        aacb = len(self.tips_of_a_day) - 1
        random_tip = random.randint(0, aacb)
        print(f"\n \n \n{self.tips_of_a_day[random_tip]} \n")
        #time.sleep(3)

    def format_output(self,character):

        self.pierwszy_wiersz = "Imie: " + str(character.name) + "      " + "Rasa: " + str(character.race.nazwa) + "     Płeć: " + str(character.gender) + "     " + "Profesja: " + str(character.profession.nazwa_profesji_dict[character.level]) + "      " + "Kariera: " + str(character.profession.nazwa_profesji_dict[2])
        self.drugi_wiersz = "Status: " + character.miss.miss['Status'] + "     " + "Poziom: " + str(character.level) + "    " + "Wzrost: " + str(character.appearance.height) + "    " + "Kolor Włosów: " + str(character.appearance.hair) + "    " + "Kolor Oczu: " + str(character.appearance.eyes) + "\n"

        # nazwy tabeli cech 'WW', 'US', etc
        self.trzeci_wiersz = ""
        cechy_rozwiniete_dict = character.characteristics[1]
        cechy_bazowe_dict = character.characteristics[0]
        kolejnosc = ['WW', 'US', 'S', 'Wt', 'I', 'Zw', 'Zr', 'Int', 'SW', 'Ogd']
        for key in kolejnosc:
            c = 7 - len(key)
            d = ""
            while c > 0:
                d = d + " "
                c = c - 1
            self.trzeci_wiersz = self.trzeci_wiersz + str(key) + d
        # cechy bazowe
        self.czwarty_wiersza = ""
        for key in kolejnosc:
            c = 5
            d = ""
            while c > 0:
                d = d + " "
                c = c - 1
            self.czwarty_wiersza = self.czwarty_wiersza + str(cechy_bazowe_dict[key]) + d

        # wartość rozwinięć
        self.czwarty_wierszb = ""

        for key in kolejnosc:
            rozw = cechy_rozwiniete_dict[key] - cechy_bazowe_dict[key]
            c = 5 - len(str(rozw))
            d = ""
            while c > 0:
                d = d + " "
                c = c - 1
            self.czwarty_wierszb = self.czwarty_wierszb + str(rozw) + d + "  "

        # wartośc końcowa
        self.czwarty_wiersz= ""
        for key in kolejnosc:
            c = 5
            d = ""
            while c > 0:
                d = d + " "
                c = c - 1
            self.czwarty_wiersz= self.czwarty_wiersz+ str(cechy_rozwiniete_dict[key]) + d

        self.trzeci_wiersz = self.trzeci_wiersz + "Żyw" + "    " + "SZ" + "    " + "PP" + "    " + "PB"
        self.czwarty_wiersz= self.czwarty_wiersz+ str(character.miss.miss["Żyw"]) + "     " + str(character.miss.miss["SZ"]) + "     " + str(character.miss.miss["PP"]) + "     " + str(character.miss.miss["PB"])
        piaty_wiersz = "UMJEJĘTNOŚCI"
        self.listow_um = ""
        umiejetnosci_z_wartosciami_powiekszonymi_o_cechy = {}

        for umiejetnosc, wartosc in character.abilities.items():
            if "(Zw)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["Zw"]
            if "(WW)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["WW"]
            if "(Ogd)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["Ogd"]
            if "(Int)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["Int"]
            if "(S)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["S"]
            if "(Wt)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["Wt"]
            if "(US)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["US"]
            if "(SW)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["SW"]
            if "(Zr)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["Zr"]
            if "(I)" in umiejetnosc:
                umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[umiejetnosc] = wartosc + cechy_rozwiniete_dict["I"]
       
        for key, val in sorted(character.abilities.items()):
            self.listow_um = self.listow_um + str(key) + ":" + str(val) + "(" + str(umiejetnosci_z_wartosciami_powiekszonymi_o_cechy[key]) + ")" + "\n"
        string_talentow = ""
        a = 1
        for el in character.talents:
            if a % 5 != 0:
                string_talentow = string_talentow + el + "; "

            if a % 5 == 0:
                string_talentow = string_talentow + el + ";\n"
            a = a + 1

        self.listow_tal = "TALENTY: " + string_talentow
        a = 1
        string_wyp = ""

        for el in character.equipment:
            if a % 5 != 0:
                string_wyp = string_wyp + el + "; "

            if a % 5 == 0:
                string_wyp = string_wyp + el + ";\n"
            a = a + 1
        self.listow_maj = "WYPOSAŻENIE: " + string_wyp 





    def output_to_CMD(self):
        print(self.pierwszy_wiersz)
        print(self.drugi_wiersz)
        print(self.trzeci_wiersz)
        print(self.czwarty_wiersza)
        print(self.czwarty_wierszb)
        print(self.czwarty_wiersz)
        print("\n")
        print("UMIEJĘTNOŚCI: \n")
        print(self.listow_um)
        print(self.listow_tal)
        print(self.listow_maj)

    def output_to_file(self,character):
        eager = input("Chcesz zapisać output do pliku? (t/n)")
        self.nazwa_pliku = str(character.profession.nazwa_profesji_dict[2]) + "_" + str(character.race.nazwa) + "_" + str(character.name) + ".txt"
        if eager != "n":
            with open(self.nazwa_pliku, "w") as file_object:
                file_object.write(self.pierwszy_wiersz + "\n")
                file_object.write(self.drugi_wiersz + "\n")
                file_object.write(self.trzeci_wiersz + "\n")
                file_object.write(self.czwarty_wiersza + "\n")
                file_object.write(self.czwarty_wierszb + "\n")
                file_object.write(self.czwarty_wiersz+ "\n")
                file_object.write("\n")
                file_object.write("UMIEJĘTNOŚCI: \n")
                file_object.write(self.listow_um + "\n")
                file_object.write(self.listow_tal + "\n" + "\n")
                file_object.write(self.listow_maj + "\n")
                file_object.write("\n \n \n")
                file_object.write(self.podpis)
                # file_object.write("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n" + prawa_zastrz)

            webbrowser.open(self.nazwa_pliku)