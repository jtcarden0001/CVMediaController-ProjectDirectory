# import validators
import vlc


class MediaPlayer:

    def __init__(self):
        self.state = 0  # may change these states into an enum
        self.volume = 50
        self.vlc_instance = vlc.Instance('--no-xlib --quiet')
        self.player = self.vlc_instance.media_player_new()
        self.placeholder = 0
        self.url = ""

    def validate_url(self, url):
        # TODO: Implement a function that can validate a YouTube URL

        # if not validators.url(url):
        #     return False
        return True

    def initialize(self, url):
        # TODO: modify the title in the media player title bar to "Computer Vision Media Controller" or it
        #  may be cool to extract data from the actual video to make the title dynamic
        if not self.validate_url(url):
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
        self.player.play()

    def pause(self):
        self.state = 1
        if self.player.is_playing():
            self.player.pause()

    def increase_volume(self):
        if self.volume < 100:
            self.volume = self.volume + 2
        self.player.audio_set_volume(self.volume)

    def decrease_volume(self):
        if self.volume > 0:
            self.volume = self.volume - 2
        self.player.audio_set_volume(self.volume)

    def get_volume(self):
        return self.volume

    def jump_forward(self):
        jump_to = self.player.get_time() + 10000
        self.player.set_time(jump_to)

    def jump_back(self):
        jump_to = self.player.get_time() - 10000
        self.player.set_time(jump_to)

    def get_state(self):
        return self.state

    def get_volume(self):
        return self.volume

    def get_time(self):
        return self.player.get_time()
