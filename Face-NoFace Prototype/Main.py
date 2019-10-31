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
state = [True, False]

while True:
    if state[0] and not state[1]:
        state = face_detector.detect(player)
    if not state[0] and not state[1]:
        print("gesture mode")
    if state[1]:
        break
