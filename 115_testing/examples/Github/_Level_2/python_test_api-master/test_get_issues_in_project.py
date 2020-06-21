from base_api import BaseApi
import random
import xmltodict
import requests


class TestGetIssuesInProject(BaseApi):

    def test_get_issues_in_project(self):
        projects_list = self._get_accessible_projects()

        project_name = random.choice(projects_list)

        url = self.base_url + '/issue/byproject/' + project_name

        params = {
            'max': '10'
        }

        r = requests.get(url, params, cookies=self.cookies)
        self.log_full(r)

        self.assert_for_status_code_and_content_type(r, 200)

        response_dict = xmltodict.parse(r.text)

        for x in response_dict['issues']['issue']:
            self.assertTrue(x['@id'])
            self.assertTrue(x['@entityId'])
            for y in x['field']:
                self.assertTrue(y['@xmlns:xsi'])
                self.assertTrue(y['@xsi:type'])
                self.assertTrue(y['@name'])
                self.assertTrue(y['value'])

        # self.validate_xml(r, 'xsd/issues.xsd')

    def test_get_issues_in_not_existing_project(self):
        url = self.base_url + '/issue/byproject/' + 'kjhfjkafsasf'

        params = {
            'max': '10'
        }

        r = requests.get(url, params, cookies=self._login())
        self.log_full(r)

        self.assert_for_status_code_and_content_type(r, 404)

        response_dict = xmltodict.parse(r.text)
        self.assertTrue(response_dict['error'])

    def test_get_issues_in_project_without_credentials(self):
        projects_list = self._get_accessible_projects()

        project_name = random.choice(projects_list)

        url = self.base_url + '/issue/byproject/' + project_name

        params = {
            'max': '10'
        }

        r = requests.get(url, params)
        self.log_full(r)

        self.assert_for_status_code_and_content_type(r, 401)

        response_dict = xmltodict.parse(r.text)

        self.assertTrue(response_dict['error'])
