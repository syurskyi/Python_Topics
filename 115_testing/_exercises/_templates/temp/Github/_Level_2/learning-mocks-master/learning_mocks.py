import os

import re
import requests
from selenium import webdriver
from lxml import html

c_ FileRemovalService(object):
    ___ rm  filename):
        if os.path.isfile(filename):
            os.remove(filename)


c_ UploadService(object):

    ___  -   removal_service):
        self.removal_service = removal_service

    ___ upload_complete  filename):
        self.removal_service.rm(filename)


___ rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)

___ get_hrefs_from_url(url):
    page = requests.get(url)
    content = html.fromstring(page.content)
    return content.xpath('//a/@href')


___ filter_hrefs_by_text(hrefs_list, filter_string):
    regex = re.compile('^http[s]?://\S*{0}\S*'.format(filter_string))
    return [h for h in hrefs_list if regex.search(h)]

___ main():
    pass


if __name__ == "__main__":
    main()
