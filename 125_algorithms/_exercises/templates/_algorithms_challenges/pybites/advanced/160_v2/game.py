_______ csv
_______ os
____ urllib.request _______ urlretrieve
____ collections _______ defaultdict

BATTLE_DATA = os.path.j..('/tmp', 'battle-table.csv')
__ n.. os.path.isfile(BATTLE_DATA):
    urlretrieve('https://bit.ly/2U3oHft', BATTLE_DATA)


___ _create_defeat_mapping
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    result = defaultdict(d..)
    with open(BATTLE_DATA) __ b:
        reader = csv.DictReader(b)
        ___ row __ reader:
            result[row['Attacker']] = row
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
    defeat_mapping = defeat_mapping o. _create_defeat_mapping()
    __ player1 n.. __ defeat_mapping o. player2 n.. __ defeat_mapping:
        raise ValueError()
    r.. {'win': player1,
            'lose': player2,
            'draw': 'Tie'}[defeat_mapping[player1][player2]]
