import subprocess
import datetime
import time
import os
import json
from typing import List
import win32gui # BIBLIOTEKA DO UKRYWANIA APLIKACJI
import win32.lib.win32con as win32con # BIBLIOTEKA DO UKRYWANIA APLIKACJI

'''
v0.10 - działa sprawdzanie czy proces jest aktualnie uruchomiony i zapisywanie do słownika w postaci 'Godzina: uruchomiony'.
v0.20 - Dodano opcję ukrywania programu. Zmiana dekodowania procesu na utf-16 z powodu zwracanego wcześniej błędu dekodowania.
        Dodano plik z rozszerzeniem .pyw - ukrywa konsolę w trakcie wykonywania programu
v0.30 - Dodano sprawdzanie kilku kolejnych programów jednocześnie (chrome, notepad, ToDo) 
        i zapisanie wspólnego słownika do pliku .json
v0.40 - zmieniony sposób zapisu danych do pliku .json, zamiast słowników ze stanami uruchomienia programów zagnieżdżonych
        w słownikach z nazwami programów, teraz są listy ze stanami uruchomienia programów zagnieżdżone w słownikach 
        nazw programów. Pozwoliło to na zmianę formatu zapisu daty ze string na datetime.

#ToDo:
- 
- przesłanie pliku ze słownikiem na adres mailowy.

'''

# funkcja sprawdzająca czy dany proces jest uruchomiony
def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode('utf-8')
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


# funkcja czyszczenia ekranu
def clear_screen():
    os.system('cls')

# funkcja zapisująca odczytane dane do pliku .json
def save_data_to_file():
    dict_file = 'd:\\users\\sebas\\onedrive\\repositories\\playtimecheck\data.json'
    with open(dict_file, 'w') as file:
        json.dump(data_dict, file, indent=4)
        # json.dump(notepad_activity, file, indent=4)
        # json.dump(ToDo_activity, file, indent=4)

clear_screen()

chrome_activity = [] # stworzenie pustj listy do zapisania danych w formacie ['czas', True] lub ['czas', False]
notepad_activity = []
ToDo_activity = []

# funkcja ukrywająca aplikację - działanie w tle
def hide_app():
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)


# Główna pętla programu
while True:

    now = datetime.datetime.now() # odczyt aktualnej daty i czasu

    if process_exists('chrome.exe') == True: # jeśli proces jest uruchomiony to:
        chrome_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', True])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Chrome działa')

    if process_exists('chrome.exe') == False: # jeśli proces nie jest uruchomiony to:
        chrome_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', False])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Chrome nie działa')

    if process_exists('notepad.exe') == True:
        notepad_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', True])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Notepad działa')

    if process_exists('notepad.exe') == False:
        notepad_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', False])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Notepad nie działa')
    
    if process_exists('ToDo.exe') == True:
        ToDo_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', True])
        print(f'{now:%Y-%m-%d %H:%M:%S}: ToDo działa')

    if process_exists('ToDo.exe') == False:
        ToDo_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', False])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Todo nie działa')
    
    data_dict = {'Chrome': chrome_activity, 'Notepad': notepad_activity, 'ToDo': ToDo_activity}

    save_data_to_file() # zapisz dane do pliku
    time.sleep(30) # odstęp czasowy w sekundach pomiędzy kolejnymi odczytami
