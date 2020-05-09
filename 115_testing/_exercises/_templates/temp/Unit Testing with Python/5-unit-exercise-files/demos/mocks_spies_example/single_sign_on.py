
c_ SingleSignOnRegistry:
    
    ___ register  credentials
        pass
    
    ___ is_valid  token
        pass
        
    ___ end_session  token
        pass

c_ FakeSingleSignOnRegistry:

    ___  -
        tokens _ set()

    ___ register  credentials
        if are_valid(credentials
            token _ SSOToken()
            tokens.add(token)
            r_ token

    ___ is_valid  token
        r_ token in tokens

    ___ end_session  token
        tokens.remove(token)

c_ MockSingleSignOnRegistry:

    ___  -   expected_token, token_is_valid_True
        expected_token _ expected_token
        token_is_valid _ token_is_valid
        is_valid_was_called _ False

    ___ is_valid  token
        is_valid_was_called _ True
        if not token == expected_token:
            raise Exception("This mock was given an unexpected argument. Expected {0} got {1}".f..(expected_token, token))
        r_ token_is_valid

c_ SpySingleSignOnRegistry:

    ___  -   accept_all_tokens _ True
        accept_all_tokens _ accept_all_tokens
        checked_tokens _ []

    ___ is_valid  token
        checked_tokens.append(token)
        r_ accept_all_tokens


c_ SSOToken:
    pass

___ are_valid(credentials
    #check the credentials
    r_ True
