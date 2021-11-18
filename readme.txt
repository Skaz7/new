playtimecheck.py:
v0.10 - działa sprawdzanie czy proces jest aktualnie uruchomiony i zapisywanie do słownika w postaci 'Godzina: uruchomiony'.
v0.20 - Dodano opcję ukrywania programu. Zmiana dekodowania procesu na utf-16 z powodu zwracanego wcześniej błędu dekodowania.
        Dodano plik z rozszerzeniem .pyw - ukrywa konsolę w trakcie wykonywania programu
v0.30 - Dodano sprawdzanie kilku kolejnych programów jednocześnie (chrome, notepad, ToDo) 
        i zapisanie wspólnego słownika do pliku .json
v0.40 - zmieniony sposób zapisu danych do pliku .json, zamiast słowników ze stanami uruchomienia programów zagnieżdżonych
        w słownikach z nazwami programów, teraz są listy ze stanami uruchomienia programów zagnieżdżone w słownikach 
        nazw programów. Pozwoliło to na zmianę formatu zapisu daty ze string na datetime.
#ToDo:
      - przesłanie pliku ze słownikiem na adres mailowy.


analysis.py:
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