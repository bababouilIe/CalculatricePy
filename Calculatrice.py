from tkinter import *
import tkinter as tk

def addition(nombre)-> None:
    nombre2=e.get()

    nombre=(nombre+nombre2)
    

def soustraire(nombre,nombre2)-> DoubleVar:
    nombre=nombre-nombre2

def multiplication(nombre,nombre2)-> DoubleVar:
    nombre=nombre*nombre2

def division(nombre,nombre2)-> DoubleVar:
    nombre=nombre/nombre2
    

window = tk.Tk()
window.title('Calculator')
window.minsize(300,300)
window.geometry("800x800")
done=False
label=tk.Label(window, 
               text="Hello World",
               foreground="red",
               background="black")
textboxes = tk.Canvas(window, width = 430, height = 330)
textboxes.pack()

var=tk.IntVar()
e = tk.Entry (window)
nombre=input("premier nombre")
btnPLUS=Button(window,text="=",bd=5,command= lambda:addition(nombre))
btnPLUS.pack(side = 'top')
textboxes.create_window(303, 146, window=e)
print(nombre)



    
    




window.mainloop()
