
c_ MyService:

    ___  -   sso_registry
        sso_registry _ sso_registry

    ___ handle_request_correctly  request, token
        __ sso_registry.is_valid(token
            r_ "hello world"
        r_ "please enter your login details"

    ___ handle_request_wrong_token  request, token
        __ sso_registry.is_valid(N..
            r_ "hello world"
        r_ "please enter your login details"

    ___ handle_request_no_call_to_is_valid  request, token
        __ token:
            r_ "hello world"
        r_ "please enter your login details"

    handle_request _ handle_request_correctly