# Billboard Hot 100 Spotify Playlist Generator

Create a private Spotify playlist using the Billboard Hot 100 chart from any date in history. Provide a date (`YYYY-MM-DD`) and the script will:

1. Scrape Billboard Hot 100 song titles from that day
2. Search for each track on Spotify
3. Create a private playlist in your Spotify account
4. Add all available tracks automatically

## 📌 Features

- Scrapes Billboard Hot 100 chart data
- Integrates with Spotify Web API (Spotipy)
- Auto-generates a private playlist
- Uses environment variables for secure credentials

## ✅ Requirements

- Python 3.8+
- Spotify Developer application credentials
- Required packages installed

## 🔧 Installation

- pip install requests beautifulsoup4 python-dotenv spotipy

## 🔐 Environment Setup
- Create a .env file in your project directory:
- SPOTIPY_CLIENT_ID=your_client_id_here
- SPOTIPY_CLIENT_SECRET=your_client_secret_here
- SPOTIPY_REDIRECT_URI=http://localhost:8888/callback

- The script will authenticate with Spotify, create a playlist, and populate it with songs from that date.

⚠️ Notes
	•	Some songs may not be available on Spotify
	•	Playlist is created as private
	•	Authorization tokens are stored in token.txt

🚀 Future Improvements
	•	Include chart ranking in playlist description
	•	Optional public playlist setting
	•	Support for additional Billboard charts

📄 License

This project is for educational and personal use only. Not affiliated with Spotify or Billboard.
