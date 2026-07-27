
jenn_playlist = [4.5, 2.8, 3.2, 5.0, 1.5]

def count_song_types(playlist):
    long_songs = 0
    short_songs = 0
    
    for duration in playlist:
        if duration >= 3.0:
            long_songs += 1
        else:
            short_songs += 1
            
    print("Long songs (>= 3.0 min):")
    print(long_songs)
    print("Short songs (< 3.0 min):")
    print(short_songs)


count_song_types(jenn_playlist)