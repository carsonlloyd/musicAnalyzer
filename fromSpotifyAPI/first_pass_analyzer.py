import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def analyze_spotify(all_track_data):
    # simplify data
    # track_names = [track.name for track in all_track_data]
    # print(track_names)

    # key vs popularity
    track_keys = [track.key for track in all_track_data]
    track_pops = [track.popularity for track in all_track_data]
    keys = ['c', 'c#', 'd', 'eb', 'e', 'f', 'f#', 'g', 'ab', 'a', 'bb', 'b']
    plt.scatter(track_keys, track_pops)
    plt.xlabel('Melodic Key')
    plt.xticks(range(12), keys)
    plt.ylabel('Relative Popularity')
    plt.ylim([0, 100])
    plt.title('Melodic Key vs. Relative Popularity')
    plt.show()

    # mode vs popularity
    track_modes = [track.mode for track in all_track_data]
    analyzed_track_modes = [track.analyzed_mode for track in all_track_data]
    plt.scatter(analyzed_track_modes, track_pops, color='b', marker='o', label='Inferred')
    plt.scatter(track_modes, track_pops, color='r', marker='^', label='Given')
    plt.xlabel('Mode')
    plt.xticks(range(2), ['Major', 'Minor'])
    plt.xlim([-1, 2])
    plt.ylabel('Relative Popularity')
    plt.ylim([0, 100])
    plt.title('Mode vs. Relative Popularity')
    plt.legend()
    plt.show()

    # tempo vs popularity
    track_tempo = [track.tempo for track in all_track_data]
    analyzed_track_tempo = [track.analyzed_tempo for track in all_track_data]
    plt.scatter(analyzed_track_tempo, track_pops, color='b', marker='o', label='Inferred')
    plt.scatter(track_tempo, track_pops, color='r', marker='^', label='Given')
    plt.xlabel('Tempo (bpm)')
    plt.ylabel('Relative Popularity')
    plt.ylim([0, 100])
    plt.title('Tempo vs. Relative Popularity')
    plt.legend()
    sns.regplot(x=track_tempo, y=track_pops)
    plt.show()

    # time signature vs popularity
    track_ts = [track.time_signature for track in all_track_data]
    analyzed_track_ts = [track.analyzed_time_signature for track in all_track_data]
    plt.scatter(analyzed_track_ts, track_pops, color='b', marker='o', label='Inferred')
    plt.scatter(track_ts, track_pops, color='r', marker='^', label='Given')
    time_sigs = ['3/4', '4/4', '5/4', '6/4', '7/4']
    plt.xlabel('Time signature')
    plt.xticks(range(3, 8), time_sigs)
    plt.xlim([2, 8])
    plt.ylabel('Relative Popularity')
    plt.ylim([0, 100])
    plt.title('Time Signature vs. Relative Popularity')
    plt.legend()
    plt.show()

    # valence vs popularity
    track_valence = [track.valence for track in all_track_data]
    plt.scatter(track_valence, track_pops)
    plt.xlabel('Valence')
    plt.xlim([0, 1])
    plt.xticks(np.linspace(0, 1, 11),
               ['Negative', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', 'Positive'])
    plt.ylabel('Relative Popularity')
    plt.ylim([0, 100])
    plt.title('Valence vs. Relative Popularity')
    sns.regplot(x=track_valence, y=track_pops)
    plt.show()

    # energy vs popularity
    track_energy = [track.energy for track in all_track_data]
    plt.scatter(track_energy, track_pops)
    plt.xlabel('Energy')
    plt.xlim([0, 1])
    plt.xticks(np.linspace(0, 1, 11),
               ['Less\nEnergetic', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', 'More\nEnergetic'],
               rotation=60)
    plt.ylabel('Relative Popularity')
    plt.ylim([0, 100])
    plt.title('Energy vs. Relative Popularity')
    sns.regplot(x=track_energy, y=track_pops)
    plt.plot()
    plt.show()

    # danceability vs popularity
    track_danceability = [track.danceability for track in all_track_data]
    plt.scatter(track_danceability, track_pops)
    plt.xlabel('Danceability')
    plt.xlim([0, 1])
    plt.xticks(np.linspace(0, 1, 11),
               ['Less\nDanceable', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', 'More\nDanceable'],
               rotation=60)
    plt.ylabel('Relative Popularity')
    plt.ylim([0, 100])
    plt.title('Danceability vs. Relative Popularity')
    sns.regplot(x=track_danceability, y=track_pops)
    plt.plot()
    plt.show()
