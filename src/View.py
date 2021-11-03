from tkinter import *
import tkinter as tk
from tkinter import font as f
from tkinter import ttk
import Controller


#initialize default font
font = ("Helvetica", 8)
state = "None"

#app class of type window
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        self.geometry('600x400')
        self.title('Calculator++')
       
        # initialize frames by stacking them on top of eachother
        self.frames = {}
        for F in (Menu, NumberConversion, Calculator):
  
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Menu)
        state = "Menu"
        self.config(bg="black")

    # called to move a frame to top of list
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#menu class of type Frame
class Menu(tk.Frame):

    def __init__(self, parent, controller):

        #initialize menu frame
        tk.Frame.__init__(self, parent) 
        self.config(width = 600, height = 400, bg="black")

       #title label
        label = Label(self, text="Calculator++")
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

        # set options for number choice
        num_options = ["Hex", "Decimal", "Binary", "Octal"]
        num_chosen = tk.StringVar(self)
        num_chosen.set("Select Number Type")

        def print_type(choice):
            chosen = Label(text=choice, font = font)
            chosen.pack()

        #create drop down menu
        num_menu = OptionMenu(self, 
                                                    num_chosen, 
                                                    *num_options)
        num_menu.config(height=1, 
                                       bg="white", 
                                       text="black", 
                                       font=font,
                                       command = print_type(num_chosen.get()))

        num_menu.pack(side = tk.LEFT, padx=10)

        input_choice = "None"
        output_choice = "None"

        input_box = Text(self, height=1, width=16, bg="white") # command = Controller.convert()
        input_box.pack(side=tk.LEFT,padx=10)


        num_output_inside = tk.StringVar(self)
        num_output_inside.set("Select Output Type")
        num_output_menu = tk.OptionMenu(self, num_output_inside, *num_options)
        num_output_menu.config(height=1, bg="white", text="black", font=font)
        num_output_menu.pack(side = tk.LEFT, padx=10)

        output = Text(self, height=1, width =16, bg="white")
        #output.config(text=Controller.get_num_output(input, input_choice, output_choice))
        output.pack(side = tk.LEFT, padx= 10)

        #back_button = Button(self, command = App.show_frame(Menu(self)), text="Back To Menu", bg="white", fg="black")
       # back_button.place(rely=.1, relx=.1, anchor='center')
    
    

class Calculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def temp():
            return

        e = Entry(self, font=('Century 26'), width=14, borderwidth=5)
        e.grid(row=0, column=0, columnspan=4)

        button_1 = Button(self, text="1", width=3, height=2, command=temp)
        button_2 = Button(self, text="2", width=3, height=2, command=temp)
        button_3 = Button(self, text="3", width=3, height=2, command=temp)
        button_4 = Button(self, text="4", width=3, height=2, command=temp)
        button_5 = Button(self, text="5", width=3, height=2, command=temp)
        button_6 = Button(self, text="6", width=3, height=2, command=temp)
        button_7 = Button(self, text="7", width=3, height=2, command=temp)
        button_8 = Button(self, text="8", width=3, height=2, command=temp)
        button_9 = Button(self, text="9", width=3, height=2, command=temp)
        button_0 = Button(self, text="0", width=3, height=2, command=temp)
        button_add = Button(self, text="+", width=3, height=2, command=temp)
        button_mult = Button(self, text="x", width=3, height=2, command=temp)
        button_div = Button(self, text="/", width=3, height=2, command=temp)
        button_sub = Button(self, text="-", width=3, height=2, command=temp)
        button_equal = Button(self, text="=", width=3, height=2, command=temp)
        button_clear = Button(self, text="Clear", width=24, height=2, command=temp)
        button_dec = Button(self, text=".", width=3, height=2, command=temp)

        #Puts the buttons on the screen

        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)
        button_sub.grid(row=3, column=3)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)
        button_mult.grid(row=2, column=3)

        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)
        button_div.grid(row=1, column=3)

        button_0.grid(row=4, column=0)
        button_dec.grid(row=4, column=1)
        button_equal.grid(row=4, column=2)
        button_add.grid(row=4, column=3)


        button_clear.grid(row=5, column=0, columnspan=4)

app = App()
app.mainloop()


