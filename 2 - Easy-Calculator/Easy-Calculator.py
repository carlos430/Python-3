from tkinter import *

def sumar():
    showResult.set(firstNumber.get() + secondNumber.get())
    borrar()

def restar():
    showResult.set(firstNumber.get() - secondNumber.get())
    borrar()

def multiplicar():
    showResult.set(firstNumber.get() * secondNumber.get())
    borrar()

def dividir():
    showResult.set(firstNumber.get() / secondNumber.get())
    borrar()

def borrar():
    firstNumber.set("")
    secondNumber.set("")

root = Tk()
root.title("CALCULADORA")
root.iconbitmap('projects/calc.ico')
root.geometry("305x440")
root.resizable(0, 0)

firstNumber = IntVar()
secondNumber = IntVar()
showResult = IntVar()

label_number_one = Label(root, text="Primer Numero", font="Times 15 bold")
label_number_second = Label(root, text="Segundo Numero", font="Times 15 bold")

label_number_one.grid(pady = 10, row=0, column=0)
label_number_second.grid(pady = 10, row=2, column=0)

entry_number_one = Entry(root, width=35, font="Times 12 bold", textvariable=firstNumber)
entry_number_one.grid(ipady = 2, padx = 10, pady = 8, row=1, column=0)

entry_number_second = Entry(root, width=35, font="Times 12 bold", textvariable=secondNumber)
entry_number_second.grid(ipady = 2, padx = 10, pady = 8, row=3, column=0)

resultLabel= Label(root, text="Resultado", font="Times 13 bold")
resultLabel.grid(pady = 10, row=4, column=0)

resultEntry = Entry(root, width=35, font="Times 12 bold", textvariable=showResult, state=DISABLED)
resultEntry.grid(padx = 10, pady = 8, row=5, column=0)

"""OPERACIONES MATEMATICAS"""
botonSumar = Button(root, text="Sumar (+)", font="Times 13 bold", bg="#a569bd", width=10, command=sumar)
botonRestar = Button(root, text="Restar (-)", font="Times 13 bold", bg="#58d68d", width=10, command=restar)
botonMultiplicar = Button(root, text="Mult (x)", font="Times 13 bold", bg="#f1c40f", width=10, command=multiplicar)
botonDividir = Button(root, text="Div (/)", font="Times 13 bold", bg="#eb984e", width=10, command=dividir)

botonSumar.grid(pady = 3, row=6, column=0)
botonRestar.grid(pady = 3, row=7, column=0)
botonMultiplicar.grid(pady = 3, row=8, column=0)
botonDividir.grid(pady = 3, row=9, column=0)

root.mainloop()