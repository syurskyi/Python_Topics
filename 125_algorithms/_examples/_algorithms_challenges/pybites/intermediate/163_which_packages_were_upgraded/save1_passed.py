def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = {}
    new = {}
    for entry in old_reqs.strip().split('\n'):
        x = entry.split('==')
        y = []

        for i in x[1].split('.'):
            if len(i) == 1:
                y.append('0' + str(i))
            else:
                y.append(str(i))

        old[x[0]] = ''.join(y)

    for entry in new_reqs.strip().split('\n'):
        x = entry.split('==')
        y = []

        for i in x[1].split('.'):
            if len(i) == 1:
                y.append('0' + str(i))
            else:
                y.append(str(i))
        new[x[0]] = ''.join(y)

    output = []
    for k1, v1 in old.items():
        for k2, v2 in new.items():
            if k1 == k2:
                if len(v1) > len(v2):
                    v1 = v1[:len(v2)]
                    if int(v2) > int(v1):
                        output.append(k1)
                elif len(v2) > len(v1):
                    v2 = v2[:len(v1)]
                    if int(v2) > int(v1):
                        output.append(k1)
                elif len(v1) == len(v2):
                    if int(v2) > int(v1):
                        output.append(k1)

    return output