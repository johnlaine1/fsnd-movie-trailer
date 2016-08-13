import re

class Movie():
    ''' A class used to store movie related information .
    
    Attributes:
        title (str): The title of the movie.
        storyline (str): A brief description of the movie.
        poster_image (str): A URL to an image file of poster for the movie.
        trailer_youtube_url: A URL to a youtube video for the movie.
        template (str): A html template used to render the movie.
        
    '''
    
    def __init__(self, title, storyline, poster_image, 
                 trailer, template):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        self.template = template
        
    def render(self):
        ''' Render the movie into html '''
        
        content = ''
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        content = self.template.format(
            movie_title=self.title,
            poster_image_url=self.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
        
        return content
