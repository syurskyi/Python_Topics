import unittest
import requests
import xmltodict


class TestGetIssue(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://codespace-api.myjetbrains.com/youtrack/rest'
        self.creds = ('root', 'c11desp@ce')

    def test_get_issue(self):
        self.id = 'API-1'
        url = self.base_url + '/issue/' + self.id
        response = requests.get(url, auth=self.creds)
        response_dict = xmltodict.parse(response.text)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response_dict['issue']['@id'], self.id)
        self.assertEquals(response.headers['Content-Type'], 'application/xml;charset=UTF-8')
        print "Response time is: " + str(response.elapsed.total_seconds())

    def test_get_issue_invalid_id(self):
        url = self.base_url + '/issue/' + '123'
        r = requests.get(url, auth=self.creds)
        r_dict = xmltodict.parse(r.text)

        self.assertEquals(r.status_code, 404)
        # assert r.status_code == 403
        self.assertEquals(r_dict['error'], 'Issue not found.')
        self.assertEquals(r.headers['Content-Type'], 'application/xml;charset=UTF-8')

if __name__ == '__main__':
    unittest.main()
