#######################################################################################
#
# Will Create a video player if you pass it a valid YouTube URL, a prompt will present itself
# to enter the YouTube URL.
#
# NOTE: for some reason the program will not accept an input URL when run in PyCharm but
# it works when run from powershell/command line
#
# Functions while the media player is playing
# Currently Functional: play: press 0, pause: press 1, volume down: press 2, volume up: press 3
#                       jump backward: press 4, jump backward: press 5
#
########################################################################################
import vlc
import keyboard
import tkinter as tk
import tkinter.simpledialog
import time


def setup_player(url):
    print(url)
    status = 0
    volume = 50
    vlc_instance = vlc.Instance('--fullscreen')
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(url)
    media_list = vlc_instance.media_list_new([url])
    player.set_media(media)
    list_player = vlc_instance.media_list_player_new()
    list_player.set_media_player(player)
    list_player.set_media_list(media_list)
    list_player.play()
    vlc.libvlc_audio_set_volume(player, volume)

    while True:
        # quit application
        if keyboard.is_pressed('q'):
            print("quit")
            break

        # play
        if keyboard.is_pressed('0'):
            status = 0
            print("play")
            player.play()

        # pause
        if keyboard.is_pressed('1'):
            status = 1
            print("pause")
            if list_player.is_playing():
                player.pause()

        # volume down
        if keyboard.is_pressed('2'):
            status = 2
            if volume > 0:
                volume = volume - 2
            player.audio_set_volume(volume)
            print("volume down: ", volume)

        # volume up
        if keyboard.is_pressed('3'):
            status = 3
            if volume < 100:
                volume = volume + 2
            player.audio_set_volume(volume)
            print("volume up: ", volume)

        # jump backward
        if keyboard.is_pressed('4'):
            status = 4
            print("jump back")
            jumpTo = player.get_time() - 10000
            player.set_time(jumpTo)

        # jump forward
        if keyboard.is_pressed('5'):
            status = 5
            print("jump forward")
            jumpTo = player.get_time() + 10000
            player.set_time(jumpTo)

        time.sleep(.1)
        pass


# Driver Code for functionality in setup_player()
root = tk.Tk()
root.withdraw()
url = tk.simpledialog.askstring("Computer Vision Media Controller", "Please Enter a valid YouTube URL")
setup_player(url)





