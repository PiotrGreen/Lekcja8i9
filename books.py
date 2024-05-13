'''
NAME
    books

DESCRIPTION
    Moduł umożliwia dodawanie książek do pliku csv lub ich usuwanie z tego pliku.

FUNCTIONS
    Moduł ten zawiera następujące funkcje:
    * dodaj_ksiazke() - funkcja przyjmuje dane książki, sprawdza czy podana książka nie jest już w bazie
    jeśli nie to jest dodawana.
    * usun_ksiazke() - użytkownik podaje według czego chce usunać książke i podaje te dane, funkcja sprawdza czy podane
    dane są w pliku csv jesli tak to je usuwa.

EXAMPLES
    dodaj_ksiazke(id=7432, autor="Adam Mickiewicz", tytul="Pan Tadeusz", liczba_stron=300, data_dodania="2024-05-06")
    usun_ksiazke(identyfikator=4352, opcja="id")
'''

import csv


def dodaj_ksiazke(id, autor, tytul, liczba_stron, data_dodania):
    """
    Sprawdz czy książka nie jest już w bazie jeśłi nie to zapisuje ją do pliku CSV.

    Args:
        id (int): Identyfikator książki.
        autor (str): Autor książki.
        tytul (str): Tytuł książki.
        liczba_stron (int): Liczba stron książki.
        data_dodania (date): Data dodania ksiązki do bazy.
    """

    def sprawdzdane(id, autor, tytul, liczba_stron, data_dodania):
        with open('book.csv', 'r') as file1:
            read = list(csv.reader(file1))
        for i in read:
            if i[0] == str(id):
                print("Błąd id jest już w bazie. ")
                return False
            elif i[2] == tytul:
                print("Błąd tytuł jest już w bazie. ")
                return False
        return True

    def zapiszdane(id, autor, tytul, liczba_stron, data_dodania):
        try:
            with open('book.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([id, autor, tytul, liczba_stron, data_dodania])
            print("Książka dodana pomyślnie do bazy.")
        except ValueError as e:
            print("ValueError exception:", e)
        except TypeError as e:
            print("TypeError exception:", e)
        except IOError as e:
            print("IOError exception:", e)

    if sprawdzdane(id, autor, tytul, liczba_stron, data_dodania):
        zapiszdane(id, autor, tytul, liczba_stron, data_dodania)
    else:
        print("Nieprawidłowe dane. Nie mogą zostać zapisane.")


def usun_ksiazke(identyfikator, opcja):
    """
    Usuwa książkę z bazy na podstawie ID lub tytułu.

    Args:
        identyfikator (str or int): ID lub tytuł książki do usunięcia.
        opcja (str): 'id' lub 'tytuł'.
    """
    try:
        with open('book.csv', 'r', newline='', encoding='utf-8') as file:
            rows = list(csv.reader(file))

        if opcja == 'id':
            for row in rows:
                if row[0] == str(identyfikator):
                    rows.remove(row)
                    print('Książka pomyślnie usunięta wg id.')
                    break
        elif opcja == 'tytuł':
            for row in rows:
                if row[2] == str(identyfikator):
                    rows.remove(row)
                    print('Książka pomyślnie usunięta wg tytułu.')
                    break
        else:
            print("Nieprawidłowa opcja.")

        with open('book.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except FileExistsError:
        print("Brak pliku")
