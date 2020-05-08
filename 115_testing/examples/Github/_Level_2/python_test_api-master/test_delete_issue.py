from base_api import BaseApi


class TestDeleteIssue(BaseApi):

    def test_delete_issue(self):
        issue_id = self._create_issue()

        url = self.base_url + '/issue/' + issue_id
        r = self.request(url, 'delete')

        self.assertEquals(r.status_code, 200)

        r = self.request(url, 'get')
        self.assertEquals(r.status_code, 404)

    def test_delete_nonexistent_issue(self):
        url = self.base_url + '/issue/' + 'ERUNDA'
        r = self.request(url, 'delete')

        self.assertEquals(r.status_code, 404)
