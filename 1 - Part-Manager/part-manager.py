from tkinter import *
from tkinter import messagebox
from db import Database

db = Database("store.db")

def populate_list():
    partList.delete(0, END)
    for row in db.fetch():
        partList.insert(END, row)

def add_item():
    if partNumber.get() == '' or loteNumber.get() == '' or cantidad.get() == '' or status.get() == '':
        messagebox.showerror("!Atención", "LLene todos los campos")
        return 

    db.insert(partNumber.get(), loteNumber.get(), cantidad.get(), status.get())
    partList.delete(0, END)
    partList.insert(END, (partNumber.get(), loteNumber.get(), cantidad.get(), status.get()))
    populate_list()

def select_item(event):
    try:
        global selected_item
        index = partList.curselection()[0]
        selected_item = partList.get(index)
        
        partNumberEntry.delete(0, END)
        partNumberEntry.insert(END, selected_item[1])
        
        loteNumberEntry.delete(0, END)
        loteNumberEntry.insert(END, selected_item[2])

        cantidadEntry.delete(0, END)
        cantidadEntry.insert(END, selected_item[3])

    except IndexError:
        pass

def update_item():
    db.update(selected_item[0], partNumber.get(), loteNumber.get(), cantidad.get(), status.get())
    populate_list()

def clean_input():
    partNumberEntry.delete(0, END)        
    loteNumberEntry.delete(0, END)
    cantidadEntry.delete(0, END)
    
def remove_item():
    db.remove(selected_item[0])
    populate_list()

app = Tk()
app.title("Part Manager")
app.geometry("890x600")
app.iconbitmap("inventory.ico")
app.resizable(0,0)

partNumber = StringVar()
loteNumber = StringVar()
cantidad = StringVar()
status = StringVar()

""" Labels """
partNumberLabel = Label(app, text="Part Number", font=("bold", 11), pady=6)
loteNumberLabel = Label(app, text="Lote", font=("bold", 11), pady=6)
cantidadLabel = Label(app, text="Cantidad", font=("bold", 11), pady=6)
statusLabel = Label(app, text="Status", font=("bold", 11), pady=6)

""" Labels Config """
partNumberLabel.grid(row=0, column=0, sticky=E, ipadx=5)
loteNumberLabel.grid(row=1, column=0, sticky=E, ipadx=5)
cantidadLabel.grid(row=0, column=2, sticky=E, ipadx=5)
statusLabel.grid(row=1, column=2, sticky=E, ipadx=5)

""" Entry """
partNumberEntry = Entry(app, textvariable=partNumber, font="bold")
loteNumberEntry = Entry(app, textvariable=loteNumber, font="bold")
cantidadEntry = Entry(app, textvariable=cantidad, font="bold")
radioButton_1 = Radiobutton(app, text="RELEASE", value="RELEASE", variable=status, font="bold")
radioButton_2 = Radiobutton(app, text="NO RELEASE", value="NO RELEASE", variable=status, font="bold")

""" Entries Config """
partNumberEntry.grid(row=0, column=1, pady=10, ipady=2, padx=20)
loteNumberEntry.grid(row=1, column=1, pady=10, ipady=2, padx=20)
cantidadEntry.grid(row=0, column=3, pady=10, ipady=2, padx=20)
radioButton_1.grid(row=1, column=3)
radioButton_2.grid(row=1, column=4)

""" Buttons """

addButton = Button(app, text="Add Product", width=15, height=5, border=4, bg="#d0d3d4", command=add_item)
updateButton = Button(app, text="Update Product", width=15, height=5, border=4, bg="#d0d3d4", command=update_item)
cleanInputButton = Button(app, text="Clean Input", width=15, height=5, border=4, bg="#d0d3d4", command=clean_input)
removeButton = Button(app, text="Remove Product", width=15, height=5, border=4, bg="#d0d3d4", command=remove_item)

addButton.grid(row=4, column=12, pady=5)
updateButton.grid(row=5, column=12, pady=5)
cleanInputButton.grid(row=6, column=12, pady=5)
removeButton.grid(row=7, column=12, pady=5)

""" ListBox """

partList = Listbox(app, height=16, width=76, font="Times 14")
partList.grid(row=3, column=0, columnspan=7, rowspan=6, pady=19, padx=20)
partList.bind('<<ListboxSelect>>', select_item)

populate_list()

"""MainLoop """
app.mainloop()
