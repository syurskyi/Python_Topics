from collections ______ defaultdict

RESULTS = dict(win=0, draw=1, loss=2)


___ invert_result(result
    __ result __ 0:
        r_ 2
    ____ result __ 2:
        r_ 0
    r_ result


___ parse_game(game_line
    game = game_line.split(';')
    __ le.(game) __ 3 and game[2] in RESULTS:
        result = RESULTS[game[2]]
        r_ (game[0], result), (game[1], invert_result(result))
    r_ []


___ calculate_points(stats
    r_ stats[0] * 3 + stats[1]


___ format_table(results
    table = ['Team                           | MP |  W |  D |  L |  P']

    ___ team, games in sorted(
            results.items(), key=lambda g: (-calculate_points(g[1]), g[0])):
        team_fmt = '{0:30} | {1:2} | {3:2} | {4:2} | {5:2} | {2:2}'
        table.append(
            team_fmt.format(team, su.(games), calculate_points(games), *games))

    r_ '\n'.join(table)


___ tally(data
    table = defaultdict(lambda: [0, 0, 0])

    ___ line in data.split('\n'
        ___ team, result in parse_game(line
            table[team][result] += 1

    r_ format_table(table)
