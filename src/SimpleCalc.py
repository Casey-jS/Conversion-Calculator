from tkinter import *

#Defines GUI

root = Tk()

#Titles GUI

root.title("Simple Calculator")

#Defines and adds input box

e = Entry(root, font=('Century 26'), width=14, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	global f_num
	f_num = 0
	e.delete(0, END)


def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	if '.' in first_number:
		f_num = float(first_number)
	else:
		f_num = int(first_number)
	e.delete(0,END)

def button_sub():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	if '.' in first_number:
		f_num = float(first_number)
	else:
		f_num = int(first_number)
	e.delete(0,END)


def button_mult():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	if '.' in first_number:
		f_num = float(first_number)
	else:
		f_num = int(first_number)
	e.delete(0,END)


def button_div():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	if '.' in first_number:
		f_num = float(first_number)
	else:
		f_num = int(first_number)
	e.delete(0,END)


def button_equal():
	second_number = e.get()
	e.delete(0, END)
	formatNumber = lambda n: n if n%1 else int(n)

	if type(f_num) is float or '.' in second_number:
		if math == "addition":
			rtn = f_num + float(second_number)
			rtn = round(rtn, 10)
			e.insert(0, formatNumber(rtn))

		if math == "subtraction":
			rtn = f_num - float(second_number)
			rtn = round(rtn, 10)
			e.insert(0, formatNumber(rtn))

		if math == "multiplication":
			rtn = f_num * float(second_number)
			rtn = round(rtn, 10)
			e.insert(0, formatNumber(rtn))

		if math == "division":
			rtn = f_num / float(second_number)
			rtn = round(rtn, 10)
			e.insert(0, formatNumber(rtn))

	else:
		if math == "addition":
			e.insert(0, f_num + int(second_number))

		if math == "subtraction":
			e.insert(0, f_num - int(second_number))

		if math == "multiplication":
			e.insert(0, f_num * int(second_number))

		if math == "division":
			e.insert(0, f_num / int(second_number))



#Define Buttons

button_1 = Button(root, text="1", width=3, height=2, command=lambda: button_click(1))
button_2 = Button(root, text="2", width=3, height=2, command=lambda: button_click(2))
button_3 = Button(root, text="3", width=3, height=2, command=lambda: button_click(3))
button_4 = Button(root, text="4", width=3, height=2, command=lambda: button_click(4))
button_5 = Button(root, text="5", width=3, height=2, command=lambda: button_click(5))
button_6 = Button(root, text="6", width=3, height=2, command=lambda: button_click(6))
button_7 = Button(root, text="7", width=3, height=2, command=lambda: button_click(7))
button_8 = Button(root, text="8", width=3, height=2, command=lambda: button_click(8))
button_9 = Button(root, text="9", width=3, height=2, command=lambda: button_click(9))
button_0 = Button(root, text="0", width=3, height=2, command=lambda: button_click(0))
button_add = Button(root, text="+", width=3, height=2, command=button_add)
button_mult = Button(root, text="x", width=3, height=2, command=button_mult)
button_div = Button(root, text="/", width=3, height=2, command=button_div)
button_sub = Button(root, text="-", width=3, height=2, command=button_sub)
button_equal = Button(root, text="=", width=3, height=2, command=button_equal)
button_clear = Button(root, text="Clear", width=24, height=2, command=button_clear)
button_dec = Button(root, text=".", width=3, height=2, command=lambda: button_click("."))



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


#Starts loop (Allows use of GUI)

root.mainloop()

