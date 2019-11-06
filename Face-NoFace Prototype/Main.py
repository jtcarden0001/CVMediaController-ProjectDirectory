from MediaModule import MediaPlayer
from CVModule import FaceDetector
import tkinter as tk
import tkinter.simpledialog

root = tk.Tk()
root.withdraw()
url = tk.simpledialog.askstring("Computer Vision Media Controller", "Please Enter a valid YouTube URL")
player = MediaPlayer()
player.initialize(url)
face_detector = FaceDetector()
# These states dictate the direction of the main loop.  State[0] indicates what mode the program should be operating in
# (state[0] == True iff face mode, state[0] == False iff gesture mode) while state[1] indicates if the program shou=ld
# continue to run or not (state[1] == True if we want to quit).
state = [True, False]

while not state[1]:
    if state[0]:
        state = face_detector.detect(player)
    else:
        print("gesture mode")
