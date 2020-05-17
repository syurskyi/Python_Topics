#!/usr/bin/python
from configparser _____ ConfigParser


def config(filename_'database.ini', section_'postgresql'):
    # create a parser
    parser _ ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db _ {}
    __ parser.has_section(section):
        params _ parser.items(section)
        ___ param __ params:
            db[param[0]] _ param[1]
    ____
        raise Exception('Section @ not found in the @ file'.f..(section, filename))

    return db

