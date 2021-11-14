import json
from datetime import datetime, timedelta
import time
import os
import matplotlib.pyplot as plt

'''
Moduł do analizy danych przesłanych w pliku .json.
Dane będą dostępne w formie tabel i wykresów.

v0.10 - piersza wersja
v0.20 - druga wersja:
    - odczytywanie danych z zapisanego pliku -json
    - konwersja danych z dict do list
    - konwersja formatu daty ze string do datetime
    - wydruk wykresu prezentującego stan programu w sprawdzanym okresie

'''

data_dict = []

# funkcja czyszcząca ekran
def clear_screen():
    os.system('cls')


def read_data_from_file():

    file_name = 'data.json'

    with open(file_name, 'r') as file:
        global data_dict
        data_dict = json.load(file)

    for date, state in data_dict.items():
        print('| ' + date + ' : ' + state + ' |')


def plot_data():
    plt.bar(*zip(*data_dict.items()))
    plt.show()


clear_screen()

print('\n   Wydruk stanu procesu w czasie:\n')
print('_____________________________________')
print('|     Data   | Godzina |    Stan    |')
print('-------------------------------------')

read_data_from_file()
print('-------------------------------------\n')


data_list = list(data_dict.items())
new_data_list = []

for k, v in data_list:
    entry = [datetime.strptime(k, '%Y-%m-%d %H:%M:%S'), v]
    new_data_list.append(entry)

for i in range(len(new_data_list)):
    print(new_data_list[i][0], ' - ', new_data_list[i][1])

first = (new_data_list[0][0]) # czas rozpoczęcia sprawdzania
second = (new_data_list[-1][0]) # czas zakończenia sprawdzania

diff = second - first # Całkowity czas działania programu sprawdzającego

print(f'\nCzas działania programu sprawdzającego (H:M:S): {diff}\n')

plt.xlabel('Godziny')
plt.ylabel('Stan sprawdzanego programu')
plt.title(f'Stan sprawdzanego programu w czasie {new_data_list[0][0]}  -  {new_data_list[-1][0]}')

for i in range(len(new_data_list)):
    plt.plot(new_data_list[i][0], new_data_list[i][1], 'go')
plt.show()