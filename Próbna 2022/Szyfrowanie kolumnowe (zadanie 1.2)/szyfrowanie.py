plik = open("tekst.txt")
tekst = plik.read()

def szyfrowanie(tekst):
    N = 10
    table = [[] for _ in range(N)]

    x = 0
    y = 0

    while(y<N):
        while(len(table[y])<N):
            try:
                table[y].append(tekst[x])
            except:
                table[y].append('X')
            x = x + 1
        y = y + 1

    for x in range(N):
        for y in range(N):
            print(table[y][x], end="")

szyfrowanie(tekst)

