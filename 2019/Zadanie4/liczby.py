filename = 'przyklad.txt'
filename = 'najtrudniejsza opcja.txt'
filename = 'liczby.txt'

def zad1(liczby):
#Zad4.1
    ile_jest_potęgą = 0
    potęgi = []
    potęga = 0
    x = 0
    while True:
        if x > 100000:break
        x = 3**potęga
        potęgi.append(x)
        potęga+=1
    for liczba in liczby:
        if int(liczba) in potęgi:
            ile_jest_potęgą+=1
    return ile_jest_potęgą

def zad2(liczby):

    pełna = 0
    wynik = []
    def sil(n):
        s = 1
        for i in range(2,n+1):
            s*=i
        return s

    for liczba in liczby:
        pełna = 0
        for i in liczba:
            if i == '\n':
                if pełna == int(liczba):
                    wynik.append(int(liczba))
                continue
            pełna+=sil(int(i))
    return wynik

def zad3(liczby):

    def NWD(a, b): return NWD(b, a%b) if b else a

    max_długość = 0
    max_pierwsza = 0
    max_dzielnik = 0

    for i in range(len(liczby)-2):

        długość = 1
        pierwsza = 0
        dzielnik = int(liczby[i])
        for j in range(i, len(liczby)-1):

            if (NWD(dzielnik, int(liczby[j+1]))) != 1:

                długość +=1
                dzielnik = NWD(dzielnik, int(liczby[j+1]))
                if pierwsza == 0:

                    pierwsza = int(liczby[i])
            else: break
        if długość > max_długość:

            max_długość = długość
            max_dzielnik = dzielnik
            max_pierwsza = pierwsza

    return f'\tPierwsza: {max_pierwsza}\n\t\t\tDługość: {max_długość}\n\t\t\tDzielnik: {max_dzielnik}'


liczby = [liczba for liczba in open(filename, 'r')]

open('wyniki4.txt', 'w').write(f'Zadanie4.1: {zad1(liczby)}\nZadanie4.2: {zad2(liczby)}\nZadanie4.3:{zad3(liczby)}')