import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

Satalite = []
Lines =[]
Next_Satalite = 0

Start_Time = 0
Total_Time = 0
End_Time = 0

Number_Of_Satalites = 8

def create_Satalites():
    global Start_Time
    for count in range (0,Number_Of_Satalites):
        space_craft = Actor("satalite")
        space_craft.pos = randint(40,WIDTH - 40), randint(40,HEIGHT - 40)
        Satalite.append(space_craft)
    Start_Time = time()

def draw():
    global Total_Time
    screen.blit("space",(0,0))
    Number = 1
    for space_craft in Satalite:
        screen.draw.text(str(Number),(space_craft.pos[0],space_craft.pos[1]+20))
        space_craft.draw()
        Number = Number+1
    for Line in Lines:
        screen.draw.line(Line[0],Line[1],("white"))
        if Next_Satalite<Number_Of_Satalites:
            Total_Time = time - Start_Time
            screen.draw.text(str(round(Total_Time,1)),(10,10), fontsize=30)
        else:
            screen.draw.text(str(round(Total_Time,1)),(10,10), fontsize=30)

def update():
    pass

def on_mouse_down(pos):
    global Next_Satalite,Lines
    if Next_Satalite < Number_Of_Satalites:
        if Satalite[Next_Satalite].collidepoint(pos):
            if Next_Satalite:
                Lines.append((Satalite[Next_Satalite-1].pos, Satalite[Next_Satalite].pos))
            Next_Satalite = Next_Satalite + 1
        else:
            Lines = []
            Next_Satalite = 0

create_Satalites()

pgzrun.go()
