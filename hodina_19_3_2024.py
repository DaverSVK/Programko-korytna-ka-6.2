def vypisGaraze(garaz):
  for auto in garaz:
    print(auto,end=", ")
  print()

otcovaGaraz=["Bugatti", "Rols Royce", "Žigulak"]
mojaGaraz=["Ferrari","Porshe"]
maminaGaraz=["BMW","Cooper","Golf"]


print("Otec")
vypisGaraze(otcovaGaraz)
  
print("Ja")
vypisGaraze(mojaGaraz)
  
print("Mama")
vypisGaraze(maminaGaraz)

rozhod = input("S kým si chces vymennit auto? (mama,otec): ")
if rozhod == "mama":
    autoVym1 = input("Ktoré auto?")
    autoVym2 = input("Za ktoré auto?")
    maminaGaraz.remove(autoVym1)
    maminaGaraz.append(autoVym2)
    mojaGaraz.remove(autoVym2)
    mojaGaraz.append(autoVym1)
    print("Hotovo")
if rozhod == "otec":
    autoVym1 = input("Ktoré auto?: ")
    autoVym2 = input("Za ktoré auto?: ")
    otcovaGaraz.remove(autoVym1)
    otcovaGaraz.append(autoVym2)
    mojaGaraz.remove(autoVym2)
    mojaGaraz.append(autoVym1)
    print("Hotovo")
    
print("Ja")
vypisGaraze(mojaGaraz)
