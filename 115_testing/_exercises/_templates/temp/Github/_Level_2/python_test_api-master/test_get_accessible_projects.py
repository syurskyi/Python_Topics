____ base_api ______ BaseApi
______ xmltodict
______ requests


c_ TestGetAccessibleProjects(BaseApi

    ___ test_get_accessible_projects
        url _ base_url + '/project/all'

        r _ request(url, 'get')

        assert_for_status_code_and_content_type(r, 200)

        response_dict _ xmltodict.parse(r.text)

        ___ x __ response_dict['projects']['project']:
            aT..(x['@name'])
            aT..(x['@shortName'])

    ___ test_get_accessible_projects_without_credentials
        url _ base_url + '/project/all'

        r _ requests.get(url)

        assert_for_status_code_and_content_type(r, 401)

        response_dict _ xmltodict.parse(r.text)

        aT..(response_dict['error'])
