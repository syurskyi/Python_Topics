IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5

___ filter_names(names):
    names_list    # list
    names_list_number = 0
    ___ name __ names:
        __ name n.. __ names_list:
            __ name.isalpha
                __ IGNORE_CHAR __ name:
                    continue
                ____ QUIT_CHAR __ name:
                    break
                ____:
                    __ names_list_number >= MAX_NAMES:
                        break
                    ____:
                        names_list.a..(name)
                        names_list_number += 1
    r.. names_list