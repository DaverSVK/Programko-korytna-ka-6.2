def vypis(pole):
    for x in pole:
        print(x, end="")
    print()

    return 0
##-------------

def sibenica(obesenec,chyby):
    if chyby == 1:
        obesenec[2][3]="O"
    if chyby == 2:
        obesenec[3][3]="|"
    if chyby == 3:
        obesenec[3][2]="/"
    if chyby == 4:
        obesenec[3][4]="\\"
    if chyby == 5:
        obesenec[4][2]="/"
    if chyby == 6:
        obesenec[4][4]="\\"
# toto sa bude menit 4-----

# -------------------------
slovo = "Ahoj osveto!"
pole = ["-"]*len(slovo)
print(slovo)
vypis(pole)

uhadol=False
pocetChyb=0
obesenec = [[' ','_','_','_',' '],
            [' ','|',' ','|',' '],
            [' ','|',' ',' ',' '],
            [' ','|',' ',' ',' '],
            [' ','|',' ',' ',' '],
            [' ','|',' ',' ',' '],
            ['_','|','_','_','_'],]
# toto sa bude menit 1-----

# -------------------------
# toto sa bude menit 2-----
for opak in range(7):
# -------------------------
    pismenoZ = input("Zadaj pismeno: ")

    i=0
    for pismenoH in slovo:
        if pismenoH.lower() == pismenoZ.lower():
            pole[i]=pismenoH
            uhadol = True
        i=i+1
    if uhadol == False:
        pocetChyb= pocetChyb+1
    else:
        uhadol = False
    
    vypis(pole)
    sibenica(obesenec,pocetChyb)

    
    for riadok in obesenec:
        for znak in riadok:
            print(znak, end="")
        print()
        
    print(pocetChyb)

    if pocetChyb == 6:
        print("Konec")
        break
# toto sa bude menit 3-----

# -------------------------
