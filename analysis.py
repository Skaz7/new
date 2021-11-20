import json
from datetime import datetime
# import time
import os
import matplotlib.pyplot as plt
import pandas as pd

'''
Moduł do analizy danych przesłanych w pliku .json.
Dane będą dostępne w formie tabel i wykresów.

v0.10 - piersza wersja
v0.20 - druga wersja:
        - odczytywanie danych z zapisanego pliku -json
        - konwersja danych z dict do list
        - konwersja formatu daty ze string do datetime
        - wydruk wykresu prezentującego stan programu w sprawdzanym okresie
v0.30 - trzecia wersja:
        - odczyytywanie nowego pliku .json (sprawdzane kilka programów jednocześnie)
        - formatowanie pliku i drukowanie na ekranie wyniku
v0.40 - czwarta wersja
        - gruntowna przebudowa pliku. Dane w formacie .json zawierają słowniki list zamiast słowników słowników jak wcześniej.
          Odczytana z pliku data jest od raz w formacie datetime a nie jak wcześniej string. W związku z tym nie ma konwersji.
          Pozwala to na wykonywanie operacji związanych z datami.


#TODO
      - drukowanie wykresów
      - #! PRAWDOPODOBNIE DO DRUKOWANIA TRZEBA PRZEKONWERTOWAĆ STRING Z FORMATU 'DZIAŁA / NIE DZIAŁA ' NA BOOLEAN (TRUE / FALSE)
'''

data_dict = {}


# funkcja czyszcząca ekran
def clear_screen():
    os.system('cls')


# Funcja wczytująca dane z pliku
def read_data_from_file():
    '''
    Wczytuje plik json w formacie jak poniżej:
    {
        "Chrome": {
            "2021-11-15 19:29:20": "Chrome działa    "
        },
        "Notepad": {
            "2021-11-15 19:29:20": "Notepad nie działa"
        },
        "ToDo": {
            "2021-11-15 19:29:20": "ToDo nie działa"
        }
    }
    '''
    file_name = 'd:\\users\\sebas\\onedrive\\repositories\\playtimecheck\\data.json'
    with open(file_name, 'r') as file:
        global data_dict
        data_dict = json.load(file)


# funcja drukująca listę słowników
def print_data():

    '''
    Drukowanie słownika list w formacie jak poniżej:

    Chrome
    ---------------------
    2021-11-15 19:29:20 Chrome działa    
    2021-11-15 19:29:22 Chrome działa    
    2021-11-15 19:29:24 Chrome działa    
    ...
    ...

    Najpierw w głównej pętli drukowany jest pierwszy element z listy, czyli nazwa programu wraz z podkreśleniem.
    Wewnętrzna pętla drukuje elementy zagnieżdżone, czyli listy z godzinami i stanami uruchomienia danego programu.
    '''

    for program, state in data_dict.items():
        print('\n\n', program, sep = '')
        print('----------------')

        for i in range(len(state)):
            state[i][0] = datetime.strptime(state[i][0], '%Y-%m-%d %H:%M:%S')
            print(state[i][0], ': ', state[i][1])


# funcja drukująca czas rozpoczęcia, zakończenia i trwania pomiaru
def check_time():

    first = data_dict['Chrome'][0][0]
    last = data_dict['Chrome'][-1][0]

    print(f'\n\nPomiar rozpoczęto:_________{first}')
    print(f'\nPomiar zakończono:_________{last}')
    print(f'\nCałkowity czas pomiaru: ___{last - first}')
    print()


# funcja drukująca wykres
def plot_data():

    check_time = list(data_dict.values()[0])
    program_state = list(data_dict.values()[1])
    plt.bar(x = check_time, y = program_state)
    plt.show()


# funkcja konwertująca opis stanu programu do formatu boolean (true/false)
def convert_to_boolean():
    for key in data_dict.keys():
        for i in range(len(data_dict[key])):
            if data_dict[key][i][1] == 'Chrome działa    ':
                data_dict[key][i][1] = True
            elif data_dict[key][i][1] == 'Chrome nie działa':
                data_dict[key][i][1] = False
            if data_dict[key][i][1] == 'Notepad działa    ':
                data_dict[key][i][1] = True
            elif data_dict[key][i][1] == 'Notepad nie działa':
                data_dict[key][i][1] = False
            if data_dict[key][i][1] == 'ToDo działa    ':
                data_dict[key][i][1] = True
            elif data_dict[key][i][1] == 'ToDo nie działa':
                data_dict[key][i][1] = False

    for key in data_dict.keys():
        print(key)
        for i, j in data_dict[key]:
            print(i, j)




########################################################################################################################
# GŁÓWNY PROGRAM:

clear_screen()                                                              # wyczyść ekran

read_data_from_file()                                                       # wczytaj plij json z danymi

print_data()

print()

check_time()

print()

convert_to_boolean()
   