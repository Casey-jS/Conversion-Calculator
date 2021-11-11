import csv
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import tkinter as tk
from tkinter import font as f
from tkinter import ttk
import os

#Decimal Conversions
#
#
#decimal to binary
def dec_to_bin(decimal):
    return int(bin(decimal)[2:])

#decimal to hex
def dec_to_hex(dec):
    return hex(dec)[2:]

#decimal to octal
def  dec_to_oct(dec):
    return oct(dec)[2:]

#Binary Conversions
#
#
#binary to decimal
def bin_to_dec(binary):
    dec = 0
    count = 0
    while(binary != 0):
        n = binary % 10
        dec = dec + n * pow(2, count)
        binary = binary // 10
        count += 1
    return dec

#binary to hexadecimal
def bin_to_hex(bin):
    dec = int(bin, 10)
    return hex(dec)

#binary to octal
def bin_to_oct(bin):
    dec = int(bin, 10)
    return oct(dec)

#Hex Conversions
#
#
#hexadecimal to decimal
def hex_to_dec(hex):
    dec = 0

    for i, j in enumerate(hex):
        hexList = "0123456789ABCDEF"
        val = hexList.index(j)
        power = (len(hex) - (i + 1))
        dec = dec + (val*16**power)
    return dec

def hex_to_oct(hex):
    dec = int(hex, 10)
    pass

#inches
#cm
#mm
#m
#km
#mi
#ft


def in_to_cm(inch): return 2.54 * inch
def in_to_feet(inch): return 12 / inch
def in_to_mm(inch): return 25.4 * inch
def in_to_m(inch): return .254 * inch
def in_to_km(inch): return .000254 * inch
def in_to_mi(inch): return inch / (5280 * 12)

def cm_to_in(cm): return cm / 2.54
def cm_to_feet(cm): return cm / 30.48
def cm_to_mm(cm): return 10 * cm
def cm_to_m(cm): return 100 / cm
def cm_to_km(cm): return 100000 / cm
def cm_to_mi(cm): return 


def getFile():
    
    file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    fileopen = open(file)

    csvreader = csv.reader(fileopen)

    global header
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)

    fileopen.close()

    return os.path.basename(file)

def selectUnits():
    global header
    unitOptions = header

    newWindow = tk.Toplevel()
    newWindow.title("Select Units")
    newWindow.geometry('185x90')
    newWindow.maxsize(185,90)
    newWindow.minsize(185,90)
    newWindow.config(bg='black')

    values1 = StringVar(newWindow)
    values2 = StringVar(newWindow)

    values1.set(header[0])
    values2.set(header[0])

    options1 = OptionMenu(newWindow, values1, *unitOptions)
    options1.config(width=6, bg="black")
    options2 = OptionMenu(newWindow, values2, *unitOptions)
    options2.config(width=6, bg="black")

    options1.grid(row=0,column=1)
    options2.grid(row=1,column=1)

    Entry1 = Entry(newWindow, width = 7, justify="left", highlightbackground='black')
    Entry1.insert(0,"Variable 1: " )
    Entry1.grid(row=0,column=0)
    Entry2 = Entry(newWindow, width = 7, justify="left", highlightbackground='black')
    Entry2.insert(0, "Variable 2: ")
    Entry2.grid(row=1,column=0)

    def submit():
        global variable1
        global variable2

        variable1 = values1.get()
        variable2 = values2.get()

        newWindow.destroy()


    submitButton = Button(newWindow, 
        width = 16, 
        height = 1, 
        highlightbackground="black",
        text="Submit", 
        command=submit)
    submitButton.grid(row=2,columnspan=2)

def graph():

    global variable1
    global variable2

    print(variable1)
    print(variable2)






