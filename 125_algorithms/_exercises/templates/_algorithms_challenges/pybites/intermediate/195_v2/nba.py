____ collections _______ n..
_______ csv
_______ os
____ pathlib _______ Path
_______ pandas as pd
_______ sqlite3
_______ random
_______ string

_______ requests

DATA_URL = 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
TMP = Path(os.getenv("TMP", "/tmp"))

salt = ''.j..(
    random.choice(string.ascii_lowercase) ___ i __ r..(20)
)
DB = TMP / f'nba_{salt}.db'

Player = n..('Player', ('name year first_year team college active '
                               'games avg_min avg_points'))

conn = sqlite3.connect(DB)
cur = conn.cursor()


___ import_data():
    with requests.Session() as session:
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


import_data()


# you code:

nba = pd.read_sql('SELECT * FROM players',conn)



nba = nba.apply(pd.to_numeric,errors='ignore')







___ player_with_max_points_per_game():
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""



    r.. nba.nlargest(1,'avg_points').squeeze()['name']

    





___ number_of_players_from_duke():
    """Return the number of players with college == Duke University"""
    r.. (nba.college __ 'Duke University').s..()


___ avg_years_active_players_stanford():
    """Return the average years that players from "Stanford University
       are active ("active" column)"""

    r.. nba.loc[nba.college __ 'Stanford University','active'].astype('int').mean()


___ year_with_most_drafts():
    """Return the year with the most drafts, in SQL you can use GROUP BY"""

    r.. int(nba.groupby('year').size().idxmax())

