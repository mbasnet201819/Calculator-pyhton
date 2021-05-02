from tkinter import *

root = Tk()

root.title("                            Calculator")

root.geometry("341x316")

root.iconbitmap("Calculator.ico")

e = Entry(root, font = ('arial', 15), width = 31, bg = "light grey", bd = 0)
e.grid(row = 0, column = 0, columnspan=4, ipady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math="add"
    f_num = int(first_number)
    e.delete(0,END)

def button_subtraction():
    first_number = e.get()
    global f_num
    global math
    math="subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiplication():
    first_number = e.get()
    global f_num
    global math
    math="multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_division():
    first_number = e.get()
    global f_num
    global math
    math="division"
    f_num = int(first_number)
    e.delete(0,END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math=="add":
        e.insert(0, f_num + int(second_number))
    if math=="subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num // int(second_number))


button_1 = Button(root, text="1", padx=35, pady=15, command=lambda  : button_click(1))
button_2 = Button(root, text="2", padx=35, pady=15, command=lambda  : button_click(2))
button_3 = Button(root, text="3", padx=35, pady=15, command=lambda  : button_click(3))
button_4 = Button(root, text="4", padx=35, pady=15, command=lambda  : button_click(4))
button_5 = Button(root, text="5", padx=35, pady=15, command=lambda  : button_click(5))
button_6 = Button(root, text="6", padx=35, pady=15, command=lambda  : button_click(6))
button_7 = Button(root, text="7", padx=35, pady=15, command=lambda  : button_click(7))
button_8 = Button(root, text="8", padx=35, pady=15, command=lambda  : button_click(8))
button_9 = Button(root, text="9", padx=35, pady=15, command=lambda  : button_click(9))
button_0 = Button(root, text="0", padx=78, pady=15, command=lambda  : button_click(0))
button_add = Button(root, text="+", padx=35, pady=15, bg="light grey", command=button_add)
button_equal = Button(root, text="=", padx=78, pady=15, bg="sky blue", command=button_equal)
button_clear = Button(root, text="Clear", padx=110, pady=15, bg="light grey", command=button_clear)
button_subtraction = Button(root, text="-", padx=35, pady=15, bg="light grey", command=button_subtraction)
button_multiplication = Button(root, text="x", padx=35, pady=15, bg="light grey", command=button_multiplication)
button_division = Button(root, text="/", padx=35, pady=15, bg="light grey", command=button_division)

button_0.grid(row=5, column=0, columnspan=2)
button_equal.grid(row=5, column=2, columnspan=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subtraction.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiplication.grid(row=2, column=3)

button_clear.grid(row=1, column=0, columnspan=3)
button_division.grid(row=1, column=3)

root.mainloop()
