import subprocess
import datetime
import time
import os
import json

'''
Wersja v0.10 - działa sprawdzanie czy proces jest aktualnie uruchomiony i zapisywanie do słownika w postaci 'Godzina: uruchomiony'.
#ToDo:
- zapisanie słownika do pliku
- 
- wykres aktywności programu
- przesłanie pliku ze słownikiem na adres mailowy.

'''

# funkcja sprawdzająca czy dany proces jest uruchomiony
def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


# funkcja czyszczenia ekranu
def clear_screen():
    os.system('cls')

# funkcja zapisująca odczytane dane do pliku .json
def save_data_to_file():
    dict_file = 'data.json'
    with open(dict_file, 'w') as file:
        json.dump(activity_dict, file, indent=4)

clear_screen()
activity_dict = {} # stworzenie pustego słownika do zapisania danych w formacie 'czas: działa' lub 'czas: nie działa'

# Główna pętla programu
while True:

    now = datetime.datetime.now() # odczyt aktualnej daty i czasu

    if process_exists('chrome.exe') == True: # jeśli proces jest uruchomiony to:
        print(f'Program działa o godzinie: {now: %Y-%m-%d %H:%M}')
        activity_dict[str(f'{now: %Y-%m-%d %H:%M:%S}')] = 'Działa    '

    else: # jeśli proces nie jest uruchomiony to:
        print(f'Program nie działa o godzinie: {now: %Y-%m-%d %H:%M}')
        activity_dict[str(f'{now: %Y-%m-%d %H:%M:%S}')] = 'Nie działa'
    
    save_data_to_file() # zapisz dane do pliku
    time.sleep(3) # odstęp czasowy w sekundach pomiędzy kolejnymi odczytami
