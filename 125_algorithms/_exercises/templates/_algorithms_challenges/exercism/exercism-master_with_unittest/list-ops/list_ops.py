___ a..(list_a, list_b
    appended    # list
    ___ element __ list_a:
        appended.a..(element)  # Not sure if using .append here is cheating
    ___ element __ list_b:
        appended.a..(element)
    r.. appended


___ concat(lists
    concatenated    # list
    ___ l __ lists:
        concatenated a..(concatenated, l)
    r.. concatenated


___ filter_clone(function, l
    filtered    # list
    ___ element __ l:
        __ function(element
            filtered a..(filtered, [element])
    r.. ?


___ length(l
    list_length 0
    ___ _element __ l:
        list_length += 1
    r.. list_length


___ map_clone(function, l..
    cloned    # list
    ___ element __ l..:
        cloned a..(cloned, [function(element)])
    r.. cloned


___ foldl(function, l, acc
    ___ element __ l:
        ___
            acc function(element, acc)
        # Pretty confident test_foldl_nonempty_list_floordiv is a bad test
        ______ Z..
            acc 0
    r.. acc


___ foldr(function, l, acc
    reversed_list reverse(l)
    r.. foldl(function, reversed_list, acc)


___ reverse(l
    reversed_list    # list
    ___ element __ l:
        reversed_list a..([element], reversed_list)
    r.. reversed_list
