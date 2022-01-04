____ collections _______ n..
_______ csv
_______ os
____ pathlib _______ Path
_______ sqlite3
_______ r__
_______ s__

_______ requests

DATA_URL = 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
TMP = Path(os.getenv("TMP", "/tmp"))

salt = ''.j..(
    r__.choice(s__.ascii_lowercase) ___ i __ r..(20)
)
DB = TMP / f'nba_{salt}.db'

Player = n..('Player', ('name year first_year team college active '
                               'games avg_min avg_points'))

conn = sqlite3.connect(DB)
cur = conn.cursor()


___ import_data
    w__ requests.Session() __ session:
        content = session.get(DATA_URL).content.decode('utf-8')

    reader = csv.DictReader(content.splitlines(), delimiter=',')

    players    # list
    ___ row __ reader:
        players.a..(Player(name=row['Player'],
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


__ DB.stat().st_size __ 0:
    print('loading data')
    import_data()


# you code:

___ player_with_max_points_per_game
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    r.. l..(cur.execute('''SELECT name
                               from players
                               where CAST(avg_points as numeric) =
                               (SELECT max(CAST(avg_points as numeric))
                               as max_points from players)'''))[0][0]


___ number_of_players_from_duke
    """Return the number of players with college == Duke University"""
    r.. l..(tuple(cur.execute('''SELECT name
                                  from players
                                  where college="Duke University"''')))


___ avg_years_active_players_stanford
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    average = tuple(cur.execute('''SELECT AVG(CAST(active as numeric))
                                 from players
                                 where college="Stanford University"'''))[0][0]
    r.. round(average, 2)


___ year_with_most_drafts
    """Return the year with the most drafts, in SQL you can use GROUP BY"""
    drafts = tuple(cur.execute('''SELECT CAST(year as numeric), COUNT(year)
                                from players
                                GROUP BY year
                                ORDER BY COUNT(year)'''))
    r.. drafts[-1][0]
