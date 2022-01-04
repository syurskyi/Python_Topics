_______ os
_______ shutil

_______ requests


___ get_cat(folder, name):
    url  'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data  get_data_from_url(url)
    save_image(folder, name, data)


___ get_data_from_url(url):
    response  requests.get(url, streamTrue)
    r.. response.raw


___ save_image(folder, name, data):
    file_name  os.path.j..(folder, name + '.jpg')
    w__ open(file_name, 'wb') __ fout:
        shutil.copyfileobj(data, fout)
