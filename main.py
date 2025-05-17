import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

clientID = "ac79692b92f44ee2966e664e4913204e"
clientSecret= "f4312e476a814859b8036b539f41b1d5"
redirectURI = "http://127.0.0.1:8000/callback"
scope = "user-read-currently-playing"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID, client_secret=clientSecret, redirect_uri=redirectURI, scope=scope))

currentTrack = sp.currently_playing()['artists']
pprint(currentTrack)