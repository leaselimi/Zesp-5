# Gra Ultimate Tic-Tac-Toe

Rozbudowana wersja klasycznej gry w kółko i krzyżyk, zaprojektowana dla dwóch graczy. Składa się z dziewięciu plansz do gry w kółko i krzyżyk ułożonych w siatkę 3 × 3. W grze Ultimate Tic Tac Toe zasady dotyczące tego, gdzie przeciwnik musi zagrać w swoim ruchu, wynikają z ruchu wykonanego przez poprzedniego gracza. 

Oto szczegółowe wyjaśnienie:
- Zasada dotycząca ruchu:
Każdy ruch odbywa się na jednej z 9 mniejszych plansz, które razem tworzą większą planszę 3x3.
Pole, na które gracz postawi swój symbol (X lub O) na małej planszy, wskazuje pole na dużej planszy, na której przeciwnik musi zagrać w swoim następnym ruchu.
* Dodatkowo ! 
Jeśli gracz wykonuje ruch, który wskazuje na małą planszę już całkowicie wypełnioną (lub wygraną), przeciwnik ma wolny wybór i może zagrać w dowolnej z dostępnych (niewypełnionych) małych plansz.

W Ultimate Tic Tac Toe istotne jest, aby nie tylko próbować wygrać swoją małą planszę, ale także kontrolować ruchy przeciwnika, wymuszając ich grę na mniej korzystnych planszach. Gracze grają na zmianę na mniejszych planszach do gry w kółko i krzyżyk, **dopóki jeden z nich nie wygra na większej planszy.**


## Opis projektu
Gra polega na połączeniu zasad klasycznego kółka i krzyżyka z nowymi regułami, wprowadzającymi większe plansze, strategie. Projekt został stworzony przez siedmioosobowy zespół.


## Funkcje
- Gra dla 2 graczy
- Tryb jednoosobowy (gra z botem)

## Technologie
- Python 3.11
- GitHub (do wersjonowania kodu)

## Instalacja

Jak zagrać?
Aby zagrać w **Ultimate Kółko i Krzyżyk**, wykonaj poniższe kroki:

1. **Sklonuj repozytorium** na swój komputer:
   ```bash
   git clone https://github.com/leaselimi/Zesp-5.git
   cd Zesp-5
2. pip install -r requirements.txt
3. python main.py
4. Wybierz dowolną opcję gry: gra z botem / 1v1.



## Zespół
<a href="https://github.com/leaselimi/Zesp-5/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=leaselimi/Zesp-5" />
</a>

Made with [contrib.rocks](https://contrib.rocks).


## Credits
Muzyka:
- "3KIPA" by EKIPA ([https://www.youtube.com/watch?v=3jHcWlO6PIw](https://youtu.be/RjRnxs0edZs?si=sKMD_wvnXt_STe0c))

Zasady gry:
- Wikipedia (https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe)
  
- Contributor graph jest stworzony przuy użyciu contrib.rocks.(https://contrib.rocks/preview?repo=angular%2Fangular-ja)

## Licencja
Projekt jest objęty licencją [GNU GPLv3](LICENCJA).
