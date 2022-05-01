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
#     r__.c..(s__.a..) ___ i __ r..(20)
#
# DB ? / _*nba_?.db
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
#     ?.e.. I.. I.. players V.. (?,?,?,?,?,?,?,?,?)' ?
#     ?.c..
#
#
# ?
#
#
# # you code:
#
# ___ player_with_max_points_per_game
#     """The player with highest average points per game (don't forget to CAST to
#        numeric in your SQL query)"""
#     cursor ?.e..
#
#         S..
#             name,
#             M.. C..(avg_points A. I..)) A. points
#         F.. players
#         "
#     r.. n.. ? 0
#
#
# ___ number_of_players_from_duke
#     """Return the number of players with college == Duke University"""
#     cursor ?.e..
#
#         S..
#             C..(*) A. record_count
#         F.. players
#         W.. college = 'Duke University'
#
#
#     r.. n.. ? 0
#
#
# ___ avg_years_active_players_stanford
#     """Return the average years that players from "Stanford University
#        are active ("active" column)"""
#     cursor ?.e..
#
#         S..
#             A..(active) A. avg_years
#         F.. players
#         W.. college = 'Stanford University'
#
#
#     r.. n.. ?  0
#
#
# ___ year_with_most_new_players
#     """Return the year with the most new players.
#        Hint: you can use GROUP BY on the year column.
#     """
#     cursor ?.e..
#         "
#         W.. years_staging A. (
#             S..
#                 C.. C..(first_year A. I..)) new_players,
#                 year
#             F.. players
#             G.. B. year)
#
#         S.. M..(new_players), year
#         F.. years_staging
#         "
#
#     r.. n.. ? 1
#
#
# # if __name__ == "__main__":
# #     print(player_with_max_points_per_game())
# #     print(number_of_players_from_duke())
# #     print(avg_years_active_players_stanford())
# #     print(year_with_most_new_players())