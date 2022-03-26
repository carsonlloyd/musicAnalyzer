import sys
from get_playlist_info import retrieve_playlist_info
from first_pass_analyzer import analyze_spotify
from song import Song

if __name__ == "__main__":
    pl_id = None

    if len(sys.argv) == 2:
        if len(sys.argv[1]) == 22 and sys.argv[1].isalnum():
            # try to treat this as a URI
            pl_id = sys.argv[1]
        else:
            # try to treat this as a URL with a URI on the end
            maybe_id = sys.argv[1].split('/')[-1]
            if len(maybe_id) == 22 and maybe_id.isalnum():
                pl_id = maybe_id

    if pl_id is not None:
        try:
            playlist_info = retrieve_playlist_info(pl_id)
            if isinstance(playlist_info, (list, Song)):
                analyze_spotify(playlist_info)
        except:
            print('Failed to retrieve playlist from specified URI/URL.')
            sys.exit()
    else:
        print('No URI/URL provided.')


# playlist_id = '6DecODNWI8oWRH8RrERv9p'  # carson playlist spring
# playlist_id = '37i9dQZF1EtqS787FW4VAD'  # steven top 2019
# playlist_id = '37i9dQZF1DX0kbJZpiYdZl'  # Hot Hits USA
# playlist_id = '6p21dRudS9FmcyGvKWPq2R'  # MH Random 30 Daily
# playlist_id = '26joDQXjEVcvfFQuUhLzTY'  # GM Random 1,000 Daily
