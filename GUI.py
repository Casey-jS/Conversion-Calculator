from tkinter import *
import tkinter as tk

window = Tk()
window.title('Unit Conversion Calculator')

frame = Frame(window)
frame.pack()

window.geometry('500x500')

label = Label(window, text = "Select Type", font=("Arial Bold", 20))
label.grid(column=0,row=0)


