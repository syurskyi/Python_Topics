from login import welcome


___ test_no_account():
    """User is not on the system"""
    assert welcome('anonymous') == 'please create an account'


___ test_not_loggedin():
    """User is on the system but not logged in"""
    assert welcome('julian') == 'please login'


___ test_loggedin():
    """User is on the system and logged in"""
    assert welcome('sue') == 'welcome back sue'


___ test_docstring():
    """Decorator should not lose function's docstring"""
    assert welcome.__doc__ == 'Return a welcome message if logged in'