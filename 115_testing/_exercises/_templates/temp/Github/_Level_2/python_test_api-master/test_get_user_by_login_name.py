____ base_api ______ BaseApi
______ xmltodict
______ requests


c_ TestGetUserByLoginName(BaseApi

    ___ test_get_user_by_login_name
        url _ base_url + '/user/' + settings['credentials']['login']

        r _ request(url, 'get')

        assert_for_status_code_and_content_type(r, 200)
        validate_xml(r, 'xsd/user.xsd')

    ___ test_get_user_by_not_existing_login_name
        url _ base_url + '/user/' + 'smash'

        r _ request(url, 'get')

        response_dict _ xmltodict.parse(r.text)

        assert_for_status_code_and_content_type(r, 403)
        aT..(response_dict['error'])

    ___ test_get_user_by_login_name_without_credentials
        url _ base_url + '/user/' + settings['credentials']['login']

        r _ requests.get(url)

        assert_for_status_code_and_content_type(r, 401)

        response_dict _ xmltodict.parse(r.text)

        aT..(response_dict['error'])
