"""
This is the GUI implementation for the coin toss program
Utilises tkinter, pillow and numpy
Function + images + No animations
next step == animation
"""


from tkinter import *
import numpy as np
from PIL import Image, ImageTk


def toss_the_coin():
    """
    Function to simulate a coin toss
    Args > None
    Return > str; HEADS OR TAILS
    """
    result = np.random.binomial(1,0.5)
    tfield.delete("1.0", "end")

    if result == 1:
        tfield.insert(INSERT, "HEADS!")
        i.config(image = heads)
    else:
        tfield.insert(INSERT, "TAILS!")
        i.config(image = tails)


root = Tk()
root.title("Python Coin Toss")

# load heads image
load = Image.open('C:/Users/desmo/Desktop/Projects/Python/Fate of the coin/Heads.jpg')
heads = ImageTk.PhotoImage(load)
# heads = Image.open('Heads.jpg')

# load tails image
load2 = Image.open('C:/Users/desmo/Desktop/Projects/Python/Fate of the coin/Tails.jpg')
tails = ImageTk.PhotoImage(load2)
# tails = Image.open('Tails.jpg')


i = Label(root, image=heads)
i.pack()

root.geometry('500x500')
b1 = Button(root, text='Toss the coin now!',font=('Arial',10),command=toss_the_coin,
            bg='teal',fg='white',activebackground='lightblue',padx=10,pady=10)
b1.pack()

tfield = Text(root, width=52, height=5)
tfield.pack()
tfield.insert(INSERT, "Click the button to flip the coin!")


root.mainloop()
