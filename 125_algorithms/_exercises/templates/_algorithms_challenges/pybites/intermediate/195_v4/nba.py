# ____ c.. _______ n..
# _______ c__
# _______ __
# ____ p.. _______ P..
# _______ _3
# _______ r__
# _______ s__
#
# _______ r__
#
# DATA_URL 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
# TMP P.. __.g.. "TMP", "/tmp"
#
# salt ''.j..
#     r__.c.. s__.a.. ___ i __ r.. 20
#
# DB ? / _*nba_ ? .db
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
#                   games, avg_min, avg_points)'''
#     ?.e.. I.. I.. players V.. (?,?,?,?,?,?,?,?,?)' ?
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
#     r.. l.. ?.e.. S.. name
#                                f.. players
#                                w.. C..(avg_points a. numeric) =
#                                (S.. max(C..(avg_points as numeric))
#                                as max_points from players) 0 0
#
#
# ___ number_of_players_from_duke
#     """Return the number of players with college == Duke University"""
#     r.. l.. t.. ?.e.. S.. name
#                                   f.. players
#                                   w.. college="Duke University"
#
#
# ___ avg_years_active_players_stanford
#     """Return the average years that players from "Stanford University
#        are active ("active" column)"""
#     average t.. ?.e.. S.. A.. C..(active as numeric))
#                                  f.. players
#                                  w.. college="Stanford University" 0 0
#     r.. r.. ? 2
#
#
# ___ year_with_most_drafts
#     """Return the year with the most drafts, in SQL you can use GROUP BY"""
#     drafts t.. ?.e.. S.. C.. year as numeric C..(year)
#                                 f.. players
#                                 G.. B. year
#                                 O.. B. C.. (year)
#     r.. ? -1 0
