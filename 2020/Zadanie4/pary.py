filename = 'przyklad.txt'
filename = 'pary.txt'

def czy_pierwsza(n):#Czy podana n jest liczbą pierwszą?
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

wynik1 = ''
wynik2 = ''
wynik3 = ''

#Zad4.3
równe_sobie = []

for linia in open(filename, 'r'):
    linia = linia.strip().split(' ')#Oddzielanie liczby od ciągu
    liczba, ciąg = int(linia[0]), linia[1]

    #Zad4.1
    max = 0
    for x in range(3,101):
        if liczba%2 == 0 and czy_pierwsza(x) and czy_pierwsza(liczba-x) and x<=liczba-x:
            #print(liczba, x, liczba-x)
            wynik1 += str(liczba)+' '+str(x)+' '+str(liczba-x)+'\n'
            break

    #Zad4.2
    poprzednia = 0
    długość = 1
    max_długość = 0
    max_poprzednia = 0
    for x in ciąg:
        if poprzednia == 0:
            poprzednia = x
        elif poprzednia == x:
            długość+=1
        if poprzednia != x:
            długość = 1
        elif długość > max_długość:
            max_poprzednia = poprzednia
            max_długość = długość

        poprzednia = x
    wynik2 += str(max_poprzednia*max_długość)+' '+str(max_długość)+'\n'

    #Zad4.3
    if len(ciąg) == liczba:
        równe_sobie.append([liczba, ciąg])

poprzednia = 0
najmniejsza = 0
for x in równe_sobie:
    if poprzednia == 0:
        poprzednia = x
    elif -(poprzednia[0]) < x[0] or -(poprzednia[0]) == x[0] and poprzednia[1] < x[1]:
        najmniejsza = x
    poprzednia = x
wynik3 += str(najmniejsza[0])+' '+str(najmniejsza[1])

open('wyniki4.txt', 'w').write(wynik1+'\n'+wynik2+'\n'+wynik3)