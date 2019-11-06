import tkinter as tk
import vlc


class MediaPlayer:

    def __init__(self):
        self.state = 0  # may change these states into an enum
        self.volume = 50
        self.vlc_instance = vlc.Instance('--no-xlib --quiet')
        self.player = self.vlc_instance.media_player_new()
        self.placeholder = 0
        self.url = ""

    def _validate_url(self, url):
        # TODO: implement a function that validates a Youtube URL
        return True

    def initialize(self, url):
        # TODO: modify the title in the media player title bar to
        #  "Computer Vision Media Controller"
        if not self._validate_url(url):
            return False
        media = self.vlc_instance.media_new(url)
        media_list = self.vlc_instance.media_list_new([url])
        self.player.set_media(media)
        list_player = self.vlc_instance.media_list_player_new()
        list_player.set_media_player(self.player)
        list_player.set_media_list(media_list)
        list_player.play()
        vlc.libvlc_audio_set_volume(self.player, self.volume)
        print("player initialized")
        return True

    def play(self):
        self.state = 0
        print("play")
        self.player.play()

    def pause(self):
        self.state = 1
        print("pause")
        if self.player.is_playing():
            self.player.pause()

    def increase_volume(self):
        if self.volume < 100:
            self.volume = self.volume + 2
        self.player.audio_set_volume(self.volume)
        print("volume up: ", self.volume)

    def decrease_volume(self):
        if self.volume > 0:
            self.volume = self.volume - 2
        self.player.audio_set_volume(self.volume)
        print("volume down: ", self.volume)

    def jump_forward(self):
        print("jump forward")
        jump_to = self.player.get_time() + 10000
        self.player.set_time(jump_to)

    def jump_back(self):
        print("jump back")
        jump_to = self.player.get_time() - 10000
        self.player.set_time(jump_to)

    def get_state(self):
        return self.state


class VideoFrame(tk.Frame):
    def __init__(self, root, player):
        super(VideoFrame, self).__init__(root)
        self.grid()
        self.root = root
        self.center_window()
        self.frame = tk.Frame(self, width=1200, height=700, bd=5)
        self.frame.configure(bg="black")
        self.frame.grid(row=0, column=0, columnspan=10, padx=8)
        self.url_label = tk.Label(self, text="YouTube URL")
        self.url_label.grid(row=1, column=0, columnspan=1)
        self.url_input = tk.Text(self, height=1, width=50)
        self.url_input.grid(row=1, column=1, columnspan=1, padx=8)
        self.reset_button = tk.Button(self, text='Reset Video', command=self.reinitialize)
        self.reset_button.grid(row=1, column=9, columnspan=1, padx=8)
        self.player = player
        self.player.player.set_hwnd(self.frame.winfo_id())

    def reinitialize(self):
        url = self.url_input.get("1.0", "end-1c")
        print(url)
        self.player.initialize(url)

    def center_window(self):
        w = 1200
        h = 700
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.geometry('+%d+%d' % (x, y))
