import movie_data
from mtw_utils import get_template

# Render the movie tile content
def render_movie_tiles(movies):
    # The HTML content for this section of the page
    content = ''

    for movie in movies:
        content += movie.render()
    return content

# Render the index file
def create_index_file(movies):
    main_page_head = get_template('templates/main_page_head.html')
    main_page_content = get_template('templates/main_page_content.html')
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=render_movie_tiles(movies))
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    
render_index_file(movie_data.movies)