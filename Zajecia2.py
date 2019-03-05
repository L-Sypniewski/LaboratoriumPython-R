class osoba:
    '''Przykładowa klasa'''

    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def postarz(self, o_ile=1):
        self.wiek += o_ile

    def wypisz(self):
        from datetime import datetime
        rok_biezacy = datetime.now().year
        print("{} {} urodził się w {} roku.".format(
            self.imie, self.nazwisko, rok_biezacy-self.wiek))


class pracownik(osoba):
    ''' Przykład dziedziczenia'''

    def __init__(self, imie, nazwisko, wiek, pensja, stanowisko):
        osoba.__init__(self, imie, nazwisko, wiek)  # Tutaj nie pomijamy "self"
        self.pensja = pensja
        self.stanowiska = [stanowisko]  # lista

    def podwyzka(self, kwota=0):
        self.pensja += kwota

    def awans(self, stanowisko, podwyzka=0):
        self.stanowiska.append(stanowisko)  # Dopisanie do listy
        self.podwyzka(podwyzka)

    def wypisz(self):
        print("{} {} zarabia {} PLN na stanowisku {}.".format(self.imie, self.nazwisko, self.pensja,
                                                              str(self.stanowiska[-1])))

##########   Rozwiazanie   ###########################################

class pracownicy:
    def __init__(self, pracownicy):
        self.pracownicy = pracownicy

    def __dane_pracownikow(self, pracownicy):
        return list(map(lambda p: "{} {}".format(
                p.imie, p.nazwisko), pracownicy))

    def __wyprintuj_rezultat(self, prefix, stanowisko, dane_pracownikow):
        print("{} {}: {}".format(
                prefix, stanowisko, ", ".join(dane_pracownikow)))

    def wypisz_pracownikow(self, stanowisko, obecnie=True):
        if obecnie:
            pracownicy_kiedykolwiek_na_stanowisku = list(
                filter(lambda p: stanowisko in p.stanowiska, self.pracownicy))

            dane_pracownikow = self.__dane_pracownikow(pracownicy_kiedykolwiek_na_stanowisku)

            self.__wyprintuj_rezultat("Pracownicy kiedykolwiek na stanowisku", stanowisko, dane_pracownikow)
        else:
            pracownicy_obecnie_na_stanowisku = list(
                filter(lambda p: p.stanowiska[-1] == stanowisko, self.pracownicy))

            dane_pracownikow = self.__dane_pracownikow(pracownicy_obecnie_na_stanowisku)

            self.__wyprintuj_rezultat("Pracownicy obecnie na stanowisku", stanowisko, dane_pracownikow)


p1 = pracownik("Jerzy", "Nowak", 20, 15000, "programista")
p1.awans("kierownik projektu")
p2 = pracownik("Andrzej", "Iksiński", 20, 15000, "programista")
p3 = pracownik("Waldemar", "Zielony", 20, 7000, "programista")
p4 = pracownik("Jan", "Kowalski", 20, 500, "bezrobotny")

lp = pracownicy([p1, p2, p3, p4])

lp.wypisz_pracownikow("programista")
# Output: Pracownicy obecnie na stanowisku programista: Andrzej Iksiński, Waldemar Zielony

lp.wypisz_pracownikow("programista", obecnie=False)
# Output: Pracownicy kiedykolwiek na stanowisku programista: Jerzy Nowak, Andrzej Iksiński, Waldemar Zielony

# Zadanie
# - Napisać klasę "pracownicy", która będzie przechowywała pracowników,
#   przekazanych w konstruktorze w formie listy
# - Napisać metodę "wypisz_pracownikow", która przyjmuje dwa argumenty:
#   "stanowisko" - nazwa stanowiska do wyświetlenia (argument obowiązkowy)
#   "obecnie" - opcjonalny argument logiczny określający czy metoda powinna wypisać pracowników
#   zatrudnionych obecnie na danym stanowisku (True - wartość domyślna),
#   czy też  pracowników którzy kiedykolwiek pracowali na danym stanowisku (False)
#   Metoda powinna wyświetlić wynik w następującej formie (przykład):
#   a) po wywołaniu .wypisz_pracownikow("programista"):
#   "Pracownicy obecnie na stanowisku programista: Imię Nazwisko, Imię Nazwisko..."
#   a) po wywołaniu .wypisz_pracownikow("programista", obecnie=False):
#   "Pracownicy kiedykolwiek na stanowisku programista: Imię Nazwisko, Imię Nazwisko..."
# - Przetestować działanie klasy i metody na obiekcie złożonym z 3 przykładowych pracowników


#p1 = pracownik("Jerzy", "Nowak", 20, 15000, "programista")
#p1.awans("kierownik projektu")
#p2 = pracownik("Andrzej", "Iksiński", 20, 15000, "programista")
#p3 = pracownik("Waldemar", "Zielony", 20, 7000, "programista")

#lp = pracownicy([p1, p2, p3])

# lp.wypisz_stanowisko("programista")
# Output: Pracownicy obecnie na stanowisku programista: Andrzej Iksiński, Waldemar Zielony

#lp.wypisz_stanowisko("programista", obecnie=False)
# Output: Pracownicy kiedykolwiek na stanowisku programista: Jerzy Nowak, Andrzej Iksiński, Waldemar Zielony
