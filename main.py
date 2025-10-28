import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# Load environment variables
load_dotenv()
spotify_client_id = os.getenv("SPOTIPY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
spotify_redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

# Ask user for a date
desired_date = input("What year would you like to travel to? (YYYY-MM-DD): ").strip()
year = desired_date.split("-")[0]  # Extract the year only

# Scrape Billboard Hot 100 for that date
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{desired_date}", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Billboard song titles selector
song_tags = soup.select("li.o-chart-results-list__item h3")
song_titles = [tag.get_text(strip=True) for tag in song_tags]

print(f"Scraped {len(song_titles)} song titles.")
print(song_titles[:10])  # Preview

# Spotify authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        redirect_uri=spotify_redirect_uri,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)

print("Logged in as:", sp.current_user()["display_name"])

# Search Spotify for each song title
song_uris = []

for title in song_titles:
    try:
        query = f"track:{title} year:{year}"
        result = sp.search(q=query, type="track", limit=1)
        track = result["tracks"]["items"][0]  # If no result → IndexError
        uri = track["uri"]
        song_uris.append(uri)
        print(f"✅ Found: {title}")
    except IndexError:
        print(f"⚠️ Not found on Spotify: {title}")
    except Exception as e:
        print(f"Error searching {title}: {e}")

print("\n✅ Finished searching!")
print(f"Total valid Spotify tracks: {len(song_uris)}")
pprint(song_uris[:10])  # Preview URIs

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{desired_date} Billboard 100",
    public=False
)
playlist_id = playlist["id"]
print(f"🎵 Playlist created: {playlist_id}")
sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris
)
print("✅ All songs added to the playlist!")
