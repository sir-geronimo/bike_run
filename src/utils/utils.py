import os


def get_file_path(path, filename):
    directory = os.path.dirname(path)
    file = os.path.join(directory, filename)

    return file
