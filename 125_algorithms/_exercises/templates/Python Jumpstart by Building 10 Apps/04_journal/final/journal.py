"""
This is the journal module.
"""
import os


___ load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data  []
    filename  get_full_pathname(name)

    __ os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


___ save(name, journal_data):
    filename  get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


___ get_full_pathname(name):
    filename  os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


___ add_entry(text, journal_data):
    journal_data.append(text)
