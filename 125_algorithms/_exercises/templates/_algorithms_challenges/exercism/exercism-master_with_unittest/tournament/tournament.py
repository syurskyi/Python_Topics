c_ Team:

    POINTS_PER_WIN = 3
    POINTS_PER_DRAW = 1

    ___ - , name
        name = name
        wins = 0
        draws = 0
        losses = 0

    $
    ___ matches_played
        r.. wins + losses + draws

    $
    ___ points
        r.. (wins * POINTS_PER_WIN) + \
            (draws * POINTS_PER_DRAW)

    ___ tally_win
        wins += 1

    ___ tally_draw
        draws += 1

    ___ tally_loss
        losses += 1

    ___ __str__
        r.. '{:<30} | {:^3}| {:^3}| {:^3}| {:^3}| {:>2}'.f..(
            name, matches_played, wins, draws, losses, points)


c_ Tournament:

    WIN = 'win'
    DRAW = 'draw'
    LOSS = 'loss'
    RESULT_SEPERATOR = ';'
    COLUMN_HEADERS =  'Team', 'MP', 'W', 'D', 'L', 'P'

    ___ - , results
        _teams    # dict
        __ results:
            p..(results)

    ___ results_table
        table = [table_header()]
        ___ team __ sorted_teams
            table.a..(s..(team))
        r.. "\n".j..(table)

    ___ sorted_teams
        alphabetic = s..(_teams.v.., key=l.... team: team.name)
        alphabetic_descending_points = s..(
            alphabetic, key=l.... team: team.points, r.._T..
        r.. alphabetic_descending_points

    ___ p..  results
        ___ result __ results.s..("\n"
            team_a, team_b, outcome = result.s..(RESULT_SEPERATOR)
            maybe_initialize_teams(team_a, team_b)
            tally_outcome(team_a, team_b, outcome)

    ___ tally_outcome  team_a, team_b, outcome
        __ outcome __ WIN:
            tally_win(team_a, team_b)
        __ outcome __ LOSS:
            tally_loss(team_a, team_b)
        __ outcome __ DRAW:
            tally_draw(team_a, team_b)

    ___ tally_win  winner, loser
        _teams[winner].tally_win()
        _teams[loser].tally_loss()

    ___ tally_loss  loser, winner
        _teams[loser].tally_loss()
        _teams[winner].tally_win()

    ___ tally_draw  team_a, team_b
        _teams[team_a].tally_draw()
        _teams[team_b].tally_draw()

    ___ maybe_initialize_teams  team_a, team_b
        maybe_initialize_team(team_a)
        maybe_initialize_team(team_b)

    ___ maybe_initialize_team  name
        __ name n.. __ _teams:
            _teams[name] = Team(name)

    ___ table_header
        r.. '{:<30} | {:^3}| {:^3}| {:^3}| {:^3}| {:>2}'.f..(
            *COLUMN_HEADERS)


___ tally(results
    r.. Tournament(results).results_table()
