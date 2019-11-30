# # -*- coding: utf-8 -*-

def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)


# [*] Время выполнения: 1.4475083351135254 секунд.
# <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage"........