from tkinter import *

main=Tk()

def leer():
    num = int(dato.get())
    return num

def esfera_dibujo():
    rad=leer()
    vent=Tk()
    ventana = Canvas(vent, width=500, height=500)
    ventana.pack()
    ventana.create_oval(250-2*rad, 250-2*rad, 250+2*rad, 250+2*rad)

def calculos():
    res_area = 'El area es: '+str(4*3.1416*(leer()**2))
    res_vol = 'El volumen es: '+str(3.1416*(leer()**3)*4/3)
    res_fin = res_area+'__'+res_vol
    return res_fin

def mostrar():
    resultado = Label(main, text=calculos())
    resultado.grid(row=3,column=0)

etiqueta = Label(main, text='Area y Volumen de una esfera').grid(row=0,column=0)
etiqueta_datos =Label(main, text='Ingresar el radio de la esfera:    ').grid(row=1,column=0)
dato = Entry(main, text=' ')
dato.grid(row=1, column=1)
boton1 = Button(main, text='Calcular', command=mostrar).grid(row=2,column=0)
boton2 = Button(main, text='Graficar', command=esfera_dibujo).grid(row=2,column=1)



main.mainloop()
