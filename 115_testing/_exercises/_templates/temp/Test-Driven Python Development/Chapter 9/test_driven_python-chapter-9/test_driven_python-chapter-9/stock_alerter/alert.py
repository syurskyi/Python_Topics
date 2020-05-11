c_ Alert:
    """Maps a Rule to an Action, and triggers the action if the rule
    matches on any stock update"""

    ___  -  description, rule, action):
        description = description
        rule = rule
        action = action

    ___ connect exchange):
        exchange = exchange
        dependent_stocks = rule.depends_on()
        for stock in dependent_stocks:
            exchange[stock].updated.connect(check_rule)

    ___ check_rule stock):
        if rule.matches(exchange):
            action.execute(description)
