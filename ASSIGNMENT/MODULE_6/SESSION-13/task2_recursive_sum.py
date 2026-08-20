def sum_playlist_durations(durations):

    if len(durations) == 0:
        return 0

    return durations[0] + sum_playlist_durations(durations[1:])


playlist = [120, 200, 300, 180]

total_duration = sum_playlist_durations(playlist)

print("Total Playlist Duration:", total_duration, "seconds")