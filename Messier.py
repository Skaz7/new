import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.max_rows", 110)  # ustawienie wyświetlania wszystkich 110 wierszy bazy

##############################################################################
# definicja funcji czyszczącej ekran
def clear_screen():

    os.system('cls')


##############################################################################
# definicja funcji 0 - powrót
def back_if_0():

    while True:
        back = input("\n0 - Powrót.   ")
        if back == "0":
            return
        else:
            continue


##############################################################################
# Wyświetlanie danych o wszystkich obiektach Messiera
def print_all_data(): 

    clear_screen()

    print(messier)

    back_if_0()


##############################################################################
# Wyświetlanie wg numeru Messiera
def filter_by_messier_number():

    clear_screen()

    print("\nLista obiektów Messiera zawiera pozycje od M1 do M110.")
    print("\n0 - Powrót")
    search = input("\nJakiego numeru szukasz? :  ").upper() # jeśli wpiszemy 'm31' to zmieni na 'M31'
    
    if search == "0":
        return

    else:
        for i in range(len(messier)):
            if messier.loc[i, 'Numer Messiera'] == search:
                print(messier.loc[i, : ])
                print('\n') 

    back_if_0()


##############################################################################
# Wyszukiwanie wg typu obiektu
def filter_by_object_type(): 

    clear_screen()

    print("\n\t\t\t----------------------------------")
    print("\t\t\t| Wyszukiwanie obiektów wg typu. |")
    print("\t\t\t----------------------------------")
    print("\t\t\t| Dostępne opcje:                |")
    print("\t\t\t|                                |")
    print("\t\t\t| 1  - Pozostałość po supernowej |")
    print("\t\t\t| 2  - Gromada kulista           |")
    print("\t\t\t| 3  - Gromada otwarta           |")
    print("\t\t\t| 4  - Mgławica emisyjna         |")
    print("\t\t\t| 5  - Gromada gwiazd            |")
    print("\t\t\t| 6  - Mgławica planetarna       |")
    print("\t\t\t| 7  - Chmura gwiezdna           |")
    print("\t\t\t| 8  - Galaktyka spiralna        |")
    print("\t\t\t| 9  - Galaktyka eliptyczna      |")
    print("\t\t\t| 10 - Gwiazda podwójna          |")
    print("\t\t\t| 11 - Grupa gwiazd              |")
    print("\t\t\t| 12 - Mgławica dyfuzyjna        |")
    print("\t\t\t| 13 - Galaktyka soczewkowa      |")
    print("\t\t\t----------------------------------")
    search = input("\nTwój wybór :  ").capitalize() # Typ obiektu będzie zaczynał się wielką literą
    
    for i in range(len(messier)):
        if messier.loc[i, 'Typ obiektu'] == search:
            print(messier.loc[i, : ])
            print('\n')
    
    back_if_0()


##############################################################################
# Wyszukiwanie wg gwiazdozbiorów
def filter_by_constellation(): 

    clear_screen()

    print("\n\t\t\t------------------------------------------------")
    print("\t\t\t|   Wyszukiwanie obiektów w gwiazdozbiorach.   |")
    print("\t\t\t------------------------------------------------")
    print("\t\t\t| Dostępne gwiazdozbiory:                      |")
    print("\t\t\t|                                              |")
    print("\t\t\t| 1  - Andromeda   | 19 - Ryby                 |")
    print("\t\t\t| 2  - Bliźnięta   | 20 - Skorpion             |")
    print("\t\t\t| 4  - Herkules    | 22 - Smok                 |")
    print("\t\t\t| 3  - Byk         | 21 - Strzała              |")
    print("\t\t\t| 5  - Hydra       | 23 - Strzelec             |")
    print("\t\t\t| 6  - Jednorożec  | 24 - Tarcza               |")
    print("\t\t\t| 7  - Kasjopea    | 25 - Trójkąt              |")
    print("\t\t\t| 8  - Koziorożec  | 26 - Warkocz Bereniki     |")
    print("\t\t\t| 9  - Lew         | 27 - Wąż                  |")
    print("\t\t\t| 10 - Lis         | 28 - Wężownik             |")
    print("\t\t\t| 11 - Lutnia      | 29 - Wielka Niedźwiedzica |")
    print("\t\t\t| 12 - Orion       | 30 - Wielki Pies          |")
    print("\t\t\t| 13 - Panna       | 31 - Wieloryb             |")
    print("\t\t\t| 14 - Pegaz       | 32 - Wodnik               |")
    print("\t\t\t| 15 - Perseusz    | 33 - Woźnica              |")
    print("\t\t\t| 16 - Psy Gończe  | 34 - Zając                |")
    print("\t\t\t| 17 - Rak         |                           |")
    print("\t\t\t| 18 - Rufa        | 35 - Łabędź               |")
    print("\t\t\t------------------------------------------------")

    search = input("\nTwój wybór :  ").title() # Nazwa będzie rozpoczynać się wielkimi literami

    for i in range(len(messier)):
        if messier.loc[i, 'Gwiazdozbiór'] == search:
            print(messier.loc[i, : ])
            print('\n')
    
    back_if_0()


##############################################################################
# Wyszukiwanie wg jasności widomej
def filter_by_brightness():

    clear_screen()

    print("Wyszukiwanie obiektów, których jasność znajduje się w danym przedziale.")
    print("\nZakres jasności musi być z przedziału 1.4 - 12.0")

    while True:
        try:
            search_min = float(input("\nDolny zakres jasności: "))
        
        except ValueError:
            print("Jasność musi być liczbą. ")
            continue
        
        if search_min < 1.4 or search_min > 12.0:
            print("\nZakres jasności musi być z przedziału 1.4 - 12.0")
            continue

        try:
            search_max = float(input("Górny przedział jasności: "))

        except ValueError:
            print("\nJasność musi być liczbą. ")
            continue

        if search_max < search_min:
            print("\nJasność maksymalna musi być większa od minimalnej!. ")
            continue
        elif search_max > 12.0:
            print("\nJasność może mieć wartość maksymalną 12.0! ")
            continue

        for i in range(len(messier)):
            if messier.loc[i, 'Jasność'] >= search_min and messier.loc[i, 'Jasność'] <= search_max:
                print(messier.loc[i, : ])
                print('\n')
        
        back_if_0()
        return


##############################################################################
# Wyszukiwanie wg odległości od Ziemi
def filter_by_distance(): 

    clear_screen()
    
    print("Wyszukiwanie obiektów, których odległość od Ziemi zawiera się w danym przedziale.")
    print("\nZakres odległości musi być z przedziału 0.3 - 60000.0 lat świetlnych.")

    while True:
        try:
            search_min = float(input("\nNajmniejsza odległość: "))
        
        except ValueError:
            print("Odległość musi być liczbą. ")
            continue
        
        if search_min < 0.3 or search_min > 60000.0:
            print("\nZakres odległości musi być z przedziału 0.3 - 60000.0")
            continue

        try:
            search_max = float(input("Największa odległość: "))

        except ValueError:
            print("\nOdległość musi być liczbą. ")
            continue

        if search_max < search_min:
            print("\nOdległość maksymalna musi być większa od minimalnej!. ")
            continue
        elif search_max > 60000.0:
            print("\nOdległość może mieć wartość maksymalną 60000.0! ")
            continue

        for i in range(len(messier)):
            if messier.loc[i, 'Odległość'] >= search_min and messier.loc[i, 'Odległość'] <= search_max:
                print(messier.loc[i, : ])
                print('\n')
        
        back_if_0()
        return


##############################################################################
# Sortowanie wg typu obiektu
def sort_by_object_type():
    
    pass


##############################################################################
# Sortowanie wg gwiazdozbioru
def sort_by_constellation():
    
    pass


##############################################################################
# Sortowanie wg jasności
def sort_by_brightness():
    
    pass


##############################################################################
# Sortowanie wg odległości od Ziemi
def sort_by_distance():
    
    pass


##############################################################################
# Wyszukiwanie wg odległości od Ziemi
def sort_objects(): 

    clear_screen()

    print("Sortowanie obiektów wg kategorii :")
    print("\n1 - Według typu obiektu.")
    print("2 - Według gwiazdozbioru.")
    print("3 - Według jasności.")
    print("4 - Według odległości od Ziemi.\n")
    print("\n0 - Powrót.")

    while True:
        try:
            choice = int(input("Twój wybór: "))
        except ValueError:
            print("Musisz wybrać opcję z zakresu 1 - 4.")
            continue
        
        if choice == 0:
            main_screen()
        if choice == 1:
            sort_by_object_type()
        elif choice == 2:
            sort_by_constellation()
        elif choice == 3:
            sort_by_brightness()
        elif choice == 4:
            sort_by_distance()
        else:
            print("\nBłędna opcja!\n")
            continue
        
        back_if_0()


##############################################################################
# Główny ekran programu
def main_screen():

    while True:
        clear_screen()
        
        print("\n\n\n\t\t\t------------------------------------------")
        print("\t\t\t| Witaj w bazie danych obiektów Messiera |")
        print("\t\t\t------------------------------------------")
        print("\n\nWybierz opcję:\n")
        print("1 - Wyświetl dane wszystkich obiektów Messiera.")
        print("2 - Filtruj wg numeru Messiera.")
        print("3 - Filtruj wg typów obiektów.")
        print("4 - Filtruj wg gwiazdozbiorów.")
        print("5 - Filtruj wg jasności widomej.")
        print("6 - Filtruj wg odległości od Ziemi.")
        print("7 - Sortowanie listy.")
        print("\n0 - Wyjście z programu.")

        choice = input("\nTwój wybór: ")

        if choice == "0":
            print("\n\n\t\t\t\t------------------")
            print("\t\t\t\t| Do zobaczenia! |")
            print("\t\t\t\t------------------\n\n")
            quit() 
        elif choice == "1":
            print_all_data() 
        elif choice == "2":
            filter_by_messier_number()
        elif choice == "3":
            filter_by_object_type ()
        elif choice == "4":
            filter_by_constellation() 
        elif choice == "5":
            filter_by_brightness() 
        elif choice == "6":
            filter_by_distance() 
        elif choice == "7":
            sort_objects()
        else: 
            print("Zły wybór!")


##############################################################################
# Wczytywanie bazy obiektów Messiera z pliku excel
file = "C:\\Users\sebas\OneDrive\Messier repo\Messier.xlsx"
messier = pd.read_excel(file)

# Ustawienie wielkich liter na początkach nazw.
for i in range(len(messier)):
        messier.loc[i, 'Nazwa'] = messier.loc[i, 'Nazwa'].title()
        messier.loc[i, 'Typ obiektu'] = messier.loc[i, 'Typ obiektu'].capitalize()
        messier.loc[i, 'Gwiazdozbiór'] = messier.loc[i, 'Gwiazdozbiór'].title()        

# Tworzenie słownika gwiazdozbiorów

constellations_set = set()  # Najpierw z kolumny 'Gwiazdozbiór' tworzymy zbiór, bo elementy zbioru nie mogą się powtarzać, więc będzie tylko po jednym wystąpieniu każdego gwiazdozbioru
for i in range(0, len(messier)): 
    constellations_set.add(messier.loc[i, 'Gwiazdozbiór'])

'''
Zbiór trzeba przekonwertować na listę, bo zbiór nie jest iterowalny
i nie da się przekonwertować na słownik wg sekwencji.
'''
constellations_list = sorted(constellations_set)
constellations_dict = {}

for i in range(1, len(constellations_list)):
    constellations_dict[i] = constellations_list[i]



##############################################################################
# Wywołanie głównego ekranu programu
main_screen()