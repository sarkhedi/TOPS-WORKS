
file = open("my_playlist.txt", "r")

for song in file:
    
    print(song.strip().upper())


file.close()