from itertools import permutations
import Dictionary as d
from tkinter import *
from tkinter import messagebox

letters = ""
numbers = ""

def click_letters():

    let = letters_entry.get()
    msg = ''

    if (len(let) < 1):

        msg = "Input Error! Try Again."
        messagebox.showinfo('message', msg)

    for i in let:

        if ((not (i.isdigit())) and (not (i == ','))):

            msg = "Input Error! Try Again."
            messagebox.showinfo('message', msg)

    if (let[-1] == ','):

        msg = "Input Error! Try Again."
        messagebox.showinfo('message', msg)
    
    global letters 
    letters = [l.lower() for l in let.split(",")]

def click_numbers():

    num = numbers_entry.get()
    msg = ''

    if (len(num) < 1):

        msg = "Input Error! Try Again."
        messagebox.showinfo('message', msg)

    for i in num:

        if ((not (i.isdigit())) and (not (i == ','))):

            msg = "Input Error! Try Again."
            messagebox.showinfo('message', msg)

    if (num[-1] == ','):

        msg = "Input Error! Try Again."
        messagebox.showinfo('message', msg)
    
    global numbers
    numbers = [int(n) for n in num.split(",")]
    numbers.sort(reverse=True)

def click():

    click_letters()
    click_numbers()

    global letters
    global numbers
    global output

    if ((not isinstance(letters , list)) or (not isinstance(letters , list))):

        output.config(text = 'Input Error')

    else:

        out = ""

        for n in list(numbers):
            
            out = out + "Words with " + str(n) + "letters:\n"
                
            perm = permutations(letters, n)
            perm = set(["".join(p) for p in perm if (d.check("".join(p)))])
            perm = list(perm)
            perm.sort()
            for p in perm:
                    
                out = out + p + "\n"

            out = out + "\n"

        output.config(text = out)


def close_window():

    global window
    global window2

    window.destroy()
    window2.destroy()
    exit()

window = Tk()
window.title("Word Game Solver v0.2")
window.configure(background = "white")

window2 = Tk()
window2.title("Solution Words")
window2.configure(background = "white")


Label(window , text = "Enter given letters separated by commas." , bg = "black" , fg = "white" , font = "none 12 bold").grid(row = 1 , column = 0)
Label(window , text = "Examples: [A,b,C,e] or [Z,y,G,o,G]." , bg = "black" , fg = "white" , font = "none 12 bold").grid(row = 1 , column = 1)
letters_entry = Entry(window , width = 20 , bg = "grey")
letters_entry.grid(row = 2 , column = 0 , sticky = W)

Label(window , text = "Enter possible sizes separated by commas (min 3)." , bg = "black" , fg = "white" , font = "none 12 bold").grid(row = 4 , column = 0)
Label(window , text = "Examples: [3,5] or [8,4,5,2]." , bg = "black" , fg = "white" , font = "none 12 bold").grid(row = 4 , column = 1)
numbers_entry = Entry(window , width = 20 , bg = "grey")
numbers_entry.grid(row = 5 , column = 0 , sticky = W)

Button(window , text = "Confirm" , width = 0 , command = click).grid(row = 7 , column = 1)

output = Label(window2 , text = '' , bg = "white")

Button(window , text = "Quit" , width = 0 , command = close_window).grid(row = 7 , column = 2)

window.mainloop()
window2.mainloop()
