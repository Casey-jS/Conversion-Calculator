import csv
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import tkinter as tk
from tkinter import font as f
from tkinter import ttk
import os

global variable1
global variable2
variable1 = ""
variable2 = ""

root = Tk()
root.geometry('300x170')
root.title("Test Reader")

e = Entry(root, width= 20, justify="center")

def getFile():
    file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    fileopen = open(file)

    csvreader = csv.reader(fileopen)

    global header 
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)

    e.delete(0, END)
    e.insert(0, "File selected: " + os.path.basename(file))
    e.pack()

    fileopen.close()

    global button2
    button2.configure(state=NORMAL)

def selectUnits():
    global header
    unitOptions = header

    newWindow = tk.Toplevel(root)
    newWindow.title("Select Units")
    newWindow.geometry('185x90')
    newWindow.maxsize(185,90)
    newWindow.minsize(185,90)

    values1 = StringVar(newWindow)
    values2 = StringVar(newWindow)

    options1 = OptionMenu(newWindow, values1, *unitOptions)
    options1.config(width=6)
    options2 = OptionMenu(newWindow, values2, *unitOptions)
    options2.config(width=6)

    options1.grid(row=0,column=1)
    options2.grid(row=1,column=1)

    Entry1 = Entry(newWindow, width = 7, justify="left")
    Entry1.insert(0,"Variable 1: " )
    Entry1.grid(row=0,column=0)
    Entry2 = Entry(newWindow, width = 7, justify="left")
    Entry2.insert(0, "Variable 2: ")
    Entry2.grid(row=1,column=0)

    def submit():
        global variable1
        global variable2

        variable1 = values1.get()
        variable2 = values2.get()

        global button3
        if  variable1!="" and variable2!="":
            button3.configure(state=NORMAL)

        newWindow.destroy()


    submitButton = Button(newWindow, width = 16, height = 1, text="Submit", command=submit)
    submitButton.grid(row=2,columnspan=2)

def graph():
    global variable1
    global variable2

    print(variable1)
    print(variable2)

button1 = Button(root, text="Select File", width=20, height=2, command=getFile)
global button2
button2 = Button(root, text="Select Units", width=20, height=2, command=selectUnits, state=DISABLED)
global button3
button3 = Button(root, text= "Graph", width=20, height=2, command=graph, state=DISABLED)
button1.pack()
button2.pack()
button3.pack()


root.mainloop()
