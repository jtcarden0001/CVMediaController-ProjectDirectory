import vlc


def setup_player(URL):
    vlc_instance = vlc.Instance('--fullscreen')
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(URL)
    media_list = vlc_instance.media_list_new([URL])
    player.set_media(media)
    list_player = vlc_instance.media_list_player_new()
    list_player.set_media_player(player)
    list_player.set_media_list(media_list)
    list_player.play()
    while True:
        pass


setup_player("https://www.youtube.com/watch?v=EngW7tLk6R8")
