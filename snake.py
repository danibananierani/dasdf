from tkinter import *
import random 


SCREENSIZE = 500
SCREENHEIGHT = 500
PIXEL = 20
D_LENGTH = 3
SPEED = 100

direction = "down"
class Snake:
    global direction, score
    def __init__(self,c):
        
        self.coordinates = []
        self.würfel = []
        
        for i in range (D_LENGTH ):
            self.coordinates.append([0,0])
            
        for x,y in self.coordinates:
            square = c.create_rectangle(x,y, x+ PIXEL, y+ PIXEL)
            self.würfel.append(square)

    

    
def drehen(neu):
    global direction
    if neu == "right" :
        if direction != "left" :
            direction = neu
    if neu == "up" :
        if direction != "down":
           direction = neu
    if neu == "down" :
        if direction != "up":
           direction = neu
    if neu == "left" :
        if direction != "right":
           direction = neu
    
class Apfel:
    
    def __init__(self, c):
        self.color = random.randint(0, 16777215)
        self.ortx = random.randint(0, (SCREENSIZE/PIXEL-1)) * PIXEL
        self.orty = random.randint(0, (SCREENHEIGHT/PIXEL -1)) * PIXEL
        self.coordinates = [self.ortx, self.orty]
        farbe = hex(self.color)
        self.farbe = "#" + farbe[3:6]
        
        
        
        
        c.create_oval( self.ortx, self.orty, self.ortx + PIXEL, self.orty + PIXEL, fill=self.farbe, tag="a")
        
def richtung(s,a):
    global direciton, score
    x, y = s.coordinates[0]
    
       
    if direction == "down":
        y += PIXEL
    elif direction == "up":
        y -= PIXEL
    elif direction == "left":
        x -= PIXEL
    elif direction == "right":
        x += PIXEL
    
    if y == a.orty and x == a.ortx:
        score += 1
        
        l.config(text=f"Score: {score}")
        c.delete("a")
        a = Apfel(c)
    else:
        del s.coordinates[-1]
        c.delete(s.würfel[-1])
        del s.würfel[-1]
    
    s.coordinates.insert(0, [x,y])    
    square = c.create_rectangle(x, y, x+ PIXEL, y + PIXEL, fill=a.farbe)
    s.würfel.insert(0, square)
    
    if  x<0 or x>= SCREENSIZE or y<0 or y>= SCREENHEIGHT or s.coordinates[0] == s.coordinates[1:] :
        c.delete(ALL)
        c.create_text(SCREENSIZE/2, SCREENHEIGHT/2,text="DU DUMMER HUAN HAST VERLOREN", font="Helvetica 18 bold", fill="#af305a")
    
    w.after(SPEED, richtung, s,a)
     
def restart():
    w.update()
    
    
w = Tk()
w.title("Snake")
w.resizable(False, False)
score = 0
direction = "down"
c = Canvas(w, bg="grey", height= SCREENHEIGHT, width=SCREENSIZE)


    
l = Label(w, text=f"Score: {score}")

l.pack()
c.pack()
for i in range(0,SCREENHEIGHT, PIXEL):
    c.create_line(0,i, SCREENSIZE, i, fill="#aaaaaa")
for j in range(0,SCREENSIZE, PIXEL):
    c.create_line(j,0, j,SCREENHEIGHT,fill= "#aaaaaa")
w.bind("<Left>", lambda event: drehen("left"))
w.bind("<Right>", lambda event: drehen("right"))
w.bind("<Up>", lambda event: drehen("up"))
w.bind("<Down>", lambda event: drehen("down"))
w.bind("a", lambda event: drehen("left"))
w.bind("d", lambda event: drehen("right"))
w.bind("w", lambda event: drehen("up"))
w.bind("s", lambda event: drehen("down"))
w.bind("r", lambda event: restart())
a = Apfel(c)
s = Snake(c)


richtung(s,a)

w.mainloop()

