from tkinter import *
import tkinter as tk
from tkinter import font as f
from tkinter import ttk


window = tk.Tk()
window.geometry('800x300')
window.title('Conversion Calculator')
window.config(bg="white")
frame = Frame()
font = f.Font(family='Helvetica', size=8)
tabControl = ttk.Notebook(window)

num_tab = ttk.Frame(tabControl)
calc_tab = ttk.Frame(tabControl)

tabControl.add(num_tab, text= "Numbers")
tabControl.add(calc_tab, text="Calculator")
tabControl.pack()

length_options = ["Inches", "Centimeters", "Meters", "Feet", "Yards", "Miles", "Kilometers"]

""" input_options = ["Numbers", "Length", "Volume", "Mass"]
input_inside = tk.StringVar(window)
input_inside.set("Select Input Type")
input_menu = tk.OptionMenu(window, input_inside, *input_options)
input_menu.config(height=1, bg="White", text="black", font=font,)
input_menu.pack(side=tk.LEFT) """

num_options = ["Hex", "Decimal", "Binary", "Octal"]
num_inside = tk.StringVar(window)
num_inside.set("Select Number Type")
num_menu = tk.OptionMenu(window, num_inside, *num_options)
num_menu.config(height=1, bg="white", text="black", font=font)
num_menu.pack(side = tk.LEFT, padx=10)

input = Text(window, height=1, width=16, bg="white")
input.pack(side=tk.LEFT,padx=10)

num_output_inside = tk.StringVar(window)
num_output_inside.set("Select Output Type")
num_output_menu = tk.OptionMenu(window, num_output_inside, *num_options)
num_output_menu.config(height=1, bg="white", text="black", font=font)
num_output_menu.pack(side = tk.LEFT, padx=10)




output = Text(window, height=1, width =16, bg="white")
output.pack(side = tk.LEFT, padx= 10)







window.mainloop()




