Zad_1 = 1
Zad_2 = 1
Zad_3 = 1
Zad_4 = 1


plik = open('liczby.txt')

def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

def nwd(a, b): return nwd(b, a%b) if b else a

liczby = []

for liczba in plik.readlines():
    liczby.append(liczba.strip())

if Zad_1:
#Zadanie 4.1
    zlicz = 0

    for x in range(0,2999):
        for y in range(1,3000):
            liczba1 = liczby[x][::-1]
            liczba2 = liczby[y]
            if int(liczba1) == int(liczba2): zlicz = zlicz + 1

    print('Zad4.1: ', zlicz)

if Zad_2:
#Zadanie 4.2

    pary = []

    for x in range(3000):
        liczba1 = int(liczby[x])
        liczba2 = int(liczby[x][::-1])

        if czy_pierwsza(liczba1) and czy_pierwsza(liczba2):
            if liczba1 > liczba2: pary.append((liczba2, liczba1))
            else: pary.append((liczba1, liczba2))

    print('Zad4.2: ', len(sorted(set(pary))), sorted(set(pary)))

if Zad_3:
#Zadanie 4.3

    Liczby = []

    for i in liczby:
        Liczby.append((int(i+i[::-1]),nwd(int(i+i[::-1]),int(i)),nwd(int(i+i[::-1]),int(i[::-1]))))

    print('Zad4.3: ', sorted(set(Liczby)))

if Zad_4:
#Zadanie 4.4

    Liczby = []
    zlicz = 0

    for i in liczby:
        Liczby.append(int(i)+int(i[::-1]))

    Liczby = sorted(set(Liczby))

    kolejne_liczby_trójkątne = []

    for i in range(210):
        suma = (i*(i+1))//2
        kolejne_liczby_trójkątne.append(suma)

    for i in Liczby:
        if i in kolejne_liczby_trójkątne: zlicz = zlicz + 1

    print('Zad4.4: ',zlicz)
