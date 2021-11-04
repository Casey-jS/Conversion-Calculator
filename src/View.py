from tkinter import *
import tkinter as tk
from tkinter import font as f
from tkinter import ttk
from Controller import Controller


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
        self.resizable(False, False)
       
        # initialize frames by stacking them on top of eachother
        self.frames = {}
        for F in (Menu, Numbers):
  
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
        title_font = f.Font(family='Helvetica', size=16)
        #initialize menu frame
        tk.Frame.__init__(self, parent)
        self.config(width = 600, height = 400, bg="black")

       #title label
        label = Label(self, text="Calculator++", font=title_font, bg='black', fg="white")
        label.place(relx =.5, rely = .1, anchor = 'center')
        
        #formats the buttons
        def menu_buttons(b, h):
            b.config(font=f.Font(family='Helvetica', size=10), bg='black', fg='white', highlightbackground='blue')
            b.place(relx=.5, rely=.5 + h, anchor='center')
        
        num_button = Button(self, text="Number Conversion", command = lambda : controller.show_frame(Numbers))
        unit_button = Button(self, text="Unit Conversion")
        graph_button = Button(self, text="Graphing")

        menu_buttons(num_button, .1)
        menu_buttons(unit_button, .2)
        menu_buttons(graph_button, .3)

        
class Numbers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width = 600, height = 400, bg="black")

        # set options for number choice
        num_options = ["Hex", "Decimal", "Binary", "Octal"]
        in_chosen = tk.StringVar(self)
        in_chosen.set("Select Number Type")

        #create drop down menu
        num_menu = OptionMenu(self,  in_chosen, *num_options)
        num_menu.config(height=1, bg="white",  text="black", font=font)
        num_menu.pack(side = tk.LEFT, padx=10)

        def print_chosen(in_choice, location):
            choice = Label(text = in_choice, fg = "White")
            choice.pack(side = tk.LEFT, pady = 10, padx = location)

        print_chosen(in_chosen.get(),  30)

        #create input box
        input_box = Entry(self, width=16, bg="white")
        input_box.pack(side=tk.LEFT, padx=10)
        input = input_box.get()

        #create output choice menu
        out_chosen = tk.StringVar(self)
        out_chosen.set("Select Output Type")
        num_output_menu = tk.OptionMenu(self, out_chosen, *num_options)
        num_output_menu.config(height=1, bg="white", text="black", font=font)
        num_output_menu.pack(side = tk.LEFT, padx=10)


        output = Controller.convert_num(in_chosen.get(), input, out_chosen.get())

        output_box = Text(self, height=1, width =16, bg="white")
        output_box.pack(side = tk.LEFT, padx= 10)

        

        convert_button = Button(self, width = 20, 
                                                font = f.Font(family="Helvetica", size = 12), 
                                                bg = "grey", 
                                                fg = "white", 
                                                text = "Convert",
                                                command = lambda : show_output()).pack(
                                                side = tk.BOTTOM, 
                                                pady = 20)
        
        def show_output():
            output_box.config(text = output)



        #back_button = Button(self, command = App.show_frame(Menu(self)), text="Back To Menu", bg="white", fg="black")
       # back_button.place(rely=.1, relx=.1, anchor='center')


app = App()
app.mainloop()


