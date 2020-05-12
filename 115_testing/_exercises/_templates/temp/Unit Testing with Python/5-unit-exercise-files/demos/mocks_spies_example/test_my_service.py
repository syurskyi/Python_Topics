______ u__
____ u__.m.. ______ *

____ my_service ______ MyService
____ single_sign_on ______ *

c_ MyServiceTest?.?
    ___ test_invalid_token
        registry _ FakeSingleSignOnRegistry()
        my_service _ MyService(registry)

        response _ my_service.handle_request("do stuff", token_None)
        aI..("please enter your login details", response)
        
    ___ test_valid_token
        registry _ FakeSingleSignOnRegistry()
        token _ registry.register("valid credentials")
        my_service _ MyService(registry)
    
        response _ my_service.handle_request("do stuff", token)
        aI..("hello world", response)
        
    ___ test_invalid_token_with_mock
        token _ SSOToken()
        registry _ MockSingleSignOnRegistry(expected_token_token, token_is_valid_False)
        my_service _ MyService(registry)

        response _ my_service.handle_request("do stuff", token_token)
        aT..(registry.is_valid_was_called)

    ___ test_valid_token_with_mock
        token _ SSOToken()
        registry _ MockSingleSignOnRegistry(expected_token_token, token_is_valid_True)
        my_service _ MyService(registry)

        response _ my_service.handle_request("do stuff", token)
        aT..(registry.is_valid_was_called)

    ___ test_invalid_token_with_spy
        token _ SSOToken()
        registry _ SpySingleSignOnRegistry(accept_all_tokens_False)
        my_service _ MyService(registry)

        response _ my_service.handle_request("do stuff", token_token)
        aI..(token, registry.checked_tokens)

    ___ test_valid_token_with_spy
        token _ SSOToken()
        registry _ SpySingleSignOnRegistry(accept_all_tokens_True)
        my_service _ MyService(registry)

        response _ my_service.handle_request("do stuff", token)
        aI..(token, registry.checked_tokens)

    ___ test_invalid_token_with_mocking_fw_as_spy
        token _ SSOToken()
        registry _ Mock(SingleSignOnRegistry)
        registry.is_valid _ Mock(return_value_False)
        my_service _ MyService(registry)

        response _ my_service.handle_request("do stuff", token_token)
        registry.is_valid.a_c_w..(token)

    ___ test_valid_token_with_mocking_fw_as_spy
        token _ SSOToken()
        registry _ Mock(SingleSignOnRegistry)
        registry.is_valid _ Mock(return_value_True)
        my_service _ MyService(registry)

        response _ my_service.handle_request("do stuff", token)
        registry.is_valid.a_c_w..(token)

    ___ test_invalid_token_with_mocking_fw_as_mock
        invalid_token _ SSOToken()
        registry _ Mock(SingleSignOnRegistry)
        ___ is_valid(token
            __ no. token __ invalid_token:
                r_ E..("Got the wrong token")
            r_ F..
        registry.is_valid _ Mock(side_effect_is_valid)
        my_service _ MyService(registry)

        response _ my_service.handle_request("do stuff", token_invalid_token)
        registry.is_valid.a_c_w..(invalid_token)

    ___ test_valid_token_with_mocking_fw_as_mock
        valid_token _ SSOToken()
        registry _ Mock(SingleSignOnRegistry)
        ___ is_valid(token
            __ no. token __ valid_token:
                r_ E..("Got the wrong token")
            r_ T..
        registry.is_valid _ Mock(side_effect_is_valid)
        my_service _ MyService(registry)

        response _ my_service.handle_request("do stuff", token_valid_token)
        registry.is_valid.a_c_w..(valid_token)
