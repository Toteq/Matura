plik = open('instrukcje.txt', 'r')
wiersze = plik.readlines()

def zakoduj_napis(instrukcjie):


    napis = ''#Zadanie1 i Zadanie4

    max_instrukcja =''#Zadanie2
    max_instrukcja_dlugość=0
    aktualna_instrukcja =''
    poprzednia_instrukcja =wiersze[0].strip().split(' ')[0]
    aktualana_instrukcjia_dlugość=1

    max_litera =''#Zadanie3
    max_litera_wystąpienia = 0
    alfabet = {}#Tworzenie słownika z literami alfabetu
    for i in range(65, 91):
        alfabet[chr(i)] = 0



    for instrukcja in instrukcjie:
        instrukcja = instrukcja.strip().split(' ') #usuwa białe znaki i rozdziela na liste według spacji

        polecenie, wartość = instrukcja #to samo co: polecenie = instrukcja[0];wartość = instrukcja[1]

        if polecenie == 'DOPISZ':
            napis += wartość
            alfabet[wartość] +=1
        elif polecenie == 'ZMIEN':
            napis = list(napis)
            napis[-1] = wartość
            napis = ''.join(napis)#Łączenie do stringu
        elif polecenie == 'USUN':
            napis = list(napis)
            napis.pop(-1)
            napis = ''.join(napis)#Łączenie do stringu
        else:#PRZESUN
            indeks_litery = napis.index(wartość)#Szukamy index pierwszego napotkanego znaku wartość

            ascii_litery = ord(wartość)+1#Przesuwamy litere "wartość" o jeden
            if ascii_litery > 90:#Jeżeli jest to "Z" to przesuwamy ją na A
                ascii_litery -= 26

            napis = list(napis)
            napis[indeks_litery] = chr(ascii_litery)#Zamieniamy litere
            napis = ''.join(napis)

        if polecenie == poprzednia_instrukcja:
            aktualana_instrukcjia_dlugość +=1
        else:
            if aktualana_instrukcjia_dlugość > max_instrukcja_dlugość:
                max_instrukcja = aktualna_instrukcja
                max_instrukcja_dlugość = aktualana_instrukcjia_dlugość
            aktualna_instrukcja = polecenie
            aktualana_instrukcjia_dlugość = 1
        poprzednia_instrukcja = polecenie

        for litera in alfabet:
            if alfabet[litera] > max_litera_wystąpienia:
                max_litera = litera
                max_litera_wystąpienia = alfabet[litera]




    return napis, max_instrukcja, max_instrukcja_dlugość, max_litera, max_litera_wystąpienia

wyniki = zakoduj_napis(wiersze)

wynik1 = len(wyniki[0])
wynik2 = wyniki[1],wyniki[2]
wynik3 = wyniki[3],wyniki[4]
wynik4 = wyniki[0]

print('Zadanie4.1: {0}\nZadanie4.2: {1}\nZadanie4.3: {2}\nZadanie4.4: {3}'.format(wynik1, wynik2, wynik3, wynik4))

