from MediaModule import MediaPlayer
import tkinter as tk


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
        self.status_message = tk.StringVar()
        self.status_message.set("Enter a YouTube URL and press start to begin!")
        self.center_window()
        self.frame = tk.Frame(self, width=1200, height=700, bd=5)
        self.frame.configure(bg="black")
        self.frame.grid(row=0, column=0, columnspan=100, padx=8, pady=8)
        self.url_label = tk.Label(self, text="YouTube URL:")
        self.url_label.grid(row=1, column=0, columnspan=1, sticky='E')
        self.url_input = tk.Text(self, height=1, width=50)
        self.url_input.grid(row=1, column=1, columnspan=1, padx=8, sticky='W')
        self.start_button = tk.Button(self, text='Start', command=self.initialize_player)
        self.start_button.grid(row=3, column=1, columnspan=2, padx=8)
        self.mode_label = tk.Label(self, text="Mode:")
        self.mode_label.grid(row=2, column=0, columnspan=1, padx=8, sticky='E')
        self.face_select = tk.Radiobutton(self, text="Facial Recognition", variable=self.mode, value=1)
        self.face_select.grid(row=2, column=1, columnspan=1, padx=8, sticky='W')
        self.gesture_select = tk.Radiobutton(self, text="Gesture Recognition", variable=self.mode, value=2)
        self.gesture_select.grid(row=3, column=1, columnspan=1, padx=8, sticky='W')
        self.status_label = tk.Label(self, textvariable=self.status_message)
        self.status_label.grid(row=4, column=0, columnspan=30, padx=8, sticky='W')
        self.player = MediaPlayer()
        self.player.player.set_hwnd(self.frame.winfo_id())

    def center_window(self):
        w = 1200
        h = 700
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.geometry('+%d+%d' % (x, y))

    def initialize_player(self):
        url = self.url_input.get("1.0", "end-1c")
        while not self.player.validate_url(url):
            self.update_status("Invalid URL")
        self.player.initialize(url)

    def current_mode(self):
        return self.mode.get()

    def update_status(self, message):
        self.status_message.set(message)