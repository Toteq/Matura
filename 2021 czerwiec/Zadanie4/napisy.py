filename = 'napisy.txt'
#filename = 'przyklad.txt'

##4.1
zlicz = 0

for line in open(filename).readlines():
    for i in line:
        if i.isdigit():
            zlicz = zlicz + 1
print('Zad41: ',zlicz)

##4.2
hasło = []
zlicz = 1

for line in open(filename).readlines():
    if zlicz%20 == 0:
        hasło.append(line[(zlicz//20)-1])
    zlicz = zlicz + 1
print('Zad42: ',''.join(hasło))

##4.3
napis = ''
hasło = []

for line in open(filename).readlines():
    napis = line.strip()
    if len(napis) == 50:

        if (napis + napis[0])[::-1] == napis + napis[0]:
            napis = napis + napis[0]
            hasło.append(napis[len(napis)//2])
            continue
        if (napis[-1] + napis)[::-1] == napis[-1] + napis:
            napis = napis[-1] + napis
            hasło.append(napis[len(napis)//2])
            continue
print('Zad43: ',''.join(hasło))

##4.4
hasło = ''
iksy = 0
for line in open(filename).readlines():
    napis = line.strip()
    cyfry = []

    for i in napis:
        if i.isdigit():
            cyfry.append(i)
    if not len(cyfry)%2 == 0:
        cyfry.remove(cyfry[-1])
    for liczba in [(cyfry[x]+cyfry[x+1]) for x in range(0,len(cyfry)-1,2)]:
        if iksy == 3: break
        liczba = int(liczba)
        if liczba <= 90 and liczba >= 65:
            if chr(liczba) == 'X': iksy = iksy + 1
            hasło = hasło + chr(liczba)
print('Zad44: ',hasło)
