from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
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
        print('welcome to Gesture mode')

    inputUrl = textBox.get("1.0", "end-1c")
    print(inputUrl)


textBox=Text(root, height=2, width=100)
textBox.pack()
# link function to change dropdown
tkvar.trace('w', change_dropdown)
w = tk.Label(root, text="enter URL")
w.pack()

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open("team_logo.png"))


#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")



root.mainloop()


