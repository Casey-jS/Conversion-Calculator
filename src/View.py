from tkinter import *
import tkinter as tk
from tkinter import font as f
from tkinter import ttk

#initializing the window globally
window = tk.Tk()
window.geometry('600x400')
window.title('Conversion Calculator')
window.config(bg="black")

#initialize default font
font = f.Font(family='Helvetica', size=8)

class Menu:

    #title label
    label = Label(window, text="Universal Calculator")
    label.config(font=f.Font(family='Helvetica', size=16), bg='black', fg='white')
    label.place(relx = .5, rely=.1, anchor='center')

    #formats the buttons
    def menu_buttons(b, h):
        b.config(font=f.Font(family='Helvetica', size=10), bg='black', fg='white', highlightbackground='blue')
        b.place(relx=.5, rely=.5 + h, anchor='center')
    
    #create buttons
    calc_button = Button(window, text="Calculator")
    menu_buttons(calc_button, .1)
    
    num_button = Button(window, text="Number Conversion")
    menu_buttons(num_button, .2)
    """ num_button.config(command = lambda: controller.show_frame("NumberConversion")) """
    
    unit_button = Button(window, text="Unit Conversion")
    menu_buttons(unit_button, .3)
        
class NumberConversion:

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

class Calculator:
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # add calculator GUI

window.mainloop()


