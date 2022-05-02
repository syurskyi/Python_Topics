____ c.. _______ d..

RESULTS d..(win=0, draw=1, loss=2)


___ invert_result(result
    __ result __ 0:
        r.. 2
    ____ result __ 2:
        r.. 0
    r.. result


___ parse_game(game_line
    game game_line.s..(';')
    __ l..(game) __ 3 a.. game[2] __ RESULTS:
        result RESULTS[game[2]]
        r.. (game[0], result), (game[1], invert_result(result
    r..    # list


___ calculate_points(stats
    r.. stats[0] * 3 + stats[1]


___ format_table(results
    table =  'Team                           | MP |  W |  D |  L |  P'

    ___ team, games __ s..(
            results.i.., k.._l.... g: (-calculate_points(g[1]), g[0]:
        team_fmt '{0:30} | {1:2} | {3:2} | {4:2} | {5:2} | {2:2}'
        table.a..(
            team_fmt.f..(team, s..(games), calculate_points(games), *games

    r.. '\n'.j..(table)


___ tally(data
    table d..(l....: [0, 0, 0])

    ___ line __ data.s..('\n'
        ___ team, result __ parse_game(line
            table[team][result] += 1

    r.. format_table(table)
