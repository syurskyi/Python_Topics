____ nba _______ (cur,
                 player_with_max_points_per_game,
                 number_of_players_from_duke,
                 avg_years_active_players_stanford,
                 year_with_most_new_players)


___ test_total_row_count_after_import
    sql '''SELECT COUNT(*) FROM players'''
    cur.execute(sql)
    ret cur.fetchall()
    ... ret[0][0] __ 3961


___ test_player_with_max_points_per_game
    ... player_with_max_points_per_game() __ 'Michael Jordan'


___ test_number_of_players_from_duke
    ... number_of_players_from_duke() __ 58


___ test_avg_years_active_players_stanford
    ... r..(avg_years_active_players_stanford(), 2) __ 4.58


___ test_year_with_most_new_players
    ... i..(year_with_most_new_players __ 1984
