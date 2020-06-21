
class SingleSignOnRegistry:
    
    def register(self, credentials):
        pass
    
    def is_valid(self, token):
        pass
        
    def end_session(self, token):
        pass

class FakeSingleSignOnRegistry:

    def __init__(self):
        self.tokens = set()

    def register(self, credentials):
        if are_valid(credentials):
            token = SSOToken()
            self.tokens.add(token)
            return token

    def is_valid(self, token):
        return token in self.tokens

    def end_session(self, token):
        self.tokens.remove(token)

class MockSingleSignOnRegistry:

    def __init__(self, expected_token, token_is_valid=True):
        self.expected_token = expected_token
        self.token_is_valid = token_is_valid
        self.is_valid_was_called = False

    def is_valid(self, token):
        self.is_valid_was_called = True
        if not token == self.expected_token:
            raise Exception("This mock was given an unexpected argument. Expected {0} got {1}".format(self.expected_token, token))
        return self.token_is_valid

class SpySingleSignOnRegistry:

    def __init__(self, accept_all_tokens = True):
        self.accept_all_tokens = accept_all_tokens
        self.checked_tokens = []

    def is_valid(self, token):
        self.checked_tokens.append(token)
        return self.accept_all_tokens


class SSOToken:
    pass

def are_valid(credentials):
    #check the credentials
    return True
