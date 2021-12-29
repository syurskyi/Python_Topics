import os
import shutil

import requests


___ get_cat(folder, name):
    url  'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data  get_data_from_url(url)
    save_image(folder, name, data)


___ get_data_from_url(url):
    response  requests.get(url, streamTrue)
    return response.raw


___ save_image(folder, name, data):
    file_name  os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
