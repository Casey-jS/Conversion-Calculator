from tkinter import *
import tkinter as tk

class View:
    def __init__(self):
        super().__init__()
        window = Tk()
        window.title("Unit Conversion Calculator")

    frame = Frame(window)
    frame.pack()

    choice = OptionMenu()
    choice.pack()

    label = Label(window, text = "Select Type", font=("Arial Bold", 20))
    label.pack()
    window.mainloop()



