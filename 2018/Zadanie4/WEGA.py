filename = 'przyklad.txt'
filename = 'sygnaly.txt'

#Zadanie4.1
'''print(linia[9], end='')'''
[open('wyniki4.txt', 'a').write(linia[9]) for i,linia in enumerate(open(filename, 'r')) if (i+1)%40 == 0]

#Zadanie4.2
litery_występowanie = []
max = [0]
for linia in open(filename, 'r'):
    linia = linia.strip()
    [litery_występowanie.append(litera) for litera in linia if litera not in litery_występowanie]
    if len(litery_występowanie) > max[0]:
        max.clear()
        max.append(len(litery_występowanie));max.append(linia)
    litery_występowanie.clear()
#print('\n'+str(max))
open('wyniki4.txt', 'a').write('\n'+'\n'+str(max)+'\n')

#Zadanie4.3
for linia in open(filename, 'r'):
    linia = linia.strip()
    for x in range(len(linia)-1):
        for y in range(x+1,len(linia)):
            if (abs((ord(linia[y])-ord(linia[x])))) > 10:
                break
        if (abs((ord(linia[y])-ord(linia[x])))) > 10:
            break
    if (abs((ord(linia[y])-ord(linia[x])))) <= 10:
        #print(linia)
        open('wyniki4.txt', 'a').write('\n'+linia)
