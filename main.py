from books import *
from customers import *
import random
from datetime import date
import globals
nowy_klient = globals.nowy_klient


def main1():
    global nowy_klient
    while 1:
        co_robic = input("Co chesz zrobić? \n"
                         "1 Dodać książkę. \n"
                         "2 Usunać książkę. \n"
                         "3 Rejestracja lub usunięcie klienta. \n"
                         "4 Dodanie klienta. \n"
                         "5 Usunięcie klienta. \n"
                         "6 Wypożyczenie książki. \n"
                         "7 Zwrot książki. \n"
                         "8 Wyjście.  ")
        if co_robic == "1":
            id1 = random.randint(1000, 9999)
            autor = input("Podaj autora. ")
            tytul = input("Podaj tytuł. ")
            liczba_stron = int(input("Podaj liczbe stron. "))
            data_dodania = date.today()
            dodaj_ksiazke(id1, autor, tytul, liczba_stron, data_dodania)
        elif co_robic == "2":
            opcja = input("Według czego usunać książke id lub tytuł? ")
            identyfikator = input("Co wybrałes to to podaj. ")
            usun_ksiazke(identyfikator, opcja)
        elif co_robic == "3":
            akcja = input("Dodać klienta czy usunąć klienta? ")
            nowy_klient = rejestracja(akcja)
        elif co_robic == "4":
            dodaj_klienta(nowy_klient)
        elif co_robic == "5":
            opcja1 = input("Według czego usunać klienta id lub imie_nazwisko? ")
            identyfikator1 = input("Co wybrałes to to podaj. ")
            usun_klienta(identyfikator1, opcja1)
        elif co_robic == "6":
            idklienta = input("Podaj id klienta który chce wypożyczyć książke.")
            tytuly = input("Podaj tytuły książek oddzielone przecinkem: ").split(',')
            wypozycz(idklienta, *tytuly)
        elif co_robic == "7":
            idklienta1 = input("Podaj id klienta który chce zwrócić książki.")
            tytuly1 = input("Podaj tytuły książek oddzielone przecinkem: ").split(',')
            zwrot(idklienta1, *tytuly1)
        elif co_robic == "8":
            break


if __name__ == "__main__":
    main1()
