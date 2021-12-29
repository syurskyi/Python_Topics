_______ itertools
___ changed_dependencies(old_reqs: str, new_reqs: str) -> l..:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    mapping = {}


    ___ req __ old_reqs.strip().splitlines():
        print(req)
        package,value = req.split("==")
        mapping[package] = l..(map(int,value.split('.')))

    

    upgrades    # list

    ___ req __ new_reqs.strip().splitlines():
        package,value = req.split('==')
        old_version = mapping[package]

        new_version = l..(map(int,value.split('.')))

        ___ n1,n2 __ itertools.zip_longest(old_version,new_version,fillvalue=0):
            __ n2 > n1:
                upgrades.a..(package)
            ____ n2 < n1:
                break


    r.. upgrades















