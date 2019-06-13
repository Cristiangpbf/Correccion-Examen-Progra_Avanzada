from tkinter import *

vent = Tk()

def secuencia(num):
	r = [2] + [x for x in range(3, num+1, 2) if not [y for y in range(3, int(x**0.5)+1, 2) if (float(x) / y).is_integer()]]
	return r

def leer():
	num = int(ingreso.get())
	return num

def mostrar():
	resultado=Label(vent,text=secuencia(leer())).grid(row=3, column=0)

def crear_archivo():
	archivo = open('primos.txt','a')
	archivo.write(str(secuencia(leer())))
	archivo.close()

etiqueta1 = Label(vent, text= 'Calculo numeros primos').grid(row=0, column=0)
etiqueta2 = Label(vent, text='Ingrese un numero: ').grid(row=1,column=0)
ingreso = Entry(vent,text=2)
ingreso.grid(row=1, column=1)
resultado = Label(vent).grid(row=3, column=0)
calcular = Button(vent, text='Calcular', command=mostrar).grid(row=2, column=0)
Guardar = Button(vent, text='Guardar', command=crear_archivo).grid(row=2, column=1)


vent.mainloop()




