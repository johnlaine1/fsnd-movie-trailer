import movie
from mtw_utils import get_template

despicable_me = movie.Movie(
    'Despicable Me',
    'Gru tries to take over the world',
    'https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg',
    'https://www.youtube.com/watch?v=fNPcZWsTgf0',
    get_template('templates/movie_tile_content.html')
    )
the_goonies = movie.Movie(
    'The Goonies',
    'In order to save their home from foreclosure, a group of misfits set out to find a pirate\'s ancient valuable treasure.',
    'https://upload.wikimedia.org/wikipedia/en/c/c6/The_Goonies.jpg',
    'https://www.youtube.com/watch?v=5qA2s_Vh0uE',
    get_template('templates/movie_tile_content.html')
    )    
love_actually = movie.Movie(
    'Love Actually',
    'Follows the lives of eight very different couples in dealing with their love lives in various loosely interrelated tales all set during a frantic month before Christmas in London, England.',
    'https://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg',
    'https://www.youtube.com/watch?v=cYCkFTyADJ0',
    get_template('templates/movie_tile_content.html')
    )
tangled = movie.Movie(
    'Tangled',
    'The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really is.',
    'https://upload.wikimedia.org/wikipedia/en/a/a8/Tangled_poster.jpg',
    'https://www.youtube.com/watch?v=ip_0CFKTO9E',
    get_template('templates/movie_tile_content.html')
    )
pulp_fiction = movie.Movie(
    'Pulp Fiction',
    'The lives of two mob hit men, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
    'https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg',
    'https://www.youtube.com/watch?v=s7EdQ4FqbhY',
    get_template('templates/movie_tile_content.html')
    )
the_matrix = movie.Movie(
    'The Matrix',
    'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
    'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
    'https://www.youtube.com/watch?v=m8e-FF8MsqU',
    get_template('templates/movie_tile_content.html')
    )
                            
movies = [despicable_me, the_goonies, love_actually, tangled, pulp_fiction, the_matrix]
