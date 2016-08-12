import os
import re
import movie_list

def get_template(file):
    template_file = open(file, 'r')
    content = template_file.read()
    template_file.close()
    return content
    
def create_movie_tiles_content(movies):
    movie_tile_content = get_template('templates/movie_tile_content.html')

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


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
    
create_index_file(movie_list.movies)