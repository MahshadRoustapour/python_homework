import requests

class iTunesSearch:
    def __init__(self):
        self.base_url = "https://itunes.apple.com/search"
    
    def search_music(self, track_name):
        # Prepare the API URL
        url = f"{self.base_url}?term={track_name}&media=music"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()['results']
        else:
            return []

class Track:
    def __init__(self, track_info):
        self.track_name = track_info.get('trackName', 'Unknown Track')
        self.artist_name = track_info.get('artistName', 'Unknown Artist')
        self.album_name = track_info.get('collectionName', 'Unknown Album')
        self.track_url = track_info.get('collectionViewUrl', '')
        
    def display_info(self):
        print(f"Track: {self.track_name}")
        print(f"Artist: {self.artist_name}")
        print(f"Album: {self.album_name}")
        print(f"Listen on iTunes: {self.track_url}")

class MusicSearchApp:
    def __init__(self):
        self.itunes_search = iTunesSearch()
    
    def start(self):
        print("Music Search!")
        track_name = input("Enter the name of the song: ").strip()
        results = self.itunes_search.search_music(track_name)
        
        if results:
            print(f"\nFound {len(results)} result(s):\n")
            for track_info in results:
                track = Track(track_info)
                track.display_info()
        else:
            print("Not found.")

if __name__ == "__main__":
    a1 = MusicSearchApp()
    