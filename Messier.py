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

    search = input("Jaki jest numer Messiera obiektu, którego szukasz? :  ")
    
    for i in range(len(messier)):
        if messier.loc[i, 'Numer Messiera'] == search:
            print(messier.loc[i, : ])
            print('\n')
    
    back_if_0()


##############################################################################
# Wyszukiwanie wg typu obiektu
def filter_by_object_type(): 

    clear_screen()

    search = input("Jaki jest typ obiektu, którego szukasz? :  ")
    
    for i in range(len(messier)):
        if messier.loc[i, 'Typ obiektu'] == search:
            print(messier.loc[i, : ])
            print('\n')
    
    back_if_0()


##############################################################################
# Wyszukiwanie wg gwiazdozbiorów
def filter_by_constellation(): 

    clear_screen()

    search = input("Podaj gwiazdozbiór :  ")

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
# Wyszukiwanie wg odległości od Ziemi
def sort_objects(): 

    clear_screen()

    pass


##############################################################################
# Główny ekran programu
def main_screen():

    while True:
        clear_screen()
        
        print("\t\t------------------------------------------")
        print("\t\t| Witaj w bazie danych obiektów Messiera |")
        print("\t\t------------------------------------------")
        print("\nWybierz opcję:\n")
        print("1 - Wyświetl dane wszystkich obiektów Messiera.")
        print("2 - Filtruj wg numeru Messiera.")
        print("3 - Filtruj wg typów obiektów.")
        print("4 - Filtruj wg gwiazdozbiorów.")
        print("5 - Filtruj wg jasności widomej.")
        print("6 - Filtruj wg odległości od Ziemi.")
        print("7 - Sortowanie obiektów.")
        print("0 - Wyjście z programu.")

        choice = input("\nTwój wybór: ")

        if choice == "0":
            print("\nDo zobaczenia!\n\n")
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


##############################################################################
# Wywołanie głównego ekranu programu
main_screen()