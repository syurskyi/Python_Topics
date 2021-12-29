IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5
import re


___ filter_names(names):

    
    result = []

    for name in names: 
        __ name.startswith(IGNORE_CHAR) or len(re.findall(r'\d',name)) >= 1:
            continue

        __ name.startswith(QUIT_CHAR) or len(result) >= MAX_NAMES:
            break


        result.append(name)

    return result
