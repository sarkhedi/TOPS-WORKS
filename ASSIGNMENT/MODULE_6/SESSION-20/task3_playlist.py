class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)
        print(song, "added to playlist.")

    def remove_song(self, song):

        if song in self._songs:
            self._songs.remove(song)
            print(song, "removed from playlist.")
        else:
            print(song, "not found in playlist.")

    def get_songs(self):
        return self._songs

playlist = Playlist()


playlist.add_song("Kesariya")
playlist.add_song("Perfect")
playlist.add_song("Believer")


print("Current Playlist:", playlist.get_songs())

playlist.remove_song("Perfect")

print("Updated Playlist:", playlist.get_songs())