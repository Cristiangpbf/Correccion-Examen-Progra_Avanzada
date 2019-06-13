from tkinter import *
from tkinter import ttk
import os

def secuencia():
    os.system("secuencia.py")

def esfera():
    os.system("esfera.py")

def tablero():
    os.system("tablero.py")
    

class menu:

	def __init__(self,ventana):

		self.vent= ventana
		self.vent.title('Menu para aplicaciones')

		frame1 = LabelFrame(self.vent, text='Opciones')
		frame1.grid(row=1, column=0, columnspan=3, rowspan= 3, pady=30, sticky = W + E)

		ttk.Button(frame1, text='Secuencia', command=secuencia).grid(row=2, column=0)
		ttk.Button(frame1, text='Esfera', command=esfera).grid(row=3, column=0)
		ttk.Button(frame1, text='Tablero', command=tablero).grid(row=4, column=0)


ventana=Tk()
app = menu(ventana)
ventana.mainloop()