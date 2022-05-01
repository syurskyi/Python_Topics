____ c.. _______ n..
_______ c__
_______ __
____ p.. _______ P..
_______ _3
_______ r__
_______ s__

_______ r__

DATA_URL 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
TMP P.. __.g.. "TMP", "/tmp"

salt ''.j..(
    r__.c..(s__.a..) ___ i __ r..(20)
)
DB TMP / f'nba_{salt}.db'

Player n..('Player', ('name year first_year team college active '
                               'games avg_min avg_points'

conn _____.c.. ?
cur ?.c..


___ import_data
    w__ r__.S.. __ session:
        content ?.g.. D...c__.d.. utf-8

    reader c__.D.. ?.s..  d.._','

    players    # list
    ___ row __ ?
        ?.a.. ? name_?'Player'
                              year_?'Draft_Yr'
                              first_year_? 'first_year'
                              team_?'Team'
                              college_? 'College'
                              active_? 'Yrs'
                              games_? 'Games'
                              avg_min_? 'Minutes.per.Game'
                              avg_points_? 'Points.per.Game'

    ?.e.. '''CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)''')
    ?.e.. I.. I.. players V.. (?,?,?,?,?,?,?,?,?)' ?
    ?.c..


?


# you code:

___ player_with_max_points_per_game
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    ?.e.. 'select name, max(cast(avg_points as float)) from players limit 1')
    player cur.fetchone()
    r.. player[0]


___ number_of_players_from_duke
    """Return the number of players with college == Duke University"""
    ?.e.. 'select count(name) from players where college = "Duke University"')
    player cur.fetchone()
    r.. player[0]

___ avg_years_active_players_stanford
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    ?.e.. 'select AVG(cast(active as int)) from players where college = "Stanford University"')
    player cur.fetchone()
    r.. player[0]


___ year_with_most_new_players
    """Return the year with the most new players.
       Hint: you can use GROUP BY on the year column.
    """
    ?.e.. 'SELECT year, count(year) FROM players GROUP BY year ORDER BY count(year) DESC')
    player cur.fetchone()
    r.. player[0]


#print(player_with_max_points_per_game())
#print(number_of_players_from_duke())
#print(avg_years_active_players_stanford())
print(year_with_most_new_players