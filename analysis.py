import json
import datetime
import time
import os

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
        data_dict = json.load(file)

    for date, state in data_dict.items():
        print('| ' + date + ' : ' + state + ' |')

clear_screen()

print('\n   Wydruk stanu procesu w czasie:\n')
print('_____________________________________')
print('|     Data   | Godzina |    Stan    |')
print('-------------------------------------')

read_data_from_file()
