from MediaModule import MediaPlayer
import tkinter as tk
from tkinter import ttk


class VideoFrame(tk.Frame):

    def __init__(self, root):
        super(VideoFrame, self).__init__(root)
        self.grid()
        self.root = root
        self.root.title("CV Media Controller")
        self.root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
        self.root.configure(bg='red')
        self.root.resizable(False, False)
        self.mode = tk.IntVar()
        self.mode.set(1)
        self.state_message = tk.StringVar()
        self.state_message.set("Enter a YouTube URL and press start to begin!")
        self.last_input_message = tk.StringVar()
        self.last_input_message.set("")
        self.player_time = tk.StringVar()
        self.player_time.set("")
        self.center_window()
        self.frame = tk.Frame(self, width=1200, height=700, bd=5)
        self.frame.configure(bg="black")
        self.frame.grid(row=0, column=0, columnspan=10, padx=8, pady=8)
        self.progress = ttk.Progressbar(self, orient="horizontal", length="900", mode="indeterminate")
        self.progress.grid(row=1, column=0, pady=10,  columnspan=9, sticky="E")
        self.player_time_label = tk.Label(self, height=1, width=30, textvariable=self.player_time)
        self.player_time_label.grid(row=1, column=9, columnspan=1, padx=8, sticky='W')
        self.url_label = tk.Label(self, text="YouTube URL:")
        self.url_label.grid(row=2, column=0, columnspan=1, padx=35)
        self.url_input = tk.Text(self, height=1, width=50)
        self.url_input.grid(row=2, column=1, columnspan=1, padx=8, sticky='W')
        self.start_button = tk.Button(self, text='Start', command=self.initialize_player)
        self.start_button.grid(row=2, column=2, columnspan=2, padx=8)
        self.mode_label = tk.Label(self, text="Mode:")
        self.mode_label.grid(row=3, column=0, columnspan=1, padx=10, pady=8, sticky="S")
        self.face_select = tk.Radiobutton(self, text="Facial Recognition", variable=self.mode, value=1)
        self.face_select.grid(row=3, column=1, columnspan=1, padx=8, sticky='SW')
        self.gesture_select = tk.Radiobutton(self, text="Gesture Recognition", variable=self.mode, value=2)
        self.gesture_select.grid(row=4, column=1, columnspan=1, padx=8, pady=8, sticky='NW')
        self.state_label = tk.Label(self, textvariable=self.state_message)
        self.state_label.grid(row=3, column=9, columnspan=1, padx=8, sticky="SE")
        self.last_input_message_label = tk.Label(self, textvariable=self.last_input_message)
        self.last_input_message_label.grid(row=4, column=9, columnspan=1, pady=8, padx=8, sticky='NE')
        self.player = MediaPlayer()
        self.player.player.set_hwnd(self.frame.winfo_id())

    def center_window(self):
        w = 1200
        h = 700
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2) - 100
        self.root.geometry('+%d+%d' % (x, y))

    def initialize_player(self):
        url = self.url_input.get("1.0", "end-1c")
        while not self.player.validate_url(url):
            self.update_status("Invalid URL")
        self.player.initialize(url)

    def current_mode(self):
        return self.mode.get()

    def update_state_status(self, message):
        self.state_message.set(message)

    def update_last_call(self, call):
        if call == 0:
            message = "Last Input Received: play"
            self.last_input_message.set(message)

        elif call == 1:
            message = "Last Input Received: pause"
            self.last_input_message.set(message)

        elif call == 2:
            message = "Last Input Received: jump forward"
            self.last_input_message.set(message)

        elif call == 3:
            message = "Last Input Received: jump back"
            self.last_input_message.set(message)

        elif call == 4:
            message = "Last Input Received: volume up ( " + str(self.player.get_volume()) + " )"
            self.last_input_message.set(message)

        elif call == 5:
            message = "Last Input Received: volume down ( " + str(self.player.get_volume()) + " )"
            self.last_input_message.set(message)

    def update_time(self):
        time = self.player.get_time()
        percent_complete = 0
        if time[1] != 0:
            percent_complete = (time[0]/time[1]) * 100
        self.progress["value"] = percent_complete
        minute = int(int(time[0]/1000) / 60)
        second = int(time[0]/1000) % 60
        if second < 10:
            formatted_time = str(minute) + ":0" + str(second)
        else:
            formatted_time = str(minute) + ":" + str(second)
        self.player_time.set(formatted_time)
