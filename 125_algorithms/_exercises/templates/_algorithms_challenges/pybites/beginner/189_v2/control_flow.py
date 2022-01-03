IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5
_______ __


___ filter_names(names):

    
    result    # list

    ___ name __ names:
        __ name.startswith(IGNORE_CHAR) o. l..(__.findall(r'\d',name)) >= 1:
            continue

        __ name.startswith(QUIT_CHAR) o. l..(result) >= MAX_NAMES:
            break


        result.a..(name)

    r.. result
