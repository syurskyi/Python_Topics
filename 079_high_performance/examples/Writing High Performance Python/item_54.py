import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 4
# db_connection.py
import sys

class Win32Database(object):
    pass

class PosixDatabase(object):
    pass

if sys.platform.startswith('win32'):
    Database = Win32Database
else:
    Database = PosixDatabase
