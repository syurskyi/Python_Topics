# genpickle.py
#
# Turn a sequence of objects into a sequence of pickle strings

______ pickle

___ gen_pickle(source):
    ___ item __ source:
        y... pickle.dumps(item)

___ gen_unpickle(infile):
    while True:
        try:
            item = pickle.load(infile)
            y... item
        except EOFError:
            return

