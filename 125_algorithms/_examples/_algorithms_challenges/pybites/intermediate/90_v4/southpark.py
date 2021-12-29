from collections import Counter, defaultdict
import csv
import re
import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""

    words_spoken = defaultdict(Counter)
    rows = csv.reader(content.splitlines())
    next(rows)                  # skip header
    for row in rows:
        epi, char, line = row[1:]
        num_words = len(re.findall(r'(\S+)', line))
        words_spoken[char].update({epi: num_words})

    return words_spoken
