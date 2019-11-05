#######################################################################################
#
# Will Create a video player if you pass it a valid YouTube URL, a prompt will present itself
# to enter the YouTube URL.
#
# NOTE: for some reason the program will not accept an input URL when run in PyCharm but
# it works when run from powershell/command line
#
# Functions while the media player is playing:
#   quit: press q,
#   play: press 0,
#   pause: press 1,
#   volume up: press 2,
#   volume down: press 3,
#   jump forward: press 4,
#   jump backward: press 5
#
#
##############################################################################################
import keyboard
import tkinter as tk
import tkinter.simpledialog
import time
from MediaModule import VideoFrame, MediaPlayer


root = tk.Tk()
root.title = "Computer Vision Media Controller"
#  url = tk.simpledialog.askstring("Computer Vision Media Controller", "Please Enter a valid YouTube URL")
url = "https://www.youtube.com/watch?v=LXb3EKWsInQ"
player = MediaPlayer()
frame = VideoFrame(root, player)
player.initialize(url)

while True:
    root.update()
    # quit application
    if keyboard.is_pressed('q'):
        print("quit")
        break

    # play
    if keyboard.is_pressed('0'):
        player.play()

    # pause
    if keyboard.is_pressed('1'):
        player.pause()

    # volume down
    if keyboard.is_pressed('2'):
        player.increase_volume()

    # volume up
    if keyboard.is_pressed('3'):
        player.decrease_volume()

    # jump backward
    if keyboard.is_pressed('4'):
        player.jump_forward()

    # jump forward
    if keyboard.is_pressed('5'):
        player.jump_back()

    time.sleep(.1)
