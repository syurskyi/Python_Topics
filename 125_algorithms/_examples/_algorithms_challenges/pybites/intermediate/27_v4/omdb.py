import sys
import re
import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    out_lst = []
    for file in files:
        with open(file) as f:
            out_lst.append(json.load(f))
    out_lst.sort(key=lambda m: m['Title'])
    return out_lst


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    return [m for m in movies if 'Comedy' in m['Genre']][0]['Title']


def _get_wins_noms(awards: str) -> int:
    """return the number of wins and noms from award string or 0 if none"""
    wins = re.findall(r'([0-9]+) ', awards)
    return sum(map(int, wins)) if wins else 0


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    return max(movies, key=lambda x: _get_wins_noms(x['Awards']))['Title']


def _get_runtime(runtime: str) -> int:
    """return the integer runtime from a runtime string"""
    return int(re.findall(r'([0-9]+) ', runtime)[0])


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    return max(movies, key=lambda x: _get_runtime(x['Runtime']))['Title']
