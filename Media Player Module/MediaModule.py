import vlc


class MediaPlayer:

    def __init__(self):
        self.state = 0  # may change these states into an enum
        self.volume = 50
        self.vlc_instance = vlc.Instance('--fullscreen')
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
        self.url = url
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
