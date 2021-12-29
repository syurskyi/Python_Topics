from collections import Counter, defaultdict
from io import StringIO
import pandas as pd
import csv

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
    

    counts = defaultdict(Counter)
    

    for line in csv.DictReader(StringIO(content)):
        counts[line['Character']][line['Episode']] += len(line['Line'].split())

    return counts


if __name__ == "__main__":

    season = 1
    get_num_words_spoken_by_character_per_episode(get_season_csv_file(season))




