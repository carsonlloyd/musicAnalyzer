class Song:
    def __init__(self, track_info, features_info, audio_analysis):
        # save everything
        # self.all_info = track_info
        # self.all_features = features_info
        # self.all_analysis = audio_analysis

        # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-track
        self.name = track_info['name']
        self.artist = track_info['album']['artists'][0]['name']
        self.duration = track_info['duration_ms']
        self.popularity = track_info['popularity']

        # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features
        keys = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#/ab', 'a', 'a#/bb', 'b']
        # if features_info['key'] >= 0:  # https://en.wikipedia.org/wiki/Pitch_class
        #    self.key = keys[features_info['key']]
        #  else:
        #    self.key = False
        self.key = features_info['key']
        self.mode = features_info['mode']  # major=1/minor=0
        self.tempo = features_info['tempo']  # bpm
        self.time_signature = features_info['time_signature']
        self.valence = features_info['valence']  # 0-1, higher = happier
        self.energy = features_info['energy']  # 0-1, higher = more energy
        self.danceability = features_info['danceability']  # 0 to 1, higher = more danceable

        # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-analysis
        self.duration = audio_analysis['track']['duration']
        self.loudness = audio_analysis['track']['loudness']  # in dB, averaged
        # if audio_analysis['track']['tempo_confidence'] > 0.67:
        #    # if high confidence in analyzed tempo, use this rather than album metadata
        self.analyzed_tempo = audio_analysis['track']['tempo']  # bpm
        # if audio_analysis['track']['time_signature_confidence'] > 0.67:
        #    # if high confidence in analyzed time signature, use this rather than album metadata
        self.analyzed_time_signature = audio_analysis['track']['time_signature']
        # if audio_analysis['track']['key_confidence'] > 0.67:
        #    # if high confidence in analyzed key, use this rather than album metadata
        self.aa_key = audio_analysis['track']['key']
        # if audio_analysis['track']['mode_confidence'] > 0.67:
        #    # if high confidence in analyzed mode, use this rather than album metadata
        self.analyzed_mode = audio_analysis['track']['mode']
        # self.bars = audio_analysis['bars']['duration']  # LIST of bars, has ['confidence'] # seconds, length of bar
        # self.beats = audio_analysis['beats']['duration']  # LIST has ['confidence'] # seconds, duration of 1 beat
        self.sections = audio_analysis['sections']  # array of sections with various attributes per section
                                                    # large variations in rhythm or timbre
        self.segments = audio_analysis['segments']  # array of segments with various attributes per segment
                                                    # consistent sound during segment
        # self.tatums = audio_analysis['tatums']['duration']  # LIST lowest regular pulse train that a listener infers
        # audio_analysis['tatums']['confidence']
