''' Utility functions for the Movie Trailer Website app. '''

# Fetch template file contents
def get_template(file):
    '''Get the html string contained in a template file.

    Args:
        file: (str) A file location.

    Returns:
        The contents of the file.
    '''
    template_file = open(file, 'r')
    content = template_file.read()
    template_file.close()
    return content