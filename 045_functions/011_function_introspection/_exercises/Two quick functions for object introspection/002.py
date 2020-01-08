def oar(o):
    for at in dir(o):
        if not at.startswith('__') and not at.endswith('__'):
            print(at,)

oar({})