from tkinter import *
import tkinter as tk

nombretoStringtoAffichage = ""


def retrieveInput():
    global nombretoStringtoAffichage, equation
    try:
        total = str(eval(nombretoStringtoAffichage))
        equation.set(str(total))
        nombretoStringtoAffichage = ""

    except:

        equation.set(" error ")
        nombretoStringtoAffichage = ""


def afficherTextBox(nombre):
    global nombretoStringtoAffichage, equation
    nombretoStringtoAffichage = nombretoStringtoAffichage+str(nombre)
    equation.set(nombretoStringtoAffichage)


window = tk.Tk()
window.title('Calculator')
window.minsize(220, 300)
window.geometry("220x300")
disp = Entry(window, state='readonly', readonlybackground="white")
disp.grid(column=0, row=0, columnspan=4)
done = False

equation = StringVar()


textBox = tk.Entry(window, textvariable=equation)
textBox.grid(column=1, row=3, columnspan=2)


buttonPLUS = tk.Button(window, text="+", width=5, height=3,
                       command=(lambda: afficherTextBox("+")))
buttonPLUS.grid(row=0, column=3, sticky='nesw')

buttonMINUS = tk.Button(window, text="-", width=5,
                        height=3, command=(lambda: afficherTextBox("-")))
buttonMINUS.grid(row=1, column=3, sticky='nesw')

buttonMULTIPLY = tk.Button(window, text="x", width=5,
                           height=3, command=(lambda: afficherTextBox("*")))
buttonMULTIPLY.grid(row=2, column=3, sticky='nesw')

buttonDIVIDE = tk.Button(window, text="/", width=5,
                         height=3, command=(lambda: afficherTextBox("/")))
buttonDIVIDE.grid(row=3, column=3, sticky='nesw')

buttonEqual = tk.Button(window, text="=", width=5,
                        height=3, command= (lambda:retrieveInput()))
buttonEqual.grid(row=4, column=3, sticky='nesw')

one = Button(window, text="1", width=5, height=3,
             command=(lambda: afficherTextBox(1)))
one.grid(column=0, row=2, sticky='nsew')
two = Button(window, text="2", width=5, height=3,
             command=(lambda: afficherTextBox(2)))
two.grid(column=1, row=2, sticky='nsew')
three = Button(window, text="3", width=5, height=3,
               command=(lambda: afficherTextBox(3)))
three.grid(column=2, row=2, sticky='nsew')
four = Button(window, text="4", width=5, height=3,
              command=(lambda: afficherTextBox(4)))
four.grid(column=0, row=1, sticky='nsew')
five = Button(window, text="5", width=5, height=3,
              command=(lambda: afficherTextBox(5)))
five.grid(column=1, row=1, sticky='nsew')
six = Button(window, text="6", width=5, height=3,
             command=(lambda: afficherTextBox(6)))
six.grid(column=2, row=1, sticky='nsew')
seven = Button(window, text="7", width=5, height=3,
               command=(lambda: afficherTextBox(7)))
seven.grid(column=0, row=0, sticky='nsew')
eight = Button(window, text="8", width=5, height=3,
               command=(lambda: afficherTextBox(8)))
eight.grid(column=1, row=0, sticky='nsew')
nine = Button(window, text="9", width=5, height=3,
              command=(lambda: afficherTextBox(9)))
nine.grid(column=2, row=0, sticky='nsew')
zero = Button(window, text="0", width=5, height=3,
              command=(lambda: afficherTextBox(0)))
zero.grid(column=0, row=3, sticky='nsew')


window.mainloop()
