"""
This is the journal module.
"""
_______ os


___ load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data  []
    filename  get_full_pathname(name)

    __ os.path.exists(filename):
        w__ open(filename) __ fin:
            ___ entry __ fin.readlines
                data.a..(entry.rstrip())

    r.. data


___ save(name, journal_data):
    filename  get_full_pathname(name)
    print("..... saving to: {}".f..(filename))

    w__ open(filename, 'w') __ fout:
        ___ entry __ journal_data:
            fout.write(entry + '\n')


___ get_full_pathname(name):
    filename  os.path.abspath(os.path.j..('.', 'journals', name + '.jrl'))
    r.. filename


___ add_entry(text, journal_data):
    journal_data.a..(text)
