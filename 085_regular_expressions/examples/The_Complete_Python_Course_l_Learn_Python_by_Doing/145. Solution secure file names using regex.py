import re


def is_filename_safe(filename):
    regex = '^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
    # ^[a-zA-Z0-9]      start with a-zA-Z0-9
    # [a-zA-Z0-9_()-]+      then only contains a-zA-Z0-9_()- for any number of times
    # (\.jpg|\.jpeg|\.png|\.gif)$       at last, it must end with one of the four extensions, remember to escape the dot
    # since we check from start to end, it can either match the whole string or none
    return re.match(regex, filename) is not None