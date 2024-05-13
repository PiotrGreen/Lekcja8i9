import csv
import random
import os
import globals
from datetime import date


def rejestracja(corobic):
    if corobic == "dodać klienta":
        imie = input("Podaj imię i nazwisko: ")
        email = input("Podaj adres e-mail: ")
        telefon = input("Podaj numer telefonu: ")
        ulica = input("Podaj ulice: ")
        miasto = input("Podaj miasto: ")
        kraj = input("Podaj kraj ")
        return imie, email, telefon, ulica, miasto, kraj
    elif corobic == "usunąć klienta":
        imie = input("Podaj imię i nazwisko: ")
        usun_klienta(imie, "imie_nazwisko")



moja_sciezka = "C:\\Users\\Pk\\PycharmProjects\\Lekcja 8 i 9\\Biblioteka\\DATABASE"


def dodaj_klienta(fun):
    imie, email, telefon, ulica, miasto, kraj = fun
    ids = random.randint(1000, 9999)
    data = date.today()
    with open('customer.csv', 'r') as file:
        read = list(csv.reader(file))
    for i in read:
        if i[0] == ids:
            print("Błąd Id jest już w bazie danych.")
            break
        elif i[1] == imie:
            print("Błąd podane imie i nazwisko jest w bazie.")
            break
        elif i[2] == email:
            print("Błąd podany email jest w bazie")
            break
        elif i[3] == telefon:
            print("Błąd podany telefon jest w bazie")
            break

    with open('customer.csv', 'a', newline='', encoding='utf-8') as file1:
        writer = csv.writer(file1)
        writer.writerow([ids, imie, email, telefon, data])

    with open('address.csv', 'a', newline='', encoding='utf-8') as file2:
        write = csv.writer(file2)
        write.writerow([ids, ulica, miasto, kraj])
    print("Nowy klient dodany do bazy.")

    filepath = os.path.join(moja_sciezka, '{}.txt'.format(ids))
    with open(filepath, 'w') as file3:
        file3.write("Wypożyczone książki czytelnika o id: {}\n".format(ids))


a = globals.a


def usun_klienta(identyfikator, opcja):
    """
    Usuwa klienta z bazy na podstawie ID lub tytułu.

    Args:
        identyfikator (str): ID lub imie klienta do usunięcia.
        opcja (str): 'id' lub 'imie_nazwisko'.
    """
    global a
    with open('customer.csv', 'r', newline='', encoding='utf-8') as file:
        custom = list(csv.reader(file))

    with open('address.csv', 'r', newline='', encoding='utf-8') as file:
        adres = list(csv.reader(file))

    if opcja == 'id':
        for row in custom:
            if row[0] == str(identyfikator):
                custom.remove(row)
                print("Klient pomyślnie usunięty z bazy customers.")
        for row in adres:
            if row[0] == str(identyfikator):
                adres.remove(row)
                print("Klient pomyślnie usunięty z bazy adresów.")
                break
    elif opcja == 'imie_nazwisko':
        for row in custom:
            if row[1] == str(identyfikator):
                custom.remove(row)
                a = row[0]
                print('Klient pomyślnie usunięty z bazy customers')
        for row in adres:
            if row[0] == a:
                adres.remove(row)
                print("Klient pomyślnie usunięty z bazy adresów.")
                break
    else:
        print("Nieprawidłowa opcja.")

    with open('customer.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(custom)

    with open('address.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(adres)


def wypozycz(idklient, *tytul):
    """
    Funkcja sprawdza czy jest dostępna książka i jeśli jest umożliwia jej wypożyczenie.
    Args:
        idklient (str): Id klienta który chce wypożyczyć.
        *tytul (str): Tytuły wypożyczanych książek

    Returns: Zapisuje do pliku wypożyczone książki

    """
    try:
        with open('book.csv', 'r', newline='', encoding='utf-8') as file:
            books = list(csv.reader(file))
        for ksiazka in tytul:
            for row in books:
                if ksiazka == row[2]:
                    filepath = os.path.join(moja_sciezka, '{}.txt'.format(idklient))
                    with open(filepath, 'a', newline='') as file1:
                        file1.write("Wypożyczono książkę {} dnia {}\n".format(ksiazka, date.today()))
                    print("Udane wypożyczenie.")
    except ValueError as e:
        print("ValueError exception:", e)
    except TypeError as e:
        print("TypeError exception:", e)
    except IOError as e:
        print("IOError exception:", e)


def udekoruj(funkcja):
    def wrapper(klient, *tytuly):
        print("Witaj w systemie zwrotu książek.")
        for tytul in tytuly:
            funkcja(klient, tytul)
    return wrapper


@udekoruj
def zwrot(idklient, tytul):
    filepath = os.path.join(moja_sciezka, '{}.txt'.format(idklient))
    with open(filepath, 'r') as file1:
        text = file1.read()
        words = text.split()
        for word in words:
            if word == tytul:
                with open(filepath, 'a', newline='') as file2:
                    file2.write("Zwrócono książke {} dnia {}\n".format(tytul, date.today()))
                print("Udany zwrot książki.")
        print("Nie posiadasz {} książki".format(tytul))

