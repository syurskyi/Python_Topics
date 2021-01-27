from Previous.login import welcome


def test_no_account():
    """User is not on the system"""
    a__ welcome('anonymous') == 'please create an account'


def test_not_loggedin():
    """User is on the system but not logged in"""
    a__ welcome('julian') == 'please login'


def test_loggedin():
    """User is on the system and logged in"""
    a__ welcome('sue') == 'welcome back sue'


def test_docstring():
    """Decorator should not lose function's docstring"""
    a__ welcome.__doc__ == 'Return a welcome message if logged in'