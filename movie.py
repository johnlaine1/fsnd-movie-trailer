import webbrowser

class Movie():
    ''' A class used to store movie related information '''
    def __init__(self, title, storyline, poster_image, 
                 trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)