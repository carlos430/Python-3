from tkinter import *

root = Tk()
root.title("Calculadora")
root.iconbitmap("projects\calc.ico")
root.geometry("395x316")
root.resizable(0,0)
    
screen = Entry(root, width=60)
screen.grid(row=0, column=0, columnspan = 7, padx = 20, pady = 10, ipady=10)

def buttonAction(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))

def cleanScreen():
    screen.delete(0, END)

def buttonAdd():
    firstNumber = screen.get()
    global f_num
    global math
    math = "addition"
    f_num = int(firstNumber)
    screen.delete(0, END)

def buttonSubt():
    firstNumber = screen.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(firstNumber)
    screen.delete(0, END)

def buttonMult():
    firstNumber = screen.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(firstNumber)
    screen.delete(0, END)

def buttonDiv():
    firstNumber = screen.get()
    global f_num
    global math
    math = "division"
    f_num = int(firstNumber)
    screen.delete(0, END)

def buttonEqual():
    secondNumber = screen.get()
    screen.delete(0, END)
    if math == "addition":
        screen.insert(0, f_num + int(secondNumber))

    if math == "subtraction":
        screen.insert(0, f_num - int(secondNumber))
        
    if math == "multiplication":
        screen.insert(0, f_num * int(secondNumber))

    if math == "division":
        screen.insert(0, f_num / int(secondNumber))

# Number Button
butonUno = Button(root, text="1", padx=40, pady=20, command=lambda: buttonAction(1))
butonDos = Button(root, text="2", padx=40, pady=20, command=lambda: buttonAction(2))
butonTres = Button(root, text="3", padx=40, pady=20, command=lambda: buttonAction(3))
butonCuatro = Button(root, text="4", padx=40, pady=20, command=lambda: buttonAction(4))
butonCinco = Button(root, text="5", padx=40, pady=20, command=lambda: buttonAction(5))
butonSeis = Button(root, text="6", padx=40, pady=20, command=lambda: buttonAction(6))
butonSiete = Button(root, text="7", padx=40, pady=20, command=lambda: buttonAction(7))
butonOcho = Button(root, text="8", padx=40, pady=20, command=lambda: buttonAction(8))
butonNueve = Button(root, text="9", padx=40, pady=20, command=lambda: buttonAction(9))
butonCero = Button(root, text="0", padx=40, pady=20, command=lambda: buttonAction(0))

# Operation Button
butonPlus = Button(root, text="+", padx=38, pady=20, command=buttonAdd)
butonMinus = Button(root, text="-", padx=40, pady=20, command=buttonSubt)
butonMult = Button(root, text="*", padx=40, pady=20, command=buttonMult)
butonDiv = Button(root, text="/", padx=40, pady=20, command=buttonDiv)
butonEqual = Button(root, text="=", padx=39, pady=20, command=buttonEqual)
butonClear = Button(root, text="Clear", padx=30, pady=20, command=cleanScreen)

# Config Number Button
butonCero.grid(row=4, column=0)
butonClear.grid(row=4, column=1)
butonEqual.grid(row=4, column=2)
butonDiv.grid(row=4, column=3)

butonUno.grid(row=3, column=0)
butonDos.grid(row=3, column=1)
butonTres.grid(row=3, column=2)
butonMult.grid(row=3, column=3)

butonCuatro.grid(row=2, column=0)
butonCinco.grid(row=2, column=1)
butonSeis.grid(row=2, column=2)
butonMinus.grid(row=2, column=3)

butonSiete.grid(row=1, column=0)
butonOcho.grid(row=1, column=1)
butonNueve.grid(row=1, column=2)
butonPlus.grid(row=1, column=3)

root.mainloop()