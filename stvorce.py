from turtle import *
showturtle()

def stvorec(dlzka):
    for x in range(4):
        forward(dlzka)
        left(90)
penup()
goto(-400,0)
pendown()

for x in range(6):
    stvorec(x*50)
    penup()
    forward(x*50+10)
    pendown()
