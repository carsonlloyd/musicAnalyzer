import sys
import spotipy
from song import Song


def get_track_info(sp, id):
    try:
        track_info = sp.track(id)
        features_info = sp.audio_features(id)[0]
        audio_analysis = sp.audio_analysis(id)
        if track_info is not None and features_info is not None and audio_analysis is not None:
            return Song(track_info, features_info, audio_analysis)
        return None
    except spotipy.SpotifyException:
        return None


def get_playlist_tracks(sp, playlist_id):
    print("Retrieving playlist...")
    track_ids = []
    results = sp.playlist_items(playlist_id, market='US')
    playlist = results['items']
    while results['next']:
        results = sp.next(results)
        playlist.extend(results['items'])

    for track in playlist:
        t = track['track']
        if t is not None and t['track']:
            track_ids.append(t['id'])
    return track_ids


def get_playlist_data(credentials, playlist_id):
    print("Connecting to Spotify...")
    try:
        sp = spotipy.Spotify(auth_manager=credentials, requests_timeout=12, status_forcelist=(401, 403, 429), retries=3,
                             status_retries=3)
    except spotipy.SpotifyException:
        print("Unable to connect. Try again later.")
        sys.exit()

    track_ids = get_playlist_tracks(sp, playlist_id)

    print("Retrieving tracks' data", end="")
    tracks = []
    for track in track_ids:
        print(".", end="")
        sys.stdout.flush()
        this_track = get_track_info(sp, track)  # a Song type or None
        if this_track is not None:
            tracks.append(this_track)
    print(". " + str(len(tracks)))

    return tracks
