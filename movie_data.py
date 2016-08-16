import requests
import movie
from mtw_utils import get_template

def get_movie_data(movie_id):
    '''Fetch movie data from external API

    Args:
        movie_id: (str) The ID of the movie as provided by API provider.

    Returns:
        A dict of data about the requested movie.
    '''

    base_url = 'https://api.themoviedb.org/3/movie/'
    API_KEY = '9c23d458160dc620ec8a017d584552f5'
    req_params = {'api_key': API_KEY}

    # Fetch the movie data.
    movie_req = requests.get(base_url + movie_id, params=req_params)
    movie_res = movie_req.json()

    # Fetch the trailer data, unfortunately the trailer url is not available
    # in the movie request object, so we need to make an additional call.
    trailer_req = requests.get(base_url + movie_id + '/videos', params=req_params)
    trailer_res = trailer_req.json()
    # Fetch just the first trailer as sometimes there are multiple versions.
    trailer_url = trailer_res['results'][0]['key']

    return {'movie_info': movie_res, 'trailer_url': trailer_url}

def create_movie(movie_id):
    '''Creates an instance of a Movie

    Args:
        movie_id: (str) A movie ID as provided by the API provider.

    Returns:
        A Movie object.
    '''

    movie_data = get_movie_data(movie_id)
    movie_info = movie_data['movie_info']
    trailer_url = movie_data['trailer_url']

    genres = []
    # Get all the genres for the movie and convert to lowercase
    for genre in movie_info['genres']:
        genres.append(genre['name'].lower())

    # Create the object.
    movie_obj = movie.Movie(
        movie_info['title'],
        movie_info['overview'],
        'https://image.tmdb.org/t/p/original' + movie_info['poster_path'],
        'https://youtu.be/' + trailer_url,
        get_template('templates/movie_tile_content.html'),
        genres
        )

    return movie_obj

def get_movies(movie_ids):
    '''Get a list of Movie objects

    Args:
        movie_ids: A list of ids(str) as provided by the API provider.

    Returns:
        A list of Movie objects.
    '''

    movies = []
    for movie_id in movie_ids:
        movie = create_movie((movie_id))
        movies.append(movie)

    return movies

