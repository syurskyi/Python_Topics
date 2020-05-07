from base_api import BaseApi
import xmltodict
import requests


class TestGetAccessibleProjects(BaseApi):

    def test_get_accessible_projects(self):
        url = self.base_url + '/project/all'

        r = self.request(url, 'get')

        self.assert_for_status_code_and_content_type(r, 200)

        response_dict = xmltodict.parse(r.text)

        for x in response_dict['projects']['project']:
            self.assertTrue(x['@name'])
            self.assertTrue(x['@shortName'])

    def test_get_accessible_projects_without_credentials(self):
        url = self.base_url + '/project/all'

        r = requests.get(url)

        self.assert_for_status_code_and_content_type(r, 401)

        response_dict = xmltodict.parse(r.text)

        self.assertTrue(response_dict['error'])
