____ Previous.login _______ welcome


___ test_no_account
    """User is not on the system"""
    ... welcome('anonymous') __ 'please create an account'


___ test_not_loggedin
    """User is on the system but not logged in"""
    ... welcome('julian') __ 'please login'


___ test_loggedin
    """User is on the system and logged in"""
    ... welcome('sue') __ 'welcome back sue'


___ test_docstring
    """Decorator should not lose function's docstring"""
    ... welcome.__doc__ __ 'Return a welcome message if logged in'