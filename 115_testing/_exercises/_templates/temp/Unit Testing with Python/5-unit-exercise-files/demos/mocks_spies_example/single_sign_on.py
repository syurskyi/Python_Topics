
c_ SingleSignOnRegistry:
    
    ___ register  credentials
        p..
    
    ___ is_valid  token
        p..
        
    ___ end_session  token
        p..

c_ FakeSingleSignOnRegistry:

    ___  -
        tokens _ se.()

    ___ register  credentials
        __ are_valid(credentials
            token _ SSOToken()
            tokens.add(token)
            r_ token

    ___ is_valid  token
        r_ token __ tokens

    ___ end_session  token
        tokens.re..(token)

c_ MockSingleSignOnRegistry:

    ___  -   expected_token, token_is_valid_True
        expected_token _ expected_token
        token_is_valid _ token_is_valid
        is_valid_was_called _ F..

    ___ is_valid  token
        is_valid_was_called _ T..
        __ no. token __ expected_token:
            r_ E..("This mock was given an unexpected argument. Expected {0} got {1}".f..(expected_token, token))
        r_ token_is_valid

c_ SpySingleSignOnRegistry:

    ___  -   accept_all_tokens _ T..
        accept_all_tokens _ accept_all_tokens
        checked_tokens _ # list

    ___ is_valid  token
        checked_tokens.a..(token)
        r_ accept_all_tokens


c_ SSOToken:
    p..

___ are_valid(credentials
    #check the credentials
    r_ T..
