''' Utility functions for the Movie Trailer Website app '''

# Fetch template file contents
def get_template(file):
    template_file = open(file, 'r')
    content = template_file.read()
    template_file.close()
    return content