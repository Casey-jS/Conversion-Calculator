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

        default_button_presets = {"fg" : 'blue', "activebackground" : 'blue'}
        
        #formats the buttons
        def menu_buttons(b, h):

            b.config(              
                                   fg = 'deep sky blue',
                                   bg = 'black',
                                   font = ("Helvetica", 16),
                                   width = 14,
                                   activebackground = 'deep sky blue',
                                   activeforeground = 'black')
            b.place(relx=.5, rely=.5 + h, anchor='center')
        
        num_button = Button(self, text="Number Conversion", 
                                                             command = lambda : controller.show_frame(Numbers), 
                                                             **default_button_presets)
        unit_button = Button(self, text="Unit Conversion",
                                                             command = lambda : controller.show_frame(Units), 
                                                             **default_button_presets)
        graph_button = Button(self, text="Graphing",
                                                             command = lambda : controller.show_frame(Graph),
                                                             **default_button_presets)

        menu_buttons(num_button, .1)
        menu_buttons(unit_button, .2)
        menu_buttons(graph_button, .3)

class Numbers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width = 600, height = 400, bg="black")

        blue = 'deep sky blue'
        label_font = ("Helvetica", 24)
        button_font = ("Helvetica", 16)

        default_label = {"fg" : blue, "bg" : "black", "font" : label_font}

        in_text = Label(self, text = "Input Type", **default_label)
        out_text = Label(self, text = "Output Type", **default_label)

        default_button = {"fg" : blue, 
                                      "bg" : 'black', 
                                      "font" : button_font,
                                      "activeforeground" : "black",
                                      "activebackground" : blue,
                                      "width" : 8} 
        
        back_btn = Button(self, **default_button, text = "Back", command = lambda : controller.show_frame(Menu))

        in_text.place(relx = .3, rely = .05, anchor = 'center')
        out_text.place(relx = .725, rely = .05, anchor = 'center')
        back_btn.place(relx= .1, rely = .9, anchor = 'center')

        # create buttons
        binary_button = Button(self, text = "Binary", command = lambda : in_button_clicked(binary_button, "Binary"))
        hex_button = Button(self, text = "Hex", command = lambda : in_button_clicked(hex_button, "Hex"))
        decimal_button = Button(self, text = "Decimal", command = lambda : in_button_clicked(decimal_button, "Decimal"))
        octal_button = Button(self, text = "Octal", command = lambda : in_button_clicked(octal_button, "Octal"))

        binary_button2 = Button(self, text = "Binary", command = lambda : out_button_clicked(binary_button2, "Binary"))
        hex_button2 = Button(self, text = "Hex", command = lambda : out_button_clicked(hex_button2, "Hex"))
        decimal_button2 = Button(self, text = "Decimal", command = lambda : out_button_clicked(decimal_button2, "Decimal"))
        octal_button2 = Button(self, text = "Octal", command = lambda : out_button_clicked(octal_button2, "Octal")) 
        button_names = ["Binary", "Hex", "Decimal", "Octal"]

        """ start_height = .15
        buttons = []
        for name in button_names:
            button = Button(self, text = name, command = lambda : in_button_clicked(button, name), **default_button)
            button.place(relx = .2, rely = start_height)
            buttons.append(button)
            start_height += .12 """

        
        # arrange input buttons                       
        start_height = .15
        for button in (binary_button, hex_button, decimal_button, octal_button):
            button.config(**default_button)
            button.place(relx = .2, rely = start_height)
            start_height += .12

        # arrange output buttons
        start_height = .15
        
        for button in (binary_button2, hex_button2, decimal_button2, octal_button2):
            button.config(**default_button)
            button.place(relx = .625, rely = start_height)
            start_height += .12 # vertical distance between buttons

        
        def in_button_clicked(clicked_button, chosen):
            clicked_button.config(bg = blue, fg = 'black')
            Controller.in_c = chosen
            for button in (binary_button, hex_button, decimal_button, octal_button):
                if button is not clicked_button:
                    button.config(bg = "black", fg = blue)
            
        def out_button_clicked(clicked_button, chosen):
            clicked_button.config(bg = blue, fg = 'black')
            Controller.out_c = chosen
            # reset button colors if a button is clicked
            for button in (binary_button2, hex_button2, decimal_button2, octal_button2):
                if button is not clicked_button:
                    button.config(bg = "black", fg = blue)
            

        in_box = Entry(self, bg = 'black', fg = blue, font = ("Helvetica", 16), width = 9)
        in_box.place(relx = .29, rely = .7, anchor = 'center')

        out_box = Label(self, bg = 'black', fg = blue, font = ('Helvetica', 16), width = 8, text = "Output")
        out_box.place(relx = .8, rely = .8, anchor = 'center')
        
        def convert():
            input = in_box.get()
            output = Controller.convert_num(Controller.in_c, input, Controller.out_c)
            out_box.config(text = output)
            

        convert_button = Button(self,
                                                 text = "Convert",
                                                 fg = blue,
                                                 bg = 'black',
                                                 font = ("Helvetica", 16),
                                                 width = 7,
                                                 height = 1,
                                                 activebackground = blue,
                                                 activeforeground = 'black',
                                                 command = lambda : convert())

        convert_button.place(relx = .5, rely = .5, anchor = 'center')

        

        


        


class Units(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width = 600, height = 400, bg="black")

        blue = 'deep sky blue'
        label_font = ("Helvetica", 16)

        default_label = {"fg" : blue, "bg" : "black", "font" : label_font}

        default_button = {"fg" : blue, "bg" : "black", "font" : label_font, "activeforeground" : "black", "activebackground" : blue, "width" : 8}

        type_label = Label(self, text = "Unit Type", **default_label)
        type_label.place(relx = .5, rely = .1, anchor = 'center')

        unit_types = ["Length", "Mass", "Volume", "Speed"]
        type_buttons = []

        types = {"Length" : {"in", "ft", "mi", "yd",  "mm", "cm", "m", "km"}, 
                       "Volume"  : {"mL", "L", "gal", "fl oz", "ft³", "in³", "cm³", "m³"},
                       "Mass" : {"oz", "lb", "mg", "g", "kg"},
                       "Speed" : {"mi/h", "km/h", "fps", "m/s", "knots"}}

        startx = .2
        for type in unit_types:
            button = Button(self, text = type, **default_button)
            button.place(relx = startx, rely = .2, anchor = 'center')
            type_buttons.append(button)
            startx+= .2
        
        def type_clicked(button_clicked):
            pass


        

        back_btn = Button(self, **default_button, command = lambda : controller.show_frame(Menu), text = "Back")
        back_btn.place(relx= .1, rely = .05, anchor = 'center')


class Graph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(width = 600, height = 400, bg="black")
        
        global file_label
        file_label = Label(self)

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
            global file_label
            file_label.destroy()
            file_label = Label(self, text = "File Selected: " + str(file), bg='black')
            file_label.place(relx=.5,rely=.7,anchor='center')


            
app = App()
app.mainloop()


