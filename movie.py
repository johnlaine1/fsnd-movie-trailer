class Movie():
    ''' A class used to store movie related information .
    
    Attributes:
        title (str): The title of the movie.
        storyline (str): A brief description of the movie.
        poster_image (str): A URL to an image file of poster for the movie.
        trailer_youtube_url: A URL to a youtube video for the movie.
        
    '''
    def __init__(self, title, storyline, poster_image, 
                 trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        
    def render_movie_tile(self):
        
