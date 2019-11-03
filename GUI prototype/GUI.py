from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


# on change dropdown value
def change_dropdown(*args):
    print('Welcome to Face Mode\n' if tkvar.get() == 'Face' else 'Welcome to Gesture mode\n')
    print(inputUrl)


def callback():
    url = textBox.get("1.0", "end-1c")
    print("You entered:" + url)


root = Tk()
root.title("Computer Vision Media Controller")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = {'Face', 'Gesture'}
tkvar.set('None')  # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a mode", font="Times, 25", relief='solid').grid(row=1, column=1)
popupMenu.grid(row=2, column=1)

textBox = Text(root, height=2, width=100)
textBox.pack()
inputUrl = textBox.get("1.0", "end-1c")

# link function to change dropdown
tkvar.trace('w', change_dropdown)
w = tk.Label(root, text="enter URL")
w.pack()

b = Button(text="LAUNCH", command=callback)
b.pack()

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open("team_logo.png"))

# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img)

# The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()  # window will stay as long as you don't click close
