____ c.. _______ n..
_______ c__
_______ __
____ p.. _______ P..
_______ sqlite3
_______ r__
_______ s__

_______ r__

DATA_URL 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
TMP P..(__.g..("TMP", "/tmp"

salt ''.j..(
    r__.c..(s__.a..) ___ i __ r..(20)
)
DB TMP / f'nba_{salt}.db'

Player n..('Player', ('name year first_year team college active '
                               'games avg_min avg_points'

conn sqlite3.connect(DB)
cur conn.cursor()


___ import_data
    w__ r__.S.. __ session:
        content session.g.. DATA_URL).content.d.. 'utf-8')

    reader c__.DictReader(content.s.. , delimiter=',')

    players    # list
    ___ row __ reader:
        players.a..(Player(name=row 'Player' ,
                              year=row 'Draft_Yr' ,
                              first_year=row 'first_year' ,
                              team=row 'Team' ,
                              college=row 'College' ,
                              active=row 'Yrs' ,
                              games=row 'Games' ,
                              avg_min=row 'Minutes.per.Game' ,
                              avg_points=row 'Points.per.Game'

    cur.execute('''CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)''')
    cur.executemany('INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)', players)
    conn.commit()


import_data()


# you code:

___ player_with_max_points_per_game
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    cursor cur.execute(
        """
        SELECT 
            name,
            MAX(CAST(avg_points AS INT)) AS points
        FROM players
        """)
    r.. next(cursor)[0]


___ number_of_players_from_duke
    """Return the number of players with college == Duke University"""
    cursor cur.execute(
        """
        SELECT
            COUNT(*) AS record_count
        FROM players
        WHERE college = 'Duke University'
        """
    )
    r.. next(cursor)[0]


___ avg_years_active_players_stanford
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    cursor cur.execute(
        """
        SELECT
            AVG(active) AS avg_years
        FROM players
        WHERE college = 'Stanford University'
        """
    )
    r.. next(cursor)[0]


___ year_with_most_new_players
    """Return the year with the most new players.
       Hint: you can use GROUP BY on the year column.
    """
    cursor cur.execute(
        """
        WITH years_staging AS (
            SELECT
                COUNT(CAST(first_year AS INT)) new_players,
                year
            FROM players
            GROUP BY year)

        SELECT MAX(new_players), year
        FROM years_staging
        """
    )
    r.. next(cursor)[1]


# if __name__ == "__main__":
#     print(player_with_max_points_per_game())
#     print(number_of_players_from_duke())
#     print(avg_years_active_players_stanford())
#     print(year_with_most_new_players())