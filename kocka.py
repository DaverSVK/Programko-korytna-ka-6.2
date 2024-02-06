from turtle import *
from random import randint 
showturtle()

def stvorec(x, y):
    penup()
    goto(x, y)
    pendown()
    for i in range(4):
        forward(100)
        right(90)
    penup()
    goto(x+45, y-65)
    pendown()
    write(randint(1,6), font=("Arial", 20, "normal"))
onscreenclick(stvorec)
mainloop()
