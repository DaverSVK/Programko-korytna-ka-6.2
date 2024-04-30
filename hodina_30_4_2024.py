from random import randint

#funkcia ktorá skontroluje či je platný vstup
def overVstup(hracovTah,mozneTahy):
    if hracovTah not in mozneTahy:
        print("Zlý vstup")
    return hracovTah in mozneTahy

#funkcia, ktorá náhodne vykoná ťah oponenta
def hernyTah(hracovTah):
    vysledok = 0
#---Medzi toto dopisuj moznosti----------
    
#-------------------------------
    if(overVstup(hracovTah.lower(),mozneTahy)):
        moznost = randint(0,2)
        tahOponenta = mozneTahy[moznost]
        if hracovTah.lower()=="kamen" and tahOponenta.lower()=="papier":
            print("Prehra O_O")
            vysledok = -1
        elif hracovTah.lower()=="papier" and tahOponenta.lower()=="noznice":
            print("Prehra O_O")
            vysledok = -1
        elif hracovTah.lower()=="noznice" and tahOponenta.lower()=="kamen":
            print("Prehra O_O")
            vysledok = -1
        elif hracovTah.lower()=="kamen" and tahOponenta.lower()=="noznice":
            print("Výhra ^_^")
            vysledok = 1
        elif hracovTah.lower()=="papier" and tahOponenta.lower()=="kamen":
            print("Výhra ^_^")
            vysledok = 1
        elif hracovTah.lower()=="noznice" and tahOponenta.lower()=="papier":
            print("Výhra ^_^")
            vysledok = 1
        else:
            print("Remíza -_-")
            vysledok = 0
    return vysledok


#---Medzi toto dopisuj----------

#-------------------------------


