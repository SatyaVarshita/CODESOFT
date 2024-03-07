import random
from tkinter import *
from tkinter.ttk import *
 
def low():
    entry.delete(0, END)
 
    length = var1.get()
 
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*?&_!@#$%^&*()"
    password = ""
 
    if var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
 
    elif var.get() == 2:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
 
    elif var.get() == 4:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")
 
 
def generate():
    password1 = medium()
    entry.insert(10, password1)
 
 
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)
 
 
root = Tk()
var = IntVar()
var1 = IntVar()
 
root.title("Random Password Generator-varshita")
 
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
 
c_label = Label(root, text="Length")
c_label.grid(row=1)
fg="black"
bg="yellow"
 

copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)
 

radio_low = Radiobutton(root, text="Low", variable=var, value=2)
radio_low.grid(row=1, column=2, sticky='S')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='S')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=4)
radio_strong.grid(row=1, column=4, sticky='S')
combo = Combobox(root, textvariable=var1)
 

combo['values'] = (6,7,8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32,34,35, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=2, row=2)
 
root.mainloop()