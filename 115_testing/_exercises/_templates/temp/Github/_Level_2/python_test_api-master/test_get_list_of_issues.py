____ base_api ______ BaseApi
______ xmltodict
______ requests


c_ TestGetListOfIssues(BaseApi

    ___ test_get_list_of_issues
        url _ base_url + '/issue'

        params _ {
            'with': 'Priority',
            'max': '10',
            'after': '20'
        }

        r _ request(url, 'get', params)

        response_dict _ xmltodict.parse(r.text)

        assert_for_status_code_and_content_type(r, 200)
        ___ x __ response_dict['issueCompacts']['issue']:
            aT..(x['@id'])

    ___ test_get_list_of_issues_without_credentials
        url _ base_url + '/issue'

        params _ {
            'with': 'Priority',
            'max': '10',
            'after': '20'
        }

        r _ requests.get(url, params)

        assert_for_status_code_and_content_type(r, 401)

        response_dict _ xmltodict.parse(r.text)

        aT..(response_dict['error'])
