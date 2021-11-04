obraz = []
for line in open('dane.txt', 'r'):
    obraz.append(line.strip().split(' '))

def zbadaj_obraz(obraz):

#Zadanie6.1
    najjaśniejszy_piksel = int(obraz[0][0])
    najciemniejszy_piksel = int(obraz[0][0])

    for wiersz in range(200):
        for kolumna in range(320):
            if int(obraz[wiersz][kolumna]) > int(najjaśniejszy_piksel):
                najjaśniejszy_piksel = obraz[wiersz][kolumna]
            if int(obraz[wiersz][kolumna]) < int(najciemniejszy_piksel):
                najciemniejszy_piksel = obraz[wiersz][kolumna]

#Zadanie6.2
    licznik = 0
    for wiersz in obraz:
        if wiersz != wiersz[::-1]: licznik +=1
    print(licznik,)

#Zadanie6.3
    liczba_pikseli__k = 0
    for x in range(200):
        for y in range(320):
            pixel = obraz[x][y]
            chociaz_jeden = 0

            if x > 0 and abs(int(pixel) - int(obraz[x-1][y])) > 128:
                chociaz_jeden=1

            if x < 199 and abs(int(pixel) - int(obraz[x+1][y])) > 128:
                chociaz_jeden=1

            if y > 0 and abs(int(pixel) - int(obraz[x][y-1])) > 128:
                chociaz_jeden=1

            if y < 319 and abs(int(pixel) - int(obraz[x][y+1])) > 128:
                chociaz_jeden=1

            liczba_pikseli__k+=chociaz_jeden

#Zadanie6.4
    długość = 1
    najdłuższy = 0
    for y in range(320):
        for x in range(200):
            if x != 199 and int(obraz[x][y])==int(obraz[x+1][y]): długość+=1
            elif długość > najdłuższy:
                najdłuższy=długość
                długość=1
            else: długość=1

    return(najciemniejszy_piksel, najjaśniejszy_piksel, licznik, liczba_pikseli__k, najdłuższy)


wyniki = zbadaj_obraz(obraz)
wynik6_1_1 = wyniki[0]
wynik6_1_2 = wyniki[1]
wynik6_2 = wyniki[2]
wynik6_3 = wyniki[3]
wynik6_4 = wyniki[4]

print(f'Zadanie6.1: Najciem.:{wynik6_1_1} Najjaśn.:{wynik6_1_2}\nZadanie6.2: {wynik6_2}\nZadanie6.3 {wynik6_3}\nZadanie6.4: {wynik6_4}')
