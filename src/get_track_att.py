import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_track_attributes(track_url):
    """
    Fetches the audio features of a track from Spotify.

    Parameters:
    track_url (str): The URL of the Spotify track.

    Returns:
    dict: A dictionary containing the audio features of the track.
    """
    # Set up authentication
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Get track ID or URL
    track_id = track_url.split('/')[-1].split('?')[0]

    # Get audio features
    features = sp.audio_features(track_id)[0]
    # Print attributes
    print(f"Danceability: {features['danceability']}")
    print(f"Energy: {features['energy']}")
    print(f"Tempo: {features['tempo']}")
    print(f"Valence: {features['valence']}")
    print(f"Loudness: {features['loudness']}")

    return features


