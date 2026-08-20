class InvalidDurationError(Exception):
    pass


def get_playlist_duration(songs):

    total_seconds = 0

  
    for duration in songs:

     
        if duration < 0:
            raise InvalidDurationError(
                "Song duration cannot be negative."
            )

        total_seconds += duration

    
    total_minutes = total_seconds / 60

    return total_minutes


songs = [180, 200, 240]

try:
    result = get_playlist_duration(songs)
    print("Total duration:", result, "minutes")

except InvalidDurationError as e:
    print("Error:", e)