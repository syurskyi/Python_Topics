#!/usr/bin/python
from configparser _____ ConfigParser


def config(filename_'database.ini', section_'postgresql'):
    # create a parser
    parser _ ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db _ {}
    if parser.has_section(section):
        params _ parser.items(section)
        ___ param __ params:
            db[param[0]] _ param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.f..(section, filename))

    return db

