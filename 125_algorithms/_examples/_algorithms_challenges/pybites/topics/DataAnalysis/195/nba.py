from collections import namedtuple
import csv
import os
from pathlib import Path
import sqlite3
import random
import string

import requests

DATA_URL = 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
TMP = Path(os.getenv("TMP", "/tmp"))

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = TMP / f'nba_{salt}.db'

Player = namedtuple('Player', ('name year first_year team college active '
                               'games avg_min avg_points'))

conn = sqlite3.connect(DB)
cur = conn.cursor()


def import_data():
    with requests.Session() as session:
        content = session.get(DATA_URL).content.decode('utf-8')

    reader = csv.DictReader(content.splitlines(), delimiter=',')

    players = []
    for row in reader:
        players.append(Player(name=row['Player'],
                              year=row['Draft_Yr'],
                              first_year=row['first_year'],
                              team=row['Team'],
                              college=row['College'],
                              active=row['Yrs'],
                              games=row['Games'],
                              avg_min=row['Minutes.per.Game'],
                              avg_points=row['Points.per.Game']))

    cur.execute('''CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)''')
    cur.executemany('INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)', players)
    conn.commit()


import_data()


# you code:

def player_with_max_points_per_game():
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    cur.execute('select name, max(cast(avg_points as float)) from players limit 1')
    player = cur.fetchone()
    return player[0]


def number_of_players_from_duke():
    """Return the number of players with college == Duke University"""
    cur.execute('select count(name) from players where college = "Duke University"')
    player = cur.fetchone()
    return player[0]

def avg_years_active_players_stanford():
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    cur.execute('select AVG(cast(active as int)) from players where college = "Stanford University"')
    player = cur.fetchone()
    return player[0]


def year_with_most_new_players():
    """Return the year with the most new players.
       Hint: you can use GROUP BY on the year column.
    """
    cur.execute('SELECT year, count(year) FROM players GROUP BY year ORDER BY count(year) DESC')
    player = cur.fetchone()
    return player[0]


#print(player_with_max_points_per_game())
#print(number_of_players_from_duke())
#print(avg_years_active_players_stanford())
print(year_with_most_new_players())