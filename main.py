import os
import movie_data

# Fetch template file contents
def get_template(file):
    template_file = open(file, 'r')
    content = template_file.read()
    template_file.close()
    return content

# Render the movie tile content
def create_movie_tiles_content(movies):
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
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    
create_index_file(movie_data.movies)