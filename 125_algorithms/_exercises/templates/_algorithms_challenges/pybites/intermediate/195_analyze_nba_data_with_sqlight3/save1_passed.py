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


___ import_data():
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


___ player_with_max_points_per_game():
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    return list(cur.execute('SELECT name '
                            'FROM players '
                            'ORDER BY CAST(avg_points as FLOAT) DESC'))[0][0]


___ number_of_players_from_duke():
    """Return the number of players with college == Duke University"""
    return len(list(cur.execute('SELECT name '
                                'FROM players '
                                'WHERE college = "Duke University"')))


___ avg_years_active_players_stanford():
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    return list(cur.execute('SELECT ROUND(AVG(active), 2) '
                            'FROM players '
                            'WHERE college = "Stanford University"'))[0][0]


___ year_with_most_drafts():
    """Return the year with the most drafts, in SQL you can use GROUP BY"""
    return list(cur.execute('SELECT year, COUNT(*) as draft_count '
                            'FROM players '
                            'GROUP BY year '
                            'ORDER BY draft_count DESC'))[0][0]