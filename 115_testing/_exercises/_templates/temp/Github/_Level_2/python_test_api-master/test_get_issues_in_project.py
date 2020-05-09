____ base_api ______ BaseApi
______ random
______ xmltodict
______ requests


c_ TestGetIssuesInProject(BaseApi

    ___ test_get_issues_in_project
        projects_list _ _get_accessible_projects()

        project_name _ random.choice(projects_list)

        url _ base_url + '/issue/byproject/' + project_name

        params _ {
            'max': '10'
        }

        r _ requests.get(url, params, cookies_cookies)
        log_full(r)

        assert_for_status_code_and_content_type(r, 200)

        response_dict _ xmltodict.parse(r.text)

        for x in response_dict['issues']['issue']:
            assertTrue(x['@id'])
            assertTrue(x['@entityId'])
            for y in x['field']:
                assertTrue(y['@xmlns:xsi'])
                assertTrue(y['@xsi:type'])
                assertTrue(y['@name'])
                assertTrue(y['value'])

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
        assertTrue(response_dict['error'])

    ___ test_get_issues_in_project_without_credentials
        projects_list _ _get_accessible_projects()

        project_name _ random.choice(projects_list)

        url _ base_url + '/issue/byproject/' + project_name

        params _ {
            'max': '10'
        }

        r _ requests.get(url, params)
        log_full(r)

        assert_for_status_code_and_content_type(r, 401)

        response_dict _ xmltodict.parse(r.text)

        assertTrue(response_dict['error'])
