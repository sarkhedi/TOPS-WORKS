class Song:

    def __init__(self, title, artist, duration):

        self.title = title
        self.artist = artist
        self.duration = duration

song1 = Song("Kesariya", "Arijit Singh", 268)

print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")