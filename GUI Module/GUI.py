from tkinter import *
from tkinter.ttk import *  # replaces tkinter components with (slightly) more modern look


def startApp():
    url = urlInput.get()
    print("You entered:" + url)
    statusText.set("Video is playing.")
    status.configure(style="Green.TLabel")


# Initialize root window parameters.
root = Tk()
topLeft = {"x": 15, "y": 18}
root.minsize(width=535, height=145)
root.maxsize(width=535, height=145)
root.title("Computer Vision Media Controller")
Style().configure("Green.TLabel", foreground="green")
Style().configure("Gray.TLabel", foreground="gray")

# Create URL label and text box.
Label(root, text='Youtube URL:').place(x=topLeft["x"], y=topLeft["y"])
urlInput = Entry(root, width=65)
urlInput.place(x=topLeft["x"] + 100, y=topLeft["y"])
defaultUrl = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # never gonna give you up
urlInput.insert(END, defaultUrl)

# Create Status label and text field.
Label(root, text='Status:').place(x=topLeft["x"] + 37, y=topLeft["y"] + 35)
statusText = StringVar()
statusText.set("Video has not been started.")
status = Label(root, textvariable=statusText, style="Gray.TLabel")
status.place(x=topLeft["x"] + 97, y=topLeft["y"] + 35)

# Create Mode label and radio buttons.
mode = IntVar()
Label(root, text='Mode:').place(x=topLeft["x"] + 38, y=topLeft["y"] + 72)
Radiobutton(root, text="Gesture Recognition", variable=mode, value=1).place(x=topLeft["x"] + 95, y=topLeft["y"] + 65)
Radiobutton(root, text="Facial Recognition", variable=mode, value=2).place(x=topLeft["x"] + 95, y=topLeft["y"] + 85)
mode.set(1)

# Create Start button.
startButton = Button(text="Start", command=startApp)
startButton.place(x=topLeft["x"] + 400, y=topLeft["y"] + 80)

root.mainloop()
