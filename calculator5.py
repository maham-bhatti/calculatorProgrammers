from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Maham\'s Calculator")
root.geometry('240x273+0+0')
root.config(bg="pink")
root.resizable(False, False)

root.iconbitmap(r"C:\Users\Lenovo\Desktop\Gui in Python\favicon.ico") 


text = Entry(root, width = 15, borderwidth= 2, font=("Times New Roman",24), bg= "White", fg="Black" )
text.grid(row =0, column= 0, columnspan=5, padx=0, pady=0)

def click(number):
    current = text.get()
    text.delete(0, END)
    text.insert(0, str(current) + str(number))
    
def clear():
    text.delete(0, END)

def equal():
    global num_1
    global math
    num = text.get()
    text.delete(0, END)
    if math == "addition":
        text.insert(0, num_1 + int(num.split('+')[1]))
    elif math == "subtraction":
        text.insert(0, num_1 - int(num.split('-')[1]))
    elif math == "multiplication":
        text.insert(0, num_1 * int(num.split('*')[1]))
    elif math == "division":
        value = num.split('/')
        if int(value[1]) != 0:
            text.insert(0, num_1 / int(value[1]))
        else:
            text.insert(0, "Error")
    elif math == "modulus":
        value_1 = num.split('%')
        if int(value_1[1]) != 0:
            text.insert(0, num_1 % int(value_1[1]))
        else:
            text.insert(0, "Error")


def add():
    num1 = text.get()
    global num_1
    global math
    math = "addition"
    num_1 = int(num1)
    text.insert(END, '+')

def divi():
    num1 = text.get()
    global num_1
    global math
    math = "division"
    num_1 = int(num1)
    text.insert(END, '/')
    
def sub():
    num1 = text.get()
    global num_1
    global math
    math = "subtraction"
    num_1 = int(num1)
    text.insert(END, '-')

def multi():
    num1 = text.get()
    global num_1
    global math
    math = "multiplication"
    num_1 = int(num1)
    text.insert(END, '*')

def mod():
    num1 = text.get()
    global num_1
    global math
    math = "modulus"
    num_1 = int(num1)
    text.insert(END, '%')

button1 = Button(root, text = "1", command= lambda: click(1), fg="Blue", bg="pink", padx=22, pady= 10)
button2 = Button(root, text = "2", command= lambda: click(2), fg="Blue", bg="pink", padx=22, pady= 10)
button3 = Button(root, text = "3", command= lambda: click(3), fg="Blue", bg="pink", padx=23, pady= 10)
button4 = Button(root, text = "4", command= lambda: click(4), fg="Blue", bg="pink", padx=22, pady= 10)
button5 = Button(root, text = "5", command= lambda: click(5), fg="Blue", bg="pink", padx=22, pady= 10)
button6 = Button(root, text = "6", command= lambda: click(6), fg="Blue", bg="pink", padx=23, pady= 10)
button7 = Button(root, text = "7", command= lambda: click(7), fg="Blue", bg="pink", padx=23, pady= 10)
button8 = Button(root, text = "8", command= lambda: click(8), fg="Blue", bg="pink", padx=22, pady= 10)
button9 = Button(root, text = "9", command= lambda: click(9), fg="Blue", bg="pink", padx=22, pady= 10)
button0 = Button(root, text = "0", command= lambda: click(0), fg="Blue", bg="pink", padx=22, pady= 10)
button_plus = Button(root, text = "+", command=lambda: add(), fg="Blue", bg="Pink", padx=23, pady= 10)
button_sub = Button(root, text = "-", command= lambda: sub(), fg="Blue", bg="pink", padx=25, pady= 10)
button_mul = Button(root, text = "*", command= lambda: multi(), fg="Blue", bg="pink", padx=25, pady= 10)
button_div = Button(root, text = "/", command= lambda: divi(), fg="Blue", bg="pink", padx=25, pady= 10)
button_mod = Button(root, text = "%", command= lambda: mod(), fg="Blue", bg="pink", padx=20, pady= 10)
button_dot = Button(root, text = ".", command= lambda: click('.'), fg="Blue", bg="pink", padx=24, pady= 10)
button_clear = Button(root, text = "Clear", command= clear, fg="Black", bg="Silver", padx=43, pady= 16)#font =("Times New Roman",8))
button_equal = Button(root, text = "=", command= equal, fg="Black", bg="Silver", padx=53, pady= 16)

button7.grid(row = 1, column =0)
button8.grid(row = 1, column =1)
button9.grid(row = 1, column =2)

button6.grid(row = 2, column =0)
button5.grid(row = 2, column =1)
button4.grid(row = 2, column =2)

button3.grid(row = 3, column =0)
button2.grid(row = 3, column =1)
button1.grid(row = 3, column =2)

button0.grid(row = 4, column =1)
button_clear.grid(row = 5, column =0, columnspan=2)
button_equal.grid(row=5, column=2,columnspan=3)

button_plus.grid(row = 1, column =4)
button_sub.grid(row = 2, column =4)
button_mul.grid(row = 3, column =4)
button_div.grid(row = 4, column =4)
button_dot.grid(row = 4, column =0)
button_mod.grid(row = 4,column = 2)

root.mainloop()