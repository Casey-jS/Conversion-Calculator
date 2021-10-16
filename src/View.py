from tkinter import *
import tkinter as tk
from tkinter import font as f
from tkinter import ttk

#initializing the window globally
""" window = tk.Tk()
window.geometry('600x400')
window.title('Conversion Calculator')
window.config(bg="black") """

#initialize default font
font = ("Helvetica", 8)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        self.geometry('600x400')
        self.title('Calculator++')
       

        self.frames = {}
        for F in (Menu, NumberConversion, Calculator):
  
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Menu)
        self.config(bg="black")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        self.config(width = 600, height = 400, bg="black")
       #title label
        label = Label(self, text="Universal Calculator")
        label.config(font=f.Font(family='Helvetica', size=16), bg='black', fg='white')
        label.place(relx = .5, rely=.1, anchor='center')

        #formats the buttons
        def menu_buttons(b, h):
            b.config(font=f.Font(family='Helvetica', size=10), bg='black', fg='white', highlightbackground='blue')
            b.place(relx=.5, rely=.5 + h, anchor='center')
        
        #create buttons
        calc_button = Button(self, text="Calculator")
        menu_buttons(calc_button, .1)
        calc_button.config(command = lambda : controller.show_frame(Calculator))
        
        num_button = Button(self, text="Number Conversion")
        menu_buttons(num_button, .2)
        num_button.config(command = lambda: controller.show_frame(NumberConversion))
    
        unit_button = Button(self, text="Unit Conversion")
        menu_buttons(unit_button, .3)
        
class NumberConversion(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width = 600, height = 400, bg="black")
        num_options = ["Hex", "Decimal", "Binary", "Octal"]
        num_inside = tk.StringVar(self)
        num_inside.set("Select Number Type")
        num_menu = tk.OptionMenu(self, num_inside, *num_options)
        num_menu.config(height=1, bg="white", text="black", font=font)
        num_menu.pack(side = tk.LEFT, padx=10)

        input = Text(self, height=1, width=16, bg="white")
        input.pack(side=tk.LEFT,padx=10)

        num_output_inside = tk.StringVar(self)
        num_output_inside.set("Select Output Type")
        num_output_menu = tk.OptionMenu(self, num_output_inside, *num_options)
        num_output_menu.config(height=1, bg="white", text="black", font=font)
        num_output_menu.pack(side = tk.LEFT, padx=10)

        output = Text(self, height=1, width =16, bg="white")
        output.pack(side = tk.LEFT, padx= 10)

        back_button = Button(self, command = lambda : App.show_frame(Menu), text="Back To Menu", bg="white", fg="black")
        back_button.place(rely=.1, relx=.1, anchor='center')

class Calculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # add calculator GUI

app = App()
app.mainloop()


