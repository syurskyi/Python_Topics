______ u__
______ requests
______ xmltodict


c_ TestGetIssue?.?

    ___ setUp
        base_url _ 'https://codespace-api.myjetbrains.com/youtrack/rest'
        creds _ ('root', 'c11desp@ce')

    ___ test_get_issue
        id _ 'API-1'
        url _ base_url + '/issue/' + id
        response _ requests.get(url, auth_creds)
        response_dict _ xmltodict.parse(response.text)

        assertEquals(response.status_code, 200)
        assertEquals(response_dict['issue']['@id'], id)
        assertEquals(response.headers['Content-Type'], 'application/xml;charset=UTF-8')
        print "Response time is: " + st.(response.elapsed.total_seconds())

    ___ test_get_issue_invalid_id
        url _ base_url + '/issue/' + '123'
        r _ requests.get(url, auth_creds)
        r_dict _ xmltodict.parse(r.text)

        assertEquals(r.status_code, 404)
        # assert r.status_code == 403
        assertEquals(r_dict['error'], 'Issue not found.')
        assertEquals(r.headers['Content-Type'], 'application/xml;charset=UTF-8')

__ _____ __ _____
    ?.?
