from packaging import version


def _load_reqs(reqs: str) -> dict:
    '''loads reqs into a dict with keys of package names
       and values of version numbers (converted to base 10 equivs)
    '''
    print(f'{reqs.splitlines()=}')
    lines = map(lambda x: x.split('=='), reqs.splitlines())
    reqs = {x[0]: version.parse(x[1]) for x in lines if x[0]}
    return reqs


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old, new = _load_reqs(old_reqs), _load_reqs(new_reqs)
    print(f'{old=}\n{new=}')
    return [pkg for pkg in new if new.get(pkg) > old.get(pkg)]
