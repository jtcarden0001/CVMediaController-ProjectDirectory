from tkinter import *
import tkinter as tk
root = Tk()
root.title("Welcome To A-Team Computer Vision Project")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)



# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { 'Face','Gesture'}
tkvar.set('None') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a mode",font="Times, 25",relief= 'solid').grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)


# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
    if tkvar.get() =="Face":
        print('welcome to Face Mode')


    else:
        print('welcome to gesture mode')

    inputUrl = textBox.get("1.0", "end-1c")
    print(inputUrl)


textBox=Text(root, height=2, width=100)
textBox.pack()
# link function to change dropdown
tkvar.trace('w', change_dropdown)
w = tk.Label(root, text="enter URL")
w.pack()
root.mainloop()


