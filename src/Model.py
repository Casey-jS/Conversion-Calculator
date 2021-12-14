import csv
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import tkinter as tk
from tkinter import font as f
from tkinter import ttk
import os
import string
import matplotlib.pyplot as plt

error = "Invalid Entry"
global graph_option
graph_option = 1

# checks input string for valid type
def is_hex(s): return all(c in string.hexdigits for c in s)
def is_octal(s): return all(c in string.octdigits for c in s)
def is_decimal(s): return all(c in string.digits for c in s)
def is_binary(string):
    p = set(string)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        return True
    return False



def dec_to_bin(decimal): 
    if is_decimal(decimal):
        return str(bin(int(decimal)))[2:]
    return error

def dec_to_hex(dec): 
    if is_decimal(dec): return str(hex(int(dec)))[2:]
    return error

def dec_to_oct(dec): 
    if is_decimal(dec): return str(oct(int(dec)))[2:]
    return error

def bin_to_dec(binary):
    if is_binary(binary): return str(int(binary, 2))
    return error

def bin_to_hex(bin): 
    if is_binary(bin): return str(hex(int(bin, 2)))[2:]
    return error

def bin_to_oct(bin):
    if is_binary(bin): return str(oct(int(bin, 2)))[2:]
    return error

def hex_to_dec(hex): 
    if is_hex(hex): return str(int(hex, 16))
    return error

def hex_to_oct(hex): 
    if is_hex(hex): return str(oct(int(hex, 16)))[2:]
    return error

def hex_to_bin(hex): 
    if is_hex(hex): return str(bin(int(hex, 16)))[2:]
    return error

def oct_to_dec(octal):
    if is_octal(octal): return str(int(octal, 8))
    return error

def oct_to_hex(octal): 
    if is_octal(octal): return str(hex(int(octal, 8)))[2:]
    return error

def oct_to_bin(octal): 
    if is_octal(octal): return str(bin(int(octal, 8)))[2:]
    return error

def same_unit_binary(input):
    if is_binary(input): return input
    return error

def same_unit_decimal(input):
    if is_decimal(input): return input
    return error

def same_unit_hex(input):
    if is_hex(input): return input
    return error

def same_unit_octal(input):
    if is_octal(input): return input
    return error

#Methods to convert one unit to another

#inches
def in_to_cm(inch): return 2.54 * inch
def in_to_m(inch): return .0254 * inch
def in_to_km(inch): return .0000254 * inch
def in_to_feet(inch): return inch / 12
def in_to_yard(inch): return inch / 36.0
def in_to_mi(inch): return inch / 63360

#feet
def feet_to_in(feet): return feet * 12.0
def feet_to_yards(feet): return feet / 3.0
def feet_to_mi(feet): return feet / 5280.0
def feet_to_cm(feet): return feet * 30.48
def feet_to_m(feet): return  feet / 3.281
def feet_to_km(feet): return feet / 3281.0

#yards
def yards_to_inches(yards): return yards * 36.0
def yards_to_m(yards): return yards * .9144
def yards_to_cm(yards): return yards * 91.44
def yards_to_mi(yards): return yards / 1760
def yards_to_km(yards): return yards / 1094.0
def yards_to_feet(yards): return yards * 3.0

#miles
def mi_to_inches(miles): return miles * 63360.0
def mi_to_feet(miles): return miles * 5280.0
def mi_to_yards(miles): return miles * 1760.0
def mi_to_cm(miles): return miles * 160934
def mi_to_m(miles): return miles * 1609.34
def mi_to_km(miles): return miles * 1.6093

#centimeter
def cm_to_in(cm): return cm / 2.54
def cm_to_feet(cm): return cm / 30.48
def cm_to_yd(cm): return cm / (2.54 * 36.0)
def cm_to_m(cm): return cm  * .01
def cm_to_km(cm): return cm * .00001
def cm_to_mi(cm): return cm * .000006

#meter
def m_to_in(m): return m * 39.37
def m_to_feet(m): return m * 3.281
def m_to_yards(m): return m * 1.094
def m_to_miles(m): return m / 1609.0
def m_to_cm(m): return m * 100
def m_to_km(m): return m / 1000

#kilometer
def km_to_in(km): return km * 39370.0
def km_to_feet(km): return km * 3281.0
def km_to_yards(km): return km * 1093.6
def km_to_mi(km): return km / 1.609
def km_to_cm(km): return km * 100000.0
def km_to_m(km): return km * 1000


def same_length_unit(input): return input



#Retrieves .csv file and reads it into a dictionary
def getFile():
    
    file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    if file != "":
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

#Brings up Toplevel window to choose graph and units
def selectUnits():
    global header
    unitOptions = header

    def getGraph():
        newWindow = tk.Toplevel()
        newWindow.title("Select Graph")
        newWindow.geometry('210x100')
        newWindow.maxsize(210,105)
        newWindow.minsize(210,105)
        newWindow.config(bg='black')

        global graph_option

        option = IntVar()
        value=1

        def clicked(option):
            global graph_option
            graph_option = option

        def submit(option):
            newWindow.destroy()
            getUnits()


        option1 = Radiobutton(newWindow, text="2 Variable Graph", variable=option, value=1, command=lambda: clicked(option.get()), background="black")
        option1.pack()

        option2 = Radiobutton(newWindow, text="3 Variable Graph", variable=option, value=2, command=lambda: clicked(option.get()), background="black")
        option2.pack()
        
        option3 = Radiobutton(newWindow, text="Histogram",variable=option, value=3, command=lambda: clicked(option.get()), background="black")
        option3.pack()

        submit_btn = Button(newWindow, text = "Submit", command= lambda: submit(value), highlightbackground="black", width=12)
        submit_btn.pack()


    def getUnits():
        if graph_option == 1:

            newWindow = tk.Toplevel()
            newWindow.title("Select Units")
            newWindow.geometry('210x90')
            newWindow.maxsize(207,80)
            newWindow.minsize(207,80)
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

            Entry1 = Label(newWindow, width = 10, justify="left", text="Variable 1 (X): ", background="black")
            Entry1.grid(row=0,column=0)
            Entry2 = Label(newWindow, width = 10, justify="left", text="Variable 2 (Y): ", background="black")
            Entry2.grid(row=1,column=0)

            def submit():
                global variable1
                global variable2

                variable1 = values1.get()
                variable2 = values2.get()

                newWindow.destroy()


            submitButton = Button(newWindow, 
                width = 19, 
                height = 1, 
                highlightbackground="black",
                text="Submit", 
                command=submit)
            submitButton.grid(row=2,columnspan=2)


        if graph_option == 2:

            newWindow = tk.Toplevel()
            newWindow.title("Select Units")
            newWindow.geometry('2107x105')
            newWindow.maxsize(207,105)
            newWindow.minsize(207,105)
            newWindow.config(bg='black')

            values1 = StringVar(newWindow)
            values2 = StringVar(newWindow)
            values3 = StringVar(newWindow)

            values1.set(header[0])
            values2.set(header[0])
            values3.set(header[0])

            options1 = OptionMenu(newWindow, values1, *unitOptions)
            options1.config(width=6, bg="black")
            options2 = OptionMenu(newWindow, values2, *unitOptions)
            options2.config(width=6, bg="black")
            options3 = OptionMenu(newWindow, values3, *unitOptions)
            options3.config(width=6, bg="black")

            options1.grid(row=0,column=1)
            options2.grid(row=1,column=1)
            options3.grid(row=2,column=1)

            Entry1 = Label(newWindow, width = 10, justify="left", text="Variable 1 (X): ", background="black")
            Entry1.grid(row=0,column=0)
            Entry2 = Label(newWindow, width = 10, justify="left", text="Variable 2 (Y1): ", background="black")
            Entry2.grid(row=1,column=0)
            Entry3 = Label(newWindow, width = 10, justify="left", text="Variable 3 (Y2): ", background="black")
            Entry3.grid(row=2,column=0)

            def submit():
                global variable1
                global variable2
                global variable3

                variable1 = values1.get()
                variable2 = values2.get()
                variable3 = values3.get()

                newWindow.destroy()


            submitButton = Button(newWindow, 
                width = 19, 
                height = 1, 
                highlightbackground="black",
                text="Submit", 
                command=submit)
            submitButton.grid(row=3,columnspan=2)


        if graph_option ==3:


            newWindow = tk.Toplevel()
            newWindow.title("Select Units")
            newWindow.geometry('210x90')
            newWindow.maxsize(207,80)
            newWindow.minsize(207,80)
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

            Entry1 = Label(newWindow, width = 10, justify="left", text="Variable 1 (X): ", background="black")
            Entry1.grid(row=0,column=0)
            Entry2 = Label(newWindow, width = 10, justify="left", text="Variable 2 (Y): ", background="black")
            Entry2.grid(row=1,column=0)

            def submit():
                global variable1
                global variable2

                variable1 = values1.get()
                variable2 = values2.get()

                newWindow.destroy()


            submitButton = Button(newWindow, 
                width = 19, 
                height = 1, 
                highlightbackground="black",
                text="Submit", 
                command=submit)
            submitButton.grid(row=2,columnspan=2)

    getGraph()

#Shows graph based of user input file and selected Units
def graph():

    global variable1
    global variable2
    global variable3
    global graph_option


    def graph_1():
        index1 = header.index(variable1) + 1
        index2 = header.index(variable2) + 1

        list1 = vars[index1]
        list2 = vars[index2]


        list1 = list(map(int, list1))
        list2 = list(map(int, list2))

        max1 = 0
        max2 = 0
        
        min1 = list1[0]
        min2 = list2[0]

        for item in list1:
            if item > max1:
                max1 = item
            if item < min1:
                min1 = item

        for item in list2:
            if item > max2:
                max2 = item
            if item < min2:
                min2 = item

        if(max2 < 20):
            max2=max2+1
        elif(max2 < 100):
            max2=max2+5
        elif(max2 > 100):
            max2=max2+20
        elif(max2 > 1000):
            max2=max2+50
        
        plt.figure("Graph")
        plt.plot(list1, list2, '-bo')

        plt.xlabel(str(variable1))
        plt.ylabel(str(variable2))

        plt.axis([min1,max1,0,max2])


        plt.show()

    def graph_2():

        index1 = header.index(variable1) + 1
        index2 = header.index(variable2) + 1
        index3 = header.index(variable3) + 1

        list1 = vars[index1]
        list2 = vars[index2]
        list3 = vars[index3]


        list1 = list(map(int, list1))
        list2 = list(map(int, list2))
        list3 = list(map(int, list3))

        max1 = 0
        max2 = 0
        max3 = 0
        
        min1 = list1[0]
        min2 = list2[0]
        min3 = list3[0]

        for item in list1:
            if item > max1:
                max1 = item
            if item < min1:
                min1 = item

        for item in list2:
            if item > max2:
                max2 = item
            if item < min2:
                min2 = item

        for item in list3:
            if item > max3:
                max3 = item
            if item < min3:
                min3 = item

        if(max3 > max2):
            if(max3 < 20):
                max3=max3+1
            elif(max3 < 100):
                max3=max3+5
            elif(max3 > 100):
                max3=max3+20
            elif(max3 > 1000):
                max3=max3+50
        else:
            if(max2 < 20):
                max2=max2+1
            elif(max2 < 100):
                max2=max2+5
            elif(max2 > 100):
                max2=max2+20
            elif(max2 > 1000):
                max2=max2+50
        

        if(variable2==variable3):
            plt.figure("Graph")
            plt.plot(list1, list2, '-bo')

            plt.xlabel(str(variable1))
            plt.ylabel(str(variable2))

            plt.axis([min1,max1,0,max2])


            plt.show()
        else:
            plt.figure("Graph")
            plt.scatter(list1, list2, marker = 'o', color='b', label=str(variable2))
            plt.scatter(list1, list3, marker='o', color='r', label=str(variable3))
            plt.plot(list1, list2, '-', list1, list3, '-')

            plt.xlabel(str(variable1))
            plt.ylabel(str(variable2) + " and " + str(variable3))

            if(max3 > max2):
                plt.axis([min1,max1,0,max3])
            else:
                plt.axis([min1,max1,0,max2])

            plt.legend()
            plt.show()

    def graph_3():
        index1 = header.index(variable1) + 1
        index2 = header.index(variable2) + 1

        list1 = vars[index1]
        list2 = vars[index2]


        list1 = list(map(int, list1))
        list2 = list(map(int, list2))

        max1 = 0
        max2 = 0
        
        min1 = list1[0]
        min2 = list2[0]

        for item in list1:
            if item > max1:
                max1 = item
            if item < min1:
                min1 = item

        for item in list2:
            if item > max2:
                max2 = item
            if item < min2:
                min2 = item

        if(min1 < 20):
            min1=min1-1
        elif(min1 < 100):
            min1=min1-5
        elif(min1 > 100):
            min1=min1-20
        elif(min1 > 1000):
            min1=min1-50

        if(max1 < 20):
            max1=max1+1
        elif(max1 < 100):
            max1=max1+5
        elif(max1 > 100):
            max1=max1+20
        elif(max1 > 1000):
            max1=max1+50


        if(max2 < 20):
            max2=max2+1
        elif(max2 < 100):
            max2=max2+5
        elif(max2 > 100):
            max2=max2+20
        elif(max2 > 1000):
            max2=max2+50
        
        plt.figure("Graph")
        plt.bar(list1, list2)

        plt.xlabel(str(variable1))
        plt.ylabel(str(variable2))

        plt.axis([min1,max1,0,max2])


        plt.show()

    if graph_option == 1:
        graph_1()
    elif graph_option == 2:
        graph_2()
    elif graph_option == 3:
        graph_3()






