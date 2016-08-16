import movie_data
from mtw_utils import get_template

def render_movie_tiles(movies):
    '''Render the movie tile content.

    Converts the data from each movie into html and
    concatenates the html strings together.

    Args:
        movies: A list of movie objects

    Returns:
        An html string containing all movies.
    '''

    content = ''

    for movie in movies:
        content += movie.render()
    return content

def render_filter_items(movies):
    '''Render the list items for the genre filter

    Args:
        movies: A list of movie objects

    Returns:
        An string containing the html needed to render the list of
        genres contained in the movie objects.
        There will be no duplicate genres created.
    '''
    all_genres = []

    # Get the list of genres from each movie abdconcatenate them.
    for movie in movies:
        all_genres = all_genres + movie.genre

    # Filter out the duplicates from the genres list.
    genres = list(set(all_genres))

    # This is the 'All' filter selection
    content = '<li><a class="movie-filter" id="all" href="#">all</a></li>\n'

    # Create and concatenate the html needed to create the list of genres.
    # The \t were used so the html lines up better when the index.html is generated.
    for genre in genres:
        li = '\t\t\t\t\t\t<li><a class="movie-filter" id="{id}" href="#">{name}</a></li>'
        content += li.format(id=genre, name=genre) + '\n'

    return content

def render_index_file(movies):
    ''' Render the index.html file.

    Render the individual components and put them all together
    to render the index.html file.
    Creates or overwrites a file named index.html in the same
    directory as this file.

    Args:
        movies: A list of movie objects

    Returns: Nothing
    '''

    # Fetch the different content that will make up the index.html page.
    page_shell = get_template('templates/main_page_shell.html')
    page_content = get_template('templates/main_page_content.html')
    filter_items = render_filter_items(movies)
    movie_tiles = render_movie_tiles(movies)

    # Interpolate the page content with the movie tile content.
    content = page_content.format(movie_tiles=movie_tiles, filter_items=filter_items)

    # Interpolate the page with the content.
    page = page_shell.format(content=content)

    # Create or overwrite the output file
    output_file = open('index.html', 'w')
    output_file.write(page)
    output_file.close()

# A list of IDs obtained from 'The Movie DB', https://www.themoviedb.org/
# If you search for a movie and click on it, you will see a number in the URL
# This is the URL used by the program.
# If you add or remove IDs from the list, the related movie will be added or
# removed from the view along with the filter item for the related genre.
movie_ids = ['278', '238', '424', '20352', '9340', '637', '508', '38757', '680', '3049', '278927']

render_index_file(movie_data.get_movies(movie_ids))