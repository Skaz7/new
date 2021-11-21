import json
from datetime import datetime
import time
import os
import matplotlib.pyplot as plt
# import pandas as pd


# Funcja wczytująca dane z pliku
def read_data_from_file():

    file_name = 'd:\\users\\sebas\\onedrive\\repositories\\playtimecheck\\data.json'
    with open(file_name, 'r') as file:
        global data_dict
        data_dict = json.load(file)


# funkcja czyszcząca ekran
def clear_screen():
    os.system('cls')


# Funcja konwertująca forma string do datetime
def convert_string_to_datetime():

    for program, state in data_dict.items():
        for i in range(len(state)):
            state[i][0] = datetime.strptime(state[i][0], '%Y-%m-%d %H:%M:%S')


# funcja drukująca czas rozpoczęcia, zakończenia i trwania pomiaru
def check_time():

    first = data_dict['Chrome'][0][0]
    last = data_dict['Chrome'][-1][0]
    measure_count = len(data_dict['Chrome'])

    print('\n--------------------------------------------------')
    print(f'| Pomiar rozpoczęto:         {first} |')
    print('|                                                |')
    print(f'| Pomiar zakończono:         {last} |')
    print('|                                                |')
    print(f'| Całkowity czas pomiaru:    {last - first}             |')
    print('|                                                |')
    print(f'| Ilość wykonanych pomiarów: {measure_count}                 |')
    print('--------------------------------------------------')
    print()

    input('Enter - powrót do głównego menu.')
    main_menu()


# funkcja drukująca zestawienie wszystkich programów i ich stanów w czasie
def print_all_data():

    clear_screen()

    for key in data_dict.keys():
        print(key)
        for i, j in data_dict[key]:
            print(i, j)

    input('Enter - powrót do głównego menu.')
    main_menu()


# funcja drukująca wykres
def plot_data():

    for i in range(len(chrome_list)):
        x_data = chrome_list[i][0]
        y_data = chrome_list[i][1]
        plt.plot(x_data, y_data, 'rx', markersize = 12, label = 'Chrome')

    for i in range(len(notepad_list)):
        x_data = notepad_list[i][0]
        y_data = notepad_list[i][1]
        plt.plot(x_data, y_data, 'b_', markersize = 12, label = 'Notepad')

    for i in range(len(todo_list)):
        x_data = todo_list[i][0]
        y_data = todo_list[i][1]
        plt.plot(x_data, y_data, 'g|', markersize = 12, label = 'ToDo')

        plt.xlabel('Data / godzina')
        plt.ylabel('Stan programu')
        plt.title('Wykres użycia programów CHROME, NOTEPAD i ToDo')
        plt.ylim(-0.3, 1.3)

    plt.show()


# Menu główne programu
def main_menu():

    while True:
        clear_screen()
        print('\n\n\n\t\t\tAnaliza danych użycia programów.')
        print('\n\t\t\tWybierz jedną z poniższych opcji:')
        print('\n\t\t\t\t1 - Analiza działania pojedynczego programu')
        print('\t\t\t\t2 - Tabela z danymi użycia wszystkich programów.')
        print('\t\t\t\t3 - Wykres użycia wszystkich programów.')
        print('\t\t\t\t4 - Wydruk czasu pomiaru.')
        print('\n\t\t\t\t0 - Wyjście z programu.')

        try:
            choice = int(input('\n\t\t\tTwój wybór: '))

            if choice == 0:
                clear_screen()
                quit()
            elif choice == 1:
                pass
            elif choice == 2:
                clear_screen()
                print_all_data()
            elif choice == 3:
                clear_screen()
                plot_data()
            elif choice == 4:
                clear_screen()
                check_time()
            else:
                print('\n\t\t\tZŁY WYBÓR!')
                time.sleep(2)
                main_menu()
        except ValueError:
            print('\n\t\t\tZŁY WYBÓR!')
            time.sleep(2)
            main_menu()








########################################################################################################################
# GŁÓWNY PROGRAM:

data_dict = {}


read_data_from_file()                     # wczytaj plij json z danymi

chrome_list = data_dict['Chrome']
notepad_list = data_dict['Notepad']
todo_list = data_dict['ToDo']

convert_string_to_datetime()

main_menu()                               # Wyświetl menu główne programu