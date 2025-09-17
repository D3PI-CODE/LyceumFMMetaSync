import requests
import time

# --- FILE CONFIGURATION ---
SONG_FILE = 'current_song.txt'      # File for the song name
ARTIST_FILE = 'current_artist.txt'  # File for the artist name

# --- USER CONFIGURATION ---
SPREADSHEET_ID = 'your-spreadsheet-id'  # Your spreadsheet ID
SHEET_NAME = 'Sheet1'  # Your sheet name
ROW_NUMBER = 1  # The row you want to read (1-based)
INTERVAL_MS = 1000  # How often to collect data (in milliseconds)
API_KEY = 'your-api-key'  # Your Google Sheets API key

# Construct the Google Sheets API URL
base_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{SHEET_NAME}!A{ROW_NUMBER}:ZZ{ROW_NUMBER}"
url = f"{base_url}?key={API_KEY}"

# Function to fetch data from Google Sheets
def get_row_data():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'values' in data and len(data['values']) > 0:
                return data['values'][0]
            else:
                return []
        elif response.status_code == 403:
            print("\nAccess Denied Error! Please check:")
            print("1. Your API key is correct")
            print("2. The API key has access to Google Sheets API")
            print("3. The spreadsheet is public (viewable by anyone with the link)")
            raise Exception(f"Access denied: {response.json()}")
        else:
            raise Exception(f"API request failed: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error: {e}")

# Function to write data to files
def write_to_files(values):
    try:
        if not values:
            return None, None
            
        # Get the first cell which should contain "songname-artist"
        full_text = str(values[0]).strip()
        
        # parse song and artist
        # format can be "songname-artist" or "prefix:songname-artist"
        # the prefix can be anything and is ignored, used for Categorization
        if ':' in full_text:
            parts = full_text.split(':', 1)
            songdetails = parts[1].strip()
            if '-' in songdetails:
                parts = songdetails.split('-', 1)  # Split on first dash only
                song_name = parts[0].strip()
                artist_name = parts[1].strip() if len(parts) > 1 else "Unknown Artist"
            else:
                song_name = full_text
                artist_name = "Unknown Artist"
        else:
            if '-' in full_text:
                parts = full_text.split('-', 1)  # Split on first dash only
                song_name = parts[0].strip()
                artist_name = parts[1].strip() if len(parts) > 1 else "Unknown Artist"
            else:
                song_name = full_text
                artist_name = "Unknown Artist"
            
        # Write song name to song file
        with open(SONG_FILE, 'w', encoding='utf-8') as f:
            f.write(song_name)
            
        # Write artist name to artist file
        with open(ARTIST_FILE, 'w', encoding='utf-8') as f:
            f.write(artist_name)
            
        return song_name, artist_name
            
    except Exception as e:
        print(f"Error writing to files: {e}")
        return None, None

# initial status message
print(f"Starting to monitor row {ROW_NUMBER} of spreadsheet {SPREADSHEET_ID}")
print(f"Checking every {INTERVAL_MS}ms...")
print(f"Song name will be written to: {SONG_FILE}")
print(f"Artist name will be written to: {ARTIST_FILE}")
print("Press Ctrl+C to stop\n")

# Main loop
while True:
    try:
        row_values = get_row_data()
        if not row_values:  # Skip if no values returned
            print(f"[{time.strftime('%H:%M:%S')}] No values received")
            continue
            
        song, artist = write_to_files(row_values)
        if song and artist:
            print(f"[{time.strftime('%H:%M:%S')}] Updated - Song: {song} | Artist: {artist}")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Failed to parse song and artist from: {row_values}")
            
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Error: {e}")
    time.sleep(INTERVAL_MS / 1000.0)