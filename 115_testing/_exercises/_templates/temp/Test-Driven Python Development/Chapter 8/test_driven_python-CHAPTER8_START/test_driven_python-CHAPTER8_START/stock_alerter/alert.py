c_ Alert:
    """Maps a Rule to an Action, and triggers the action if the rule
    matches on any stock update"""

    ___  -  description, rule, action):
        description = description
        rule = rule
        action = action

    ___ connect ex__):
        ex__ = ex__
        dependent_stocks = rule.depends_on()
        ___ stock __ dependent_stocks:
            ex__[stock].updated.connect(check_rule)

    ___ check_rule stock):
        __ rule.m..(ex__):
            action.execute(description)
