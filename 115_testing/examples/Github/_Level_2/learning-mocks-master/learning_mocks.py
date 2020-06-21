import os

import re
import requests
from selenium import webdriver
from lxml import html

class FileRemovalService(object):
    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)


class UploadService(object):

    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, filename):
        self.removal_service.rm(filename)


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)

def get_hrefs_from_url(url):
    page = requests.get(url)
    content = html.fromstring(page.content)
    return content.xpath('//a/@href')


def filter_hrefs_by_text(hrefs_list, filter_string):
    regex = re.compile('^http[s]?://\S*{0}\S*'.format(filter_string))
    return [h for h in hrefs_list if regex.search(h)]

def main():
    pass


if __name__ == "__main__":
    main()
