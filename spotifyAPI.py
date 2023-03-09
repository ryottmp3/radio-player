import json
import spotipy
import webbrowser

username = '0pzf1e7d76gox33onmdobm2w7'
clientID = 'ef56171a97204e91bb37ec4de0e483be'
clientSecret = 'a5d1e1be4f474c79b077ad00b485a33d'
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

# To print the response in readable format.
print(json.dumps(user_name, sort_keys=True, indent=4))

while True:
	print("Welcome to the project, " + user_name['display_name'])
	
