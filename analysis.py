import json
import datetime
import time
import os
import matplotlib.pyplot as plt

'''
Moduł do analizy danych przesłanych w pliku .json.
Dane będą dostępne w formie tabel i wykresów.

v0.10 - piersza wersja

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


# plot_data()

data_dict = {k: True if data_dict[k] == 'Działa    ' else False for k in data_dict}
print(data_dict)

plot_data()