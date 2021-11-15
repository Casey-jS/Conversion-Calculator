import csv
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import tkinter as tk
from tkinter import font as f
from tkinter import ttk
import os
import string

error = "Invalid Entry"
def is_hex(s): return all(c in string.hexdigits for c in s)
def is_octal(s): return all(c in string.octdigits for c in s)
def is_decimal(s): return all(c in string.digits for c in s)

def is_binary(string):
    p = set(string)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        return True
    return False

#import matplotlib.pyplot as plt

#Decimal Conversions
#
#
#decimal to binary


#decimal to binary
def dec_to_bin(decimal): # done
    if is_decimal(decimal):
        dec_int = int(decimal)
        return bin(dec_int)[2:]
    return error

#decimal to hex
def dec_to_hex(dec): # done
    if is_decimal(dec): return hex(dec)[2:]
    return error

#decimal to octal
def  dec_to_oct(dec): # done
    if is_decimal(dec): return oct(dec)[2:]
    return error

#Binary Conversions
#
#
#binary to decimal
def bin_to_dec(binary):
    if is_binary(binary):
        return 

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
def hex_to_dec(hex): # done
    if is_hex(hex): return int(hex, 16)
    return error

def hex_to_oct(hex): # done
    if is_hex(hex): return oct(int(hex, 16))[2:]
    return error

def hex_to_bin(hex): # done
    if is_hex(hex): return bin(int(hex, 16))[2:]
    return error

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
    length = len(header)

    global vars
    vars = {}

    for i in range(length):
        vars[i+1] = []

    for row in csvreader:
        i=0
        for item in row:
            vars[i+1].append(item)
            i+=1

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

    index1 = header.index(variable1) + 1
    index2 = header.index(variable2) + 1

# plt.plot(vars[index1], vars[index2], 'ro')
# plt.show()






