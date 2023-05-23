from collections import defaultdict


class Song:
    count = 0
    genres = []
    artists = []
    genre_count = defaultdict(int)
    artist_count = defaultdict(int)
    def __init__(self, name, artist, genre):
        Song.count += 1
        self.name = name
        self.artist = artist
        self.genre = genre
        self.genres.append(genre)
        self.artists.append(artist)
        Song.add_to_genres()
        Song.add_to_artists()
        Song.genre_count[genre] += 1
        Song.artist_count[artist] += 1

    @classmethod
    def add_to_genres(cls):
        unique_genres = list(set(cls.genres))
        cls.genres = unique_genres   

    @classmethod
    def add_to_artists(cls):
        unique_artists = list(set(cls.artists))
        cls.artists = unique_artists 

    @classmethod
    def add_to_genre_count(cls):
        for genre in set(cls.genres):
            cls.genre_count[genre] = cls.genres.count(genre)  


    @classmethod
    def add_to_artist_count(cls):
        for artist in set(cls.artists):
            cls.artist_count[artist] = cls.artists.count(artist)
        


    


     
