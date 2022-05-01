_______ c__
_______ __
____ u__.r.. _______ u..
____ c.. _______ d..

BATTLE_DATA __.p...j..('/tmp', 'battle-table.csv')
__ n.. __.p...i..(BATTLE_DATA
    u..('https://bit.ly/2U3oHft', BATTLE_DATA)


___ _create_defeat_mapping
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    result d..(d..)
    w__ o.. BATTLE_DATA) __ b:
        reader c__.D.. b)
        ___ row __ ?
            result[row 'Attacker']] row
    r.. result


___ get_winner(player1, player2, defeat_mapping_ N..
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping defeat_mapping o. _create_defeat_mapping()
    __ player1 n.. __ defeat_mapping o. player2 n.. __ defeat_mapping:
        r.. V...()
    r.. {'win': player1,
            'lose': player2,
            'draw': 'Tie'}[defeat_mapping[player1][player2]]
