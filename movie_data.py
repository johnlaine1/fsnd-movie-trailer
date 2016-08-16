import requests
import movie
from mtw_utils import get_template

def get_movie_data(movie_id):
    base_url = 'https://api.themoviedb.org/3/movie/'
    API_KEY = '9c23d458160dc620ec8a017d584552f5'
    req_params = {'api_key': API_KEY}
    
    # fetch the movie data
    movie_req = requests.get(base_url + movie_id, params=req_params)
    movie_res = movie_req.json()
    
    # Fetch the trailer data, unfortunately the trailer url is not available 
    # in the movie request object.
    trailer_req = requests.get(base_url + movie_id + '/videos', params=req_params)
    trailer_res = trailer_req.json()
    trailer_url = trailer_res['results'][0]['key']
    
    return {'movie_info': movie_res, 'trailer_url': trailer_url}


def create_movie(movie_id):
    
    movie_data = get_movie_data(movie_id)
    movie_info = movie_data['movie_info']
    trailer_url = movie_data['trailer_url']
    
    genres = []
    for genre in movie_info['genres']:
        genres.append(genre['name'].lower())
    
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
    movies = []
    for movie_id in movie_ids:
        movie = create_movie((movie_id))
        movies.append(movie)
    return movies


movie_ids = ['278', '238', '424', '20352', '9340', '637', '508', '38757', '680', '3049', '278927']

movies = get_movies(movie_ids)
