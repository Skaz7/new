import subprocess
import datetime
import time
import os
import json
import win32gui # BIBLIOTEKA DO UKRYWANIA APLIKACJI
import win32.lib.win32con as win32con # BIBLIOTEKA DO UKRYWANIA APLIKACJI



def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode('utf-8')
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


def clear_screen():
    os.system('cls')


def save_data_to_file():
    dict_file = 'd:\\users\\sebas\\onedrive\\repositories\\playtimecheck\data.json'
    with open(dict_file, 'w') as file:
        json.dump(data_dict, file, indent=4)


def hide_app():
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)


clear_screen()

chrome_activity = [] # stworzenie pustj listy do zapisania danych w formacie ['czas', True] lub ['czas', False]
notepad_activity = []
ToDo_activity = []


# MAIN LOOP
while True:

    now = datetime.datetime.now() # get actual data & time

    if process_exists('chrome.exe') == True: 
        chrome_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', True])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Chrome działa')

    if process_exists('chrome.exe') == False: 
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

    save_data_to_file() 
    time.sleep(120) 
