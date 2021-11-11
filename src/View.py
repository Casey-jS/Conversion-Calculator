from tkinter import *
import tkinter as tk
from tkinter import font as f
from tkinter import ttk
from Controller import Controller


#initialize default font
font = ("Helvetica", 8)

#app class of type window
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        self.geometry('600x400')
        self.title('Calculator++')
        self.minsize(600,400)
        self.maxsize(600,400)
       
        # initialize frames by stacking them on top of eachother
        self.frames = {}
        for F in (Menu, Numbers, Graph, Units):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
    
        self.show_frame(Menu)
        self.config(bg="black")

    # called to move a frame to top of list
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#menu class of type Frame
class Menu(tk.Frame):
    def __init__(self, parent, controller):
        title_font = f.Font(family='Helvetica', size=32)
        
        # Make Menu
        tk.Frame.__init__(self, parent, 
                                     width = 600, 
                                     height = 400, 
                                     bg = "black")
       #title label
        label = Label(self, text="Calculator++", font=title_font, bg='black', fg="deep sky blue")
        label.place(relx =.5, rely = .1, anchor = 'center')
        
        #formats the buttons
        def menu_buttons(b, h):
            b.config(font=f.Font(family='Helvetica', size=10), bg='black', fg='white', highlightbackground='blue')
            b.place(relx=.5, rely=.5 + h, anchor='center')
        
        num_button = Button(self, text="Number Conversion", 
                                                             command = lambda : controller.show_frame(Numbers), 
                                                             activebackground = 'deep sky blue',
                                                             fg = 'deep sky blue',
                                                             )
        unit_button = Button(self, text="Unit Conversion",
                                                             command = lambda : controller.show_frame(Units), 
                                                             activebackground = 'deep sky blue',
                                                             fg = 'deep sky blue',
                                                             )
        graph_button = Button(self, text="Graphing",
                                                             command = lambda : controller.show_frame(Graph),
                                                             activebackground = 'deep sky blue',
                                                             fg = 'deep sky blue',
                                                             )

        menu_buttons(num_button, .1)
        menu_buttons(unit_button, .2)
        menu_buttons(graph_button, .3)

        
class Numbers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width = 600, height = 400, bg="black")

        in_text = Label(self, text = "Input Type",  fg = 'deep sky blue', bg = 'black', font = ("Helvetica", 24))
        in_text.place(rely = .05, relx = .3, anchor = 'center')

        out_text = Label(self, text = "Output Type", fg = 'deep sky blue', bg ='black', font = ("Helvetica", 24))
        out_text.place(rely = .05, relx = .7, anchor = 'center')

        binary_button = Button(self, text = "Binary", command = lambda : in_button_clicked(binary_button, "Binary"))
        hex_button = Button(self, text = "Hex", command = lambda : in_button_clicked(hex_button, "Hex"))
        decimal_button = Button(self, text = "Decimal", command = lambda : in_button_clicked(decimal_button, "Decimal"))                   
        octal_button = Button(self, text = "Octal", command = lambda : in_button_clicked(octal_button, "Octal"))

        binary_button2 = Button(self, text = "Binary", command = lambda : out_button_clicked(binary_button2, "Binary"))
        hex_button2 = Button(self, text = "Hex", command = lambda : out_button_clicked(hex_button2, "Hex"))
        decimal_button2= Button(self, text = "Decimal", command = lambda : out_button_clicked(decimal_button2, "Decimal"))                   
        octal_button2 = Button(self, text = "Octal", command = lambda : out_button_clicked(octal_button2, "Octal"))

        # arrange input buttons                       
        start_height = .15
        for button in (binary_button, hex_button, decimal_button, octal_button):
            button.config(fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ('Helvetica', 16),
                                   width = 8,
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black')
            button.place(relx = .2, rely = start_height)
            start_height += .12

        # arrange output buttons
        start_height = .15
        for button in (binary_button2, hex_button2, decimal_button2, octal_button2):
            button.config(fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ("Helvetica", 16),
                                   width = 8,
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black')
            button.place(relx = .6, rely = start_height)
            start_height += .12

        input_choice = ""
        output_choice = ""

        back_btn = Button(self, 
                                   text="Back", 
                                   fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ("Helvetica", 16),
                                   width = 8,
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black',
                                   command = lambda : controller.show_frame(Menu))
        back_btn.place(relx= .1, rely = .05, anchor = 'center')

        def in_button_clicked(button, choice):
            button.config(bg = 'deep sky blue', fg = 'black')
            input_type = choice
        
        def out_button_clicked(button, choice):
            button.config(bg = 'deep sky blue', fg = 'black')
            output_type = choice


class Units(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width = 600, height = 400, bg="black")




        back_btn = Button(self, 
                                   text="Back", 
                                   fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ("Helvetica", 16),
                                   width = 8,
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black',
                                   command = lambda : controller.show_frame(Menu))
        back_btn.place(relx= .1, rely = .05, anchor = 'center')


class Graph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width = 600, height = 400, bg="black")
        

        file_btn = Button(self, 
                                   text="Select File", 
                                   fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ("Helvetica", 16),
                                   width = 8,
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black',
                                   command = lambda : [getFile(), units_btn.config(state=NORMAL)])
        file_btn.place(relx= .5, rely = .4, anchor = 'center')
        units_btn = Button(self, 
                                   text="Select Units", 
                                   fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ("Helvetica", 16),
                                   width = 8,
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black',
                                   state=DISABLED,
                                   command = lambda : [Controller.selectUnits(), graph_btn.config(state=NORMAL)])
        units_btn.place(relx= .5, rely = .5, anchor = 'center')
        graph_btn = Button(self, 
                                   text="Graph it", 
                                   fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ("Helvetica", 16),
                                   width = 8,
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black',
                                   state=DISABLED,
                                   command = lambda : Controller.graphit())
        graph_btn.place(relx= .5, rely = .6, anchor = 'center')

        title = Label(self,
                                   text="Graph", 
                                   fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ("Helvetica", 72),
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black')
        title.place(relx= .5, rely = .2, anchor='center')

        back_btn = Button(self, 
                                   text="Back", 
                                   fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ("Helvetica", 16),
                                   width = 8,
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black',
                                   command = lambda : controller.show_frame(Menu))
        back_btn.place(relx= .1, rely = .05, anchor = 'center')

        def getFile():
            file = Controller.selectFile()
            updateFileLabel(file)

        def updateFileLabel(file):
            file_label = Label(self, text = "File Selected: " + str(file), bg='black')
            file_label.place(relx=.5,rely=.7,anchor='center')

            
app = App()
app.mainloop()


