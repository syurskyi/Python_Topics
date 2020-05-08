
c_ MyService:

    ___  -   sso_registry):
        self.sso_registry = sso_registry

    ___ handle_request_correctly  request, token):
        if self.sso_registry.is_valid(token):
            return "hello world"
        return "please enter your login details"

    ___ handle_request_wrong_token  request, token):
        if self.sso_registry.is_valid(None):
            return "hello world"
        return "please enter your login details"

    ___ handle_request_no_call_to_is_valid  request, token):
        if token:
            return "hello world"
        return "please enter your login details"

    handle_request = handle_request_correctly