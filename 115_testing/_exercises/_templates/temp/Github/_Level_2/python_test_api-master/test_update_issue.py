____ base_api ______ BaseApi
______ xmltodict
______ d_t_
______ requests


c_ TestUpdateIssue(BaseApi

    ___ test_update_issue
        issue_id _ _create_issue()  # obviously we need to create an issue before updating it

        url _ base_url + '/issue/' + issue_id

        current_time _ st.(d_t_.d_t_.now())[0:-7]

        issue_summary _ 'Summary updated at ' + current_time
        issue_description _ 'Description updated at ' + current_time

        params _ {
            'summary': issue_summary,
            'description': issue_description
        }

        r _ request(url, 'post', params)

        assert_for_status_code_and_content_type(r, 200, 'text/plain;charset=UTF-8')

        url _ base_url + '/issue/' + issue_id
        r _ request(url, 'get')

        response_dict _ xmltodict.parse(r.text)

        assert_for_status_code_and_content_type(r, 200)

        aE..(response_dict['issue']['@id'], issue_id)
        ___ field __ response_dict['issue']['field']:
            __ field['@name'] __ 'summary':
                aE..(field['value'], issue_summary)
            __ field['@name'] __ 'description':
                aE..(field['value'], issue_description)

    ___ test_update_not_existing_issue
        url _ base_url + '/issue/' + 'kjhfkaskafk'

        current_time _ st.(d_t_.d_t_.now())[0:-7]

        issue_summary _ 'Summary updated at ' + current_time
        issue_description _ 'Description updated at ' + current_time

        params _ {
            'summary': issue_summary,
            'description': issue_description
        }

        r _ request(url, 'post', params)

        response_dict _ xmltodict.parse(r.text)

        assert_for_status_code_and_content_type(r, 404)
        aT..(response_dict['error'])

    ___ test_update_issue_without_credentials
        issue_id _ _create_issue()
        url _ base_url + '/issue/' + issue_id

        current_time _ st.(d_t_.d_t_.now())[0:-7]

        issue_summary _ 'Summary updated at ' + current_time
        issue_description _ 'Description updated at ' + current_time

        params _ {
            'summary': issue_summary,
            'description': issue_description
        }

        r _ requests.post(url, params)

        assert_for_status_code_and_content_type(r, 401)

        response_dict _ xmltodict.parse(r.text)

        aT..(response_dict['error'])
