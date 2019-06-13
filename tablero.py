from tkinter import *
import time

i=(0,1,2,3,4,5,6,7)
ind=0;
tk = Tk()
canvas = Canvas(tk,width=800, height=800)
canvas.pack()

def crear_tablero():    
    for x in range(32):
        canvas.create_rectangle(0,0,100,100, fill='black')        
    for a in range(4):
        canvas.move(a+1,(a)*200,0)
    for b in range(4):
        canvas.move(b+5,(b+(b+1))*100,100)
    for a in range(4):        
        canvas.move(a+9,(a)*200,200)
    for b in range(4):
        canvas.move(b+13,(b+(b+1))*100,300)
    for a in range(4):        
        canvas.move(a+17,(a)*200,400)
    for b in range(4):
        canvas.move(b+21,(b+(b+1))*100,500)
    for a in range(4):        
        canvas.move(a+25,(a)*200,600)
    for b in range(4):
        canvas.move(b+29,(b+(b+1))*100,700)

crear_tablero()

ficha = PhotoImage(file='ficha.png')

canvas.create_image(25,0, anchor=NW, image=ficha)

def moverFicha(event):

    if event.keysym == 'Up':
        canvas.move(33, 0, -5)
        print(canvas.coords(33))

    elif event.keysym == 'Down':
        canvas.move(33, 0, 5)
        print(canvas.coords(33))
    elif event.keysym == 'Left':
        canvas.move(33, -5, 0)
        print(canvas.coords(33))
    else:
        canvas.move(33, 5, 0)
        print(canvas.coords(33))



canvas.bind_all('<KeyPress-Up>', moverFicha)
canvas.bind_all('<KeyPress-Down>', moverFicha)
canvas.bind_all('<KeyPress-Left>', moverFicha)
canvas.bind_all('<KeyPress-Right>', moverFicha)

tk.mainloop()