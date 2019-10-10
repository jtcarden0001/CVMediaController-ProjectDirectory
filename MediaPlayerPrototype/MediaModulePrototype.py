#######################################################################################
#
# Will Create a video player if you pass it a valid YouTube URL, a prompt will present itself
# to enter the YouTube URL.
#
# NOTE: for some reason the program will not accept an input URL when run in PyCharm but
# it works when run from powershell/command line
#
# Currently Functional: play, pause, volume up, volume down
# Functionality To Do: jump forward, jump backward
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
        if keyboard.is_pressed('q'):
            break
        if keyboard.is_pressed('0'):
            status = 0
            print(status)
            list_player.play()
        if keyboard.is_pressed('1'):
            status = 1
            print(status)
            if list_player.is_playing():
                list_player.pause()
        if keyboard.is_pressed('2'):
            status = 2
            print(status)
            if volume > 0:
                volume = volume - 2
            vlc.libvlc_audio_set_volume(player, volume)
            print("volume: %d\n", volume)
        if keyboard.is_pressed('3'):
            status = 3
            print(status)
            if volume < 100:
                volume = volume + 2
            vlc.libvlc_audio_set_volume(player, volume)
            print("volume: %d\n", volume)
        if keyboard.is_pressed('4'):
            status = 4
            print(status)
        if keyboard.is_pressed('5'):
            status = 5
            print(status)
        time.sleep(.1)
        pass


root = tk.Tk()
root.withdraw()
url = tk.simpledialog.askstring("Computer Vision Media Controller","Please Enter a valid YouTube URL")
setup_player(url)





