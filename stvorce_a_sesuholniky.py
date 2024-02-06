from turtle import *
showturtle()
#funkcia pre sesťuholnik
def sestuholnik(dlzka):
    for x in range(6):
        forward(dlzka)
        left(60)
#funkcia pre štvorec
def stvorec(dlzka):
    for x in range(4):
        forward(dlzka)
        left(90)
#posun pera na kraj
penup()
goto(-400,0)
pendown()

#hlavná časť čo volá na striedačku kocku a štvorec
for x in range(6):
  #ak x modulo čize zostatok po delení rovný nule (čize ak x párne) tak vykreslí sestuholnik inak stvorec
    if x%2 == 0:
        sestuholnik(50)
    else:
        stvorec(50)
      #posun dalšieho tvaru
    penup()
    forward(100)
    pendown()
