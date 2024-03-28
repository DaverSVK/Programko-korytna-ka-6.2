def vypis(pole):
    for x in pole:
        print(x, end="")
    print()

    return 0

slovo = "Ahoj osveto!"
pole = ["-"]*len(slovo)
print(slovo)
vypis(pole)

for opak in range(7):
    pismenoZ = input("Zadaj pismeno: ")

    i=0
    for pismenoH in slovo:
        if pismenoH == pismenoZ:
            pole[i]=pismenoZ
        i=i+1

    vypis(pole)
