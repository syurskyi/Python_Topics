import itertools
___ changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    mapping = {}


    for req in old_reqs.strip().splitlines():
        print(req)
        package,value = req.split("==")
        mapping[package] = list(map(int,value.split('.')))

    

    upgrades = []

    for req in new_reqs.strip().splitlines():
        package,value = req.split('==')
        old_version = mapping[package]

        new_version = list(map(int,value.split('.')))

        for n1,n2 in itertools.zip_longest(old_version,new_version,fillvalue=0):
            __ n2 > n1:
                upgrades.append(package)
            elif n2 < n1:
                break


    return upgrades















