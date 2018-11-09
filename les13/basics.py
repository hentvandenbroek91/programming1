from tkinter import *
import math

def kwadraat():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    tekst = "kwadraat: van {} = {}"
    label["text"] = tekst.format(grondtal, kwadraat)

def wortel():
    grondtal = int(entry.get())
    tekst = "Wortel: van {} = {}"
    wortel = math.sqrt(grondtal)
    label["text"] = tekst.format(grondtal, wortel)

root = Tk()

label = Label(master=root,
              text='Hello World',
              background='yellow',
              foreground='blue',
              font=('Helvetica', 16, 'bold italic'),
              width=14,
              height=3)
label.pack(fil=X)

kwadraat = Button(master=root, text='Kwadraat', command=kwadraat)
kwadraat.pack(pady=10, fil=X, padx=10)

wortel = Button(master=root, text='Wortel', command=wortel)
wortel.pack(pady=10, fil=X, padx=10)

entry = Entry(master=root)
entry.pack(padx=10, fil=X, pady=10)

root.mainloop()