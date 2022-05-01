# ____ c.. _______ n..
# _______ c__
# ____ p.. _______ P..
# _______ _3
#
# _______ r__
#
# DATA_URL 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
# TMP P..('/tmp')
# DB TMP / 'nba.db'
#
# Player n..('Player', ('name year first_year team college active '
#                                'games avg_min avg_points'
#
# conn _____.c.. ?
# cur ?.c..
#
#
# ___ import_data
#     w__ r__.S.. __ session
#         content ?.g.. D...c__.d.. utf-8
#
#     reader c__.D.. ?.s..  d.._','
#
#     players    # list
#     ___ row __ ?
#         ?.a.. ? name_?'Player'
#                               year_?'Draft_Yr'
#                               first_year_? 'first_year'
#                               team_?'Team'
#                               college_? 'College'
#                               active_? 'Yrs'
#                               games_? 'Games'
#                               avg_min_? 'Minutes.per.Game'
#                               avg_points_? 'Points.per.Game'
#
#     ?.e.. '''CREATE TABLE IF NOT EXISTS players
#                   (name, year, first_year, team, college, active,
#                   games, avg_min, avg_points)''')
#     ?.e.. I.. I.. players V.. (?,?,?,?,?,?,?,?,?) ?
#     ?.c..
#
#
# __ __.s__ .s.. __ 0
#     print('loading data')
#     ?
#
#
# # you code:
#
# ___ player_with_max_points_per_game
#     """The player with highest average points per game (don't forget to CAST to
#        numeric in your SQL query)"""
#     ?.e.. S.. name avg_points F.. players O.. B. -avg_points L.. 0,1
#     result ?.f..
#     r.. ? 0 0
#
#
# ___ number_of_players_from_duke
#     """Return the number of players with college == Duke University"""
#     ?.e.. '''SELECT COUNT(*) FROM players WHERE college='Duke University';''')
#     result ?.f..
#     r.. ? 0 0
#
#
# ___ avg_years_active_players_stanford
#     """Return the average years that players from "Stanford University
#        are active ("active" column)"""
#     ?.e.. S.. A..(active) F.. players W.. college='Stanford University'
#     result ?.f..
#     r.. ? 0 0
#
#
# ___ year_with_most_drafts
#     """Return the year with the most drafts, in SQL you can use GROUP BY"""
#     ?.e.. S.. year, count(*) c F.. players group by year order by -c limit 0,1
#     result ?.f..
#     r.. ? 0 0
