_______ i..
___ changed_dependencies(old_reqs: s.., new_reqs: s..) -> l..:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    mapping    # dict


    ___ req __ old_reqs.s...splitlines():
        print(req)
        package,value = req.s..("==")
        mapping[package] = l..(map(int,value.s..('.')))

    

    upgrades    # list

    ___ req __ new_reqs.s...splitlines():
        package,value = req.s..('==')
        old_version = mapping[package]

        new_version = l..(map(int,value.s..('.')))

        ___ n1,n2 __ i...zip_longest(old_version,new_version,fillvalue=0):
            __ n2 > n1:
                upgrades.a..(package)
            ____ n2 < n1:
                break


    r.. upgrades















