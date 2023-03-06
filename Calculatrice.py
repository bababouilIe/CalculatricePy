from tkinter import *
import tkinter as tk

def retrieveInput():
    input=textBox.get("1.0",END)
    print(input)
def addition(nombre)-> None:
    nombre=nombre+nombre2
    
    

def soustraire(nombre,nombre2)-> DoubleVar:
    nombre=nombre-nombre2

def multiplication(nombre,nombre2)-> DoubleVar:
    nombre=nombre*nombre2

def division(nombre,nombre2)-> DoubleVar:
    nombre=nombre/nombre2
    

window = tk.Tk()
window.title('Calculator')
window.minsize(180,250)
window.geometry("180x300")
disp = Entry(window, state='readonly', readonlybackground="white")
disp.grid(column=0, row=0, columnspan=4)
done=False
#label=tk.Label(window, 
               #text="Hello World",
               #foreground="red",
               #background="black")
#label.pack(side=BOTTOM)

#var=tk.IntVar()
textBox=Text(window, height=3, width=10)
textBox.grid(column=1,row=3,columnspan=2)


#nombre=input("premier nombre")
buttonPLUS=tk.Button(window,text="+",width=5,height=3,command=lambda:retrieveInput())
buttonPLUS.grid(row=0,column=3,sticky='nesw')

buttonMINUS=tk.Button(window, text="-",width=5,height=3)
buttonMINUS.grid(row=1,column=3,sticky='nesw')

buttonMULTIPLY=tk.Button(window, text="x",width=5,height=3)
buttonMULTIPLY.grid(row=2,column=3,sticky='nesw')

buttonDIVIDE=tk.Button(window, text="/",width=5,height=3)
buttonDIVIDE.grid(row=3,column=3,sticky='nesw')

buttonEqual=tk.Button(window, text="=",width=5,height=3)
buttonEqual.grid(row=4,column=3,sticky='nesw')

one=Button(window,text="1",width=5,height=3)
one.grid(column=0,row=2,sticky='nsew')
two=Button(window,text="2",width=5,height=3)
two.grid(column=1,row=2,sticky='nsew')
three=Button(window,text="3",width=5,height=3)
three.grid(column=2,row=2,sticky='nsew')
four=Button(window,text="4",width=5,height=3)
four.grid(column=0,row=1,sticky='nsew')
five=Button(window,text="5",width=5,height=3)
five.grid(column=1,row=1,sticky='nsew')
six=Button(window,text="6",width=5,height=3)
six.grid(column=2,row=1,sticky='nsew')
seven=Button(window,text="7",width=5,height=3)
seven.grid(column=0,row=0,sticky='nsew')
eight=Button(window,text="8",width=5,height=3)
eight.grid(column=1,row=0,sticky='nsew')
nine=Button(window,text="9",width=5,height=3)
nine.grid(column=2,row=0,sticky='nsew')
zero=Button(window,text="0",width=5,height=3)
zero.grid(column=0,row=3,sticky='nsew')








    
    




window.mainloop()
