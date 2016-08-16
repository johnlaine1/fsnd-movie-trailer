import movie_data
from mtw_utils import get_template

# Render the movie tile content
def render_movie_tiles(movies):
    # The HTML content for this section of the page
    content = ''

    for movie in movies:
        content += movie.render()
    return content

# Render the <li> for the 'Genre' filter
def render_filter_items(movies):
    all_genres = []
    
    # Get the list of genres from each movie, concatenate them and then filter
    # out the duplicates.
    for movie in movies:
        all_genres = all_genres + movie.genre
        
    genres = list(set(all_genres))
    
    # TODO: get all of the 
    content = '<li><a class="movie-filter" id="all" href="#">all</a></li>\n'
    for genre in genres:
        li = '\t\t\t\t\t\t<li><a class="movie-filter" id="{id}" href="#">{name}</a></li>'
        content += li.format(id=genre, name=genre) + '\n'
        
    return content
# Render the index file
def render_index_file(movies):
    ''' Create and combine the content to render the page and output
    to a file.
    '''
    
    # Fetch the different content that will make up our page.
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
    
render_index_file(movie_data.movies)