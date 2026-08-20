playlist_prices = {
    "Workout Mix": 100,
    "Chill Vibes": 150,
    "Party Hits": 200,
    "Study Music": 120,
    "Romantic Songs": 180
}

def update_playlist_price(playlist, new_price):
    playlist_prices[playlist] = new_price

update_playlist_price("Workout Mix", 250)
print(playlist_prices)