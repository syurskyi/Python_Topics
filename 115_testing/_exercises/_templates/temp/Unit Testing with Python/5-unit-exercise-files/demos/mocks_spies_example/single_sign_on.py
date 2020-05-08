
c_ SingleSignOnRegistry:
    
    ___ register  credentials):
        pass
    
    ___ is_valid  token):
        pass
        
    ___ end_session  token):
        pass

c_ FakeSingleSignOnRegistry:

    ___  - (self):
        self.tokens = set()

    ___ register  credentials):
        if are_valid(credentials):
            token = SSOToken()
            self.tokens.add(token)
            return token

    ___ is_valid  token):
        return token in self.tokens

    ___ end_session  token):
        self.tokens.remove(token)

c_ MockSingleSignOnRegistry:

    ___  -   expected_token, token_is_valid=True):
        self.expected_token = expected_token
        self.token_is_valid = token_is_valid
        self.is_valid_was_called = False

    ___ is_valid  token):
        self.is_valid_was_called = True
        if not token == self.expected_token:
            raise Exception("This mock was given an unexpected argument. Expected {0} got {1}".format(self.expected_token, token))
        return self.token_is_valid

c_ SpySingleSignOnRegistry:

    ___  -   accept_all_tokens = True):
        self.accept_all_tokens = accept_all_tokens
        self.checked_tokens = []

    ___ is_valid  token):
        self.checked_tokens.append(token)
        return self.accept_all_tokens


c_ SSOToken:
    pass

___ are_valid(credentials):
    #check the credentials
    return True
