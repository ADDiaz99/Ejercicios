#// calculator.py - 
from tkinter import *


master = Tk()
def close_window():
    exit()
button = Button(master, text = 'Click me', command = close_window)
button.pack()

mainloop()