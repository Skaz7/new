import subprocess
import datetime
import time
import os
import json
import win32gui # BIBLIOTEKA DO UKRYWANIA APLIKACJI
import win32.lib.win32con as win32con # BIBLIOTEKA DO UKRYWANIA APLIKACJI

'''
v0.10 - działa sprawdzanie czy proces jest aktualnie uruchomiony i zapisywanie do słownika w postaci 'Godzina: uruchomiony'.
V0.20 - Dodano opcję ukrywania programu. Zmiana dekodowania procesu na utf-16 z powodu zwracanego wcześniej błędu dekodowania.
        Dodano plik z rozszerzeniem .pyw - ukrywa konsolę w trakcie wykonywania programu
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
    output = subprocess.check_output(call).decode('utf-16')
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


# funkcja ukrywająca aplikację - działanie w tle
def hide_app():
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)


# Główna pętla programu
while True:

    now = datetime.datetime.now() # odczyt aktualnej daty i czasu

    if process_exists('chrome.exe') == True: # jeśli proces jest uruchomiony to:
        activity_dict[str(f'{now: %Y-%m-%d %H:%M:%S}')] = 'Działa    '

    else: # jeśli proces nie jest uruchomiony to:
        activity_dict[str(f'{now: %Y-%m-%d %H:%M:%S}')] = 'Nie działa'
    
    save_data_to_file() # zapisz dane do pliku
    time.sleep(10) # odstęp czasowy w sekundach pomiędzy kolejnymi odczytami
