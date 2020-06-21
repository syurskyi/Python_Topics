____ base_api ______ BaseApi


c_ TestDeleteIssue(BaseApi

    ___ test_delete_issue
        issue_id _ _create_issue()

        url _ base_url + '/issue/' + issue_id
        r _ request(url, 'delete')

        assertEquals(r.status_code, 200)

        r _ request(url, 'get')
        assertEquals(r.status_code, 404)

    ___ test_delete_nonexistent_issue
        url _ base_url + '/issue/' + 'ERUNDA'
        r _ request(url, 'delete')

        assertEquals(r.status_code, 404)
