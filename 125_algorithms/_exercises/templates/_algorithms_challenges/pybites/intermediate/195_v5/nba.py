____ c.. _______ n..
_______ c__
____ p.. _______ P..
_______ _3

_______ r__

DATA_URL 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
TMP P..('/tmp')
DB TMP / 'nba.db'

Player n..('Player', ('name year first_year team college active '
                               'games avg_min avg_points'

conn sqlite3.connect(DB)
cur conn.cursor()


___ import_data
    w__ r__.S.. __ session:
        content ?.g.. DATA_URL).c__.d.. utf-8

    reader c__.D.. content.s.. , d.._',')

    players    # list
    ___ row __ reader
        players.a..(? name=row 'Player' ,
                              year=row 'Draft_Yr' ,
                              first_year=row 'first_year' ,
                              team=row 'Team' ,
                              college=row 'College' ,
                              active=row 'Yrs' ,
                              games=row 'Games' ,
                              avg_min=row 'Minutes.per.Game' ,
                              avg_points=row 'Points.per.Game'

    ?.e.. '''CREATE TABLE IF NOT EXISTS players
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
    ?.e.. '''SELECT name, avg_points FROM players ORDER BY -avg_points LIMIT 0,1;''')
    result cur.fetchall()
    r.. result 0 0 


___ number_of_players_from_duke
    """Return the number of players with college == Duke University"""
    ?.e.. '''SELECT COUNT(*) FROM players WHERE college='Duke University';''')
    result cur.fetchall()
    r.. result 0 0 


___ avg_years_active_players_stanford
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    ?.e.. '''SELECT AVG(active) FROM players WHERE college='Stanford University';''')
    result cur.fetchall()
    r.. result 0 0 


___ year_with_most_drafts
    """Return the year with the most drafts, in SQL you can use GROUP BY"""
    ?.e.. '''SELECT year, count(*) c FROM players group by year order by -c limit 0,1;''')
    result cur.fetchall()
    r.. result 0 0 
