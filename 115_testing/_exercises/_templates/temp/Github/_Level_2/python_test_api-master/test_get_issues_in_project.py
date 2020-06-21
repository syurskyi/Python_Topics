____ base_api ______ BaseApi
______ ra__
______ xmltodict
______ requests


c_ TestGetIssuesInProject(BaseApi

    ___ test_get_issues_in_project
        projects_list _ _get_accessible_projects()

        project_name _ ra__.ch..(projects_list)

        url _ base_url + '/issue/byproject/' + project_name

        params _ {
            'max': '10'
        }

        r _ requests.get(url, params, cookies_cookies)
        log_full(r)

        assert_for_status_code_and_content_type(r, 200)

        response_dict _ xmltodict.parse(r.text)

        ___ x __ response_dict['issues']['issue']:
            aT..(x['@id'])
            aT..(x['@entityId'])
            ___ y __ x['field']:
                aT..(y['@xmlns:xsi'])
                aT..(y['@xsi:type'])
                aT..(y['@name'])
                aT..(y['value'])

        # self.validate_xml(r, 'xsd/issues.xsd')

    ___ test_get_issues_in_not_existing_project
        url _ base_url + '/issue/byproject/' + 'kjhfjkafsasf'

        params _ {
            'max': '10'
        }

        r _ requests.get(url, params, cookies__login())
        log_full(r)

        assert_for_status_code_and_content_type(r, 404)

        response_dict _ xmltodict.parse(r.text)
        aT..(response_dict['error'])

    ___ test_get_issues_in_project_without_credentials
        projects_list _ _get_accessible_projects()

        project_name _ ra__.ch..(projects_list)

        url _ base_url + '/issue/byproject/' + project_name

        params _ {
            'max': '10'
        }

        r _ requests.get(url, params)
        log_full(r)

        assert_for_status_code_and_content_type(r, 401)

        response_dict _ xmltodict.parse(r.text)

        aT..(response_dict['error'])
