___ filter_names(names):
    IGNORE_CHAR = 'b'
    QUIT_CHAR = 'q'
    MAX_NAMES = 5
    names_list = []
    names_list_number = 0
    for name in names:
        __ name not in names_list:
            __ name.isalpha():
                __ IGNORE_CHAR in name:
                    continue
                elif QUIT_CHAR in name:
                    break
                else:
                    __ names_list_number >= MAX_NAMES:
                        break
                    else:
                        names_list.append(name)
                        names_list_number += 1
    return names_list