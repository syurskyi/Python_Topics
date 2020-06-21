____ base_api ______ BaseApi
______ xmltodict
______ requests


c_ TestGetInfoForCurrentUser(BaseApi

    ___ test_get_info_for_current_user
        url _ base_url + '/user/current'

        r _ request(url, 'get')

        assert_for_status_code_and_content_type(r, 200)
        validate_xml(r, 'xsd/user.xsd')

    ___ test_get_info_for_current_user_without_credentials
        url _ base_url + '/user/current'

        r _ requests.get(url)

        assert_for_status_code_and_content_type(r, 200)

        response_dict _ xmltodict.parse(r.text)

        aT..(response_dict['user'])
        aE..(response_dict['user']['@login'], '<no user>')
        aE..(response_dict['user']['@guest'], 'false')
