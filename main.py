"""main.py"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

config = dotenv_values(".env")

scope = ["user-read-private", "user-library-read", "user-library-modify",
         "user-read-recently-played", "user-top-read", "user-read-playback-position",
         "playlist-modify-public", "playlist-modify-private", "playlist-read-collaborative",
         "playlist-read-private", "streaming", "app-remote-control",
         "user-read-currently-playing", "user-modify-playback-state", "user-read-playback-state",
         "ugc-image-upload"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config["CLIENT_ID"],
                                               client_secret=config["CLIENT_SECRET"],
                                               redirect_uri="http://localhost:8000/callback",
                                               scope=scope))

""" results = sp.current_user_top_artists(limit=10, time_range="long_term")
print(len(results))
print(results.keys())
print(len(results["items"]))
for i in results["items"]:
    print(i["name"]) """

print(sp.me())
sp.pause_playback()
