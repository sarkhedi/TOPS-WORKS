class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

my_song = Song("Kesariya", "Arijit Singh", 268)


print("Song Title:", my_song.title)
print("Artist:", my_song.artist)