from classes.Talents import Talents
from classes.Character import Character
from classes.Name import Name
from classes.Level import Level
from classes.Gender import Gender
from classes.RaceSeizure import RaceSeizure
from classes.ProfessionSeizure import ProfessionSeizure
from classes.Characteristics import Characteristics
from classes.Abilities import Abilities
from classes.Equipment import Equipment
from classes.Miss import Miss
from classes.Appearence import Appearence
from classes.Output import Output




# start instancja Character
character = Character()
# tworzymy obiekt RaceSeizure, który słuzy do dobierania rasy
race_seizure = RaceSeizure()
#pytamy o rasę
race_seizure.ask_for_race()
#dajemy rasę {character.race} wybraną, bądź losową w postaci obiektu RaceTraits
race_seizure.give_race(character)
#Informacja o rasie
print(f"Twoja rasa to {character.race.nazwa} \n")
# tworzymy instancję obiektu ProfessionSeizure, ktory słuzy do dobierania profesji
profession_seizure = ProfessionSeizure()
#pytamy o profesję
profession_seizure.ask_for_profession()
#dobieramy profesję według rasy, lub inputu
profession_seizure.give_profession_name_from_input_or_random(character)
#dajemy profesję {character.profession} w postaci obiektu ProfessionTraits
profession_seizure.create_ProfessionTraits_object_and_add_to_character(character)
#Informacja o profesji
print(f"Twoja profesja to {character.profession.nazwa_profesji_dict[2]} \n")
#tworzymy instancję obiektu Gender, ktory służy do dobierania płci
gender = Gender()
#pytamy o płeć
gender.ask_for_gender()
#dajemy płeć {character.gender} w postaci stringu
gender.give_gender_to_character(character)
#Informacja o płci
print(f"Twoja płeć to {character.gender}")
#tworzymy instancję obiektu Name, ktory słuzy do dobierania imienia
name = Name()
#pytamy o imię
name.ask_for_name()
#dajemy imię {character.name} w postaci stringu
name.name_to_character(character) 
#Informacja o imieniu
print(f"Twoje imię to {character.name} \n")
#tworzymy instancję obiektu Level, ktory słuzy do dobierania poziomu
level = Level()
#pytamy o poziom i od razu go aplikujemy {character.level} w postaci liczby 0-4
level.ask_for_level_and_give(character)
#Informacja o poziomie
print(f"Twój poziom to {character.level} \n")
#tworzymy instancję obiektu Talents, ktory służy do dobierania talentów
talents = Talents()
# dobieramy losowe talenty od rasy. Co ważne ta funkcja usuwa cyfrę z końca listy, więc po tym lista character.race.talenty_z_liczba_losowych_lista_list zawiera tylko stringi i listy
talents.draw_random_talents(character)
#pytamy i dodajemy wybieralne talenty 'albo/albo' pochądzące od rasy
talents.choosable_talents_from_race(character)
#dodajemy talenty od profesji w zależności od levelu postaci
talents.talents_from_profession(character)
#dodajemy talenty do instancji character w postaci listy
talents.add_talents_to_character(character)
#Informacja o talentach
print(f"Twoje talenty to {character.talents} \n")
#tworzenie instancji obiektu Characteristics, służącej do dobierania cech
characteristics = Characteristics()
#pytanie o własne rzuty
characteristics.ask_for_characteristics()
#losowanie rzutów. Odpali tylko jeśli nie zostały wcześniej wpisane
characteristics.draw_random_characteristics(character)
print(f"Twoje rzuty to {(characteristics.characteristics)} \n")
print(f"Razem {characteristics.dobroc} Współczynnik dobroci Twoich rzutów to {characteristics.dobroc/110}")
#podnoszenie charakterystyk od talentów
characteristics.raise_characteristics_with_talents(character)
#podnoszenie charakterystyk od rasy
characteristics.raise_characteristics_with_race(character)
#podnoszenie charakterystyk od profesji, dodanie atrybutu characteristics.characteristics2
characteristics.raise_characteristics_with_profession(character)
#dodanie charakterystyk do character.characteristics
characteristics.give_characteristics_to_character(character)
#Informacja o charakterystykach
print(f"Twoje bazowe charakterystyki to {(character.characteristics[0])}")
print(f"Twoje rozwinięte charakterystyki to {(character.characteristics[1])}\n")
#Stworzenie instancji obiektu Abilities, służącej do dobierania umiejetności
abilities = Abilities()
#wyciągnięcie informacji od instancji Character
abilities.import_abilities(character)
#formatowanie promptu dla umeiejętności rasowych
abilities.format_question_for_race_abilities()
#spytanie o wybranie umiejętności
abilities.ask_for_race_abilities()
#wpisane losowych umiejętności
abilities.write_random_race_abilities()
#wpisanie umiejętności od profesji, w zalezności od levelu
abilities.write_profession_abilities(character)
#dodanie umiejętności od rasy i od profesji
abilities.join_race_and_profession_abilities()
#dodanie umiejętności do instancji Character 
abilities.give_profession_abilities_to_character(character)
#Informacja o umiejętnościach
print(f"Twoje umiejętności to {character.abilities} \n")
#punkty bohatera, punkty przeznaczenia i status. Klasa Miss to rozwiązuje
miss = Miss()
#dodajemy miss do character
miss.add_miss_to_character(character)
#pytamy PP i PB
miss.get_PP_and_PB(character)
#Informacja o PP i PB
print(f"Twoje PP to {character.miss.miss['PP']}")
print(f"Twoje PB to {character.miss.miss['PB']}\n")
#dodajemy status
miss.get_status(character)
#rozpakowanie ekwipunku
eq = Equipment()
eq.unpack_eq(character)
#dodanie złota
eq.create_gold_str_and_append_to_character_equipment(character)
#dodajemy klase Appearence która odpowiada za wygląd
character.appearance = Appearence()
#pytamy czy chce wpisać cechy wyglądu
character.appearance.ask_about_app()
#losujemy/pytamy o włosy
character.appearance.get_hair(character)
#losujmeyy/pytamy o oczy
character.appearance.get_eyes(character)
#losujmeyy/pytamy o wzrost
character.appearance.get_height(character)
#informacje o wyglądzie
print(f"Twoje włosy to {character.appearance.hair}")
print(f"Twoje oczy to {character.appearance.eyes}")
print(f"Twój wzrost to {character.appearance.height} \n")
#zdobywamy HP
character.miss.get_HP(character)
#zdobywamy SZ
character.miss.get_speed(character)
#budujemy output
out = Output()
out.format_output(character)
out.random_tip_of_a_day()
#wyświetlamy output
out.output_to_CMD()
#pytamy czy chce zapisać plik
out.output_to_file(character)
#KONIEC

