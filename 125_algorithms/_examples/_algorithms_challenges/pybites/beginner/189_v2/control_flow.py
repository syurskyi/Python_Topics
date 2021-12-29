IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5
import re


def filter_names(names):

    
    result = []

    for name in names: 
        if name.startswith(IGNORE_CHAR) or len(re.findall(r'\d',name)) >= 1:
            continue

        if name.startswith(QUIT_CHAR) or len(result) >= MAX_NAMES:
            break


        result.append(name)

    return result
