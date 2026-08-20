class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print(
            f"Playing 30-second preview of {self.title} by {self.artist}"
        )

my_song = Song("Kesariya", "Arijit Singh", 268)

my_song.play_preview()