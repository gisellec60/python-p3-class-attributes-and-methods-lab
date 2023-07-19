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
            cls.genres.extend((self.genre,1))
        else:
            for x, genre in enumerate(cls.genres):
                if isinstance(genre, str):
                   if self.genre == genre: 
                        cls.genres[x+1] = cls.genres[x+1] + 1
                        
        # print("this is genres", cls.genres)
        return cls.genres
    
    @classmethod
    def add_to_artists(cls, self):
        if self.artist not in cls.artists:
            cls.artists.extend((self.artist,1))
        else:
            for x, artist in enumerate(cls.artists):
                if isinstance(artist, str):
                   if self.artist == artist: 
                        cls.artists[x+1] = cls.artists[x+1] + 1
        # print("this is artists", cls.artists)
        return cls.artists
    
    @classmethod  
    def add_to_genre_count(cls):
        genre_count = {cls.genres[i]: cls.genres[i+1] for i in range(0,len(cls.genres),2)}    
        cls.genre_count=genre_count
        # print("this is the dict", cls.genre_count) 
        return Song.genre_count
    
    @classmethod  
    def add_to_artist_count(cls):
        artist_count = {cls.artists[i]: cls.artists[i+1] for i in range(0,len(cls.artists),2)}    
        cls.artist_count=artist_count
        # print("this is the dict", cls.artist_count) 
        return cls.artist_count            

# Song("99 Problems", "Jay Z", "Rap")
# Song("Halo", "Beyonce", "Pop")
# Song("Smells Like Teen Spirit", "Nirvana", "Rock")  
# Song("Sara Smile", "Hall and Oates", "Pop")
# Song("Out of Touch", "Hall and Oates", "Pop")
# # Song.add_to_genre_count()
# # print("the list", Song.genres)
# # print("Song.genre_count['Rap'] =", Song.genre_count['Rap'])  
# # print("the list", Song.artists)
# Song.add_to_artist_count()
# print("Song.artist_count['Jay Z'] =", Song.artist_count['Jay Z'])             