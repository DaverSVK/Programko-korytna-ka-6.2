def vypis(pole):
    for x in pole:
        print(x, end="")
    print()

    return 0

slovo = "Ahoj osveto!"
pole = ["-"]*len(slovo)
print(slovo)
vypis(pole)
## pridal som
uhadol=False
pocetChyb=0
obesenec = [[' ','_','_','_',' '],
            [' ','|',' ','|',' '],
            [' ','|',' ',' ',' '],
            [' ','|',' ',' ',' '],
            [' ','|',' ',' ',' '],
            [' ','|',' ',' ',' '],
            ['_','|','_','_','_'],]

for opak in range(7):
    pismenoZ = input("Zadaj pismeno: ")

    i=0
    for pismenoH in slovo:
        if pismenoH.lower() == pismenoZ.lower():
            pole[i]=pismenoH
            ## pridal som
            uhadol = True
        i=i+1
    ## pridal som
    if uhadol == False:
        pocetChyb= pocetChyb+1
    else:
        uhadol = False
    
    vypis(pole)
    
    for riadok in obesenec:
        for znak in riadok:
            print(znak, end="")
        print()
        
    print(pocetChyb)
