class Song:

    def __init__(self, title, artist, duration):

        self.title = title
        self.artist = artist
        self.duration = duration

        self.play_count = 0

    def increment_play_count(self):

        self.play_count += 1

my_song = Song("Kesariya", "Arijit Singh", 268)


print("Play Count:", my_song.play_count)

my_song.increment_play_count()
print("Play Count:", my_song.play_count)

my_song.increment_play_count()
print("Play Count:", my_song.play_count)

my_song.increment_play_count()
print("Play Count:", my_song.play_count)