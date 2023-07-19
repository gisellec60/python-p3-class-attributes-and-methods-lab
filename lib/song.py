class Song:

    count=0
    found = 'no'
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}

    def __init__(self, name, artist, genre):
        self.name=name
        self.genre=genre
        self.artist=artist

        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        
    @classmethod
    def add_song_to_count(cls):
        cls.count = cls.count + 1
        return cls.count
    
    @classmethod
    def add_to_genres(cls, self):
        if self.genre not in cls.genres:
            cls.genres.append(self.genre)
            cls.genre_count[self.genre]=1
        else:
            cls.genre_count[self.genre] += 1
        return cls.genres
         
    @classmethod
    def add_to_artists(cls, self):
        if self.artist not in cls.artists:
            cls.artists.append(self.artist)
            cls.artist_count[self.artist]=1
        else:
           cls.artist_count[self.artist] += 1
        return cls.artists
    
    @classmethod  
    def add_to_genre_count(cls):
        return cls.genre_count
    
    @classmethod  
    def add_to_artist_count(cls):
        # print("this is the dict", cls.artist_count) 
        return cls.artist_count            

