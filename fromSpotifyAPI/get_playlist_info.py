from intake import get_playlist_data
from spotipy.oauth2 import SpotifyClientCredentials
import config


def retrieve_playlist_info(playlist_id='37i9dQZF1DX0kbJZpiYdZl'):
    auth_manager = SpotifyClientCredentials(client_id='6c3b776619c14dba9a9800450215a2f9',
                                            client_secret=config.client_secret)

    all_track_data = get_playlist_data(auth_manager, playlist_id)

    return all_track_data


if __name__ == "__main__":
    retrieve_playlist_info()
