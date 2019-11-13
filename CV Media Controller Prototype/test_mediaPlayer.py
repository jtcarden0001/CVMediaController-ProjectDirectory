from unittest import TestCase
from MediaModule import MediaPlayer


class TestMediaPlayer(TestCase):
    def setUp(self):
        self.media_player = MediaPlayer()

    def test_play(self):
        self.media_player.play()
        assert (self.media_player.state == 0)

    def test_pause(self):
        self.media_player.pause()
        assert (self.media_player.state == 1)

    def test_increase_volume(self):
        # test with volume below 100
        starting_volume = 50
        self.media_player.volume = starting_volume
        self.media_player.increase_volume()
        assert (self.media_player.volume == starting_volume + 2)

        # test with volume already at max
        starting_volume = 100
        self.media_player.volume = starting_volume
        self.media_player.increase_volume()
        assert (self.media_player.volume == starting_volume)

    def test_decrease_volume(self):
        # test with volume above 0
        starting_volume = 50
        self.media_player.volume = starting_volume
        self.media_player.decrease_volume()
        assert (self.media_player.volume == starting_volume - 2)

        # test with volume already at min
        starting_volume = 0
        self.media_player.volume = starting_volume
        self.media_player.decrease_volume()
        assert (self.media_player.volume == starting_volume)

    def test_get_volume(self):
        assert (self.media_player.volume == self.media_player.get_volume())

    def test_get_state(self):
        assert (self.media_player.state == self.media_player.get_state())
